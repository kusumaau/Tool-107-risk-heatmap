package com.internship.tool.service;

import com.internship.tool.entity.RiskItem;
import com.internship.tool.exception.ResourceNotFoundException;
import com.internship.tool.repository.RiskItemRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.cache.annotation.CacheEvict;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
@RequiredArgsConstructor
public class RiskItemService {

    private final RiskItemRepository repository;
    private final AiServiceClient aiServiceClient;

    @Cacheable(value = "riskItems")
    public Page<RiskItem> getAll(Pageable pageable) {
        return repository.findByDeletedFalse(pageable);
    }

    @Cacheable(value = "riskItem", key = "#id")
    public RiskItem getById(Long id) {
        return repository.findById(id)
                .filter(r -> !r.getDeleted())
                .orElseThrow(() -> new ResourceNotFoundException("Risk item not found with id: " + id));
    }

    @CacheEvict(value = {"riskItems", "riskItem"}, allEntries = true)
    public RiskItem create(RiskItem item) {
        RiskItem saved = repository.save(item);
        enrichWithAi(saved);
        return saved;
    }

    @CacheEvict(value = {"riskItems", "riskItem"}, allEntries = true)
    public RiskItem update(Long id, RiskItem updated) {
        RiskItem existing = getById(id);
        existing.setTitle(updated.getTitle());
        existing.setDescription(updated.getDescription());
        existing.setLikelihood(updated.getLikelihood());
        existing.setImpact(updated.getImpact());
        existing.setRiskScore(updated.getRiskScore());
        existing.setStatus(updated.getStatus());
        existing.setCategory(updated.getCategory());
        existing.setAffectedAreas(updated.getAffectedAreas());
        return repository.save(existing);
    }

    @CacheEvict(value = {"riskItems", "riskItem"}, allEntries = true)
    public void delete(Long id) {
        RiskItem item = getById(id);
        item.setDeleted(true);
        repository.save(item);
    }

    public List<RiskItem> search(String q) {
        return repository.searchByQuery(q);
    }

    public Map<String, Object> getStats() {
        return Map.of(
                "total", repository.countByDeletedFalse(),
                "open", repository.countByStatusAndDeletedFalse("OPEN"),
                "closed", repository.countByStatusAndDeletedFalse("CLOSED"),
                "inProgress", repository.countByStatusAndDeletedFalse("IN_PROGRESS")
        );
    }

    @Async
    public void enrichWithAi(RiskItem item) {
        try {
            String text = item.getTitle() + " " + item.getDescription();
            String description = aiServiceClient.describe(text);
            String recommendations = aiServiceClient.recommend(text);
            String report = aiServiceClient.generateReport(text);
            item.setAiDescription(description);
            item.setAiRecommendations(recommendations);
            item.setAiReport(report);
            repository.save(item);
        } catch (Exception e) {
            item.setIsFallback(true);
            repository.save(item);
        }
    }
}
