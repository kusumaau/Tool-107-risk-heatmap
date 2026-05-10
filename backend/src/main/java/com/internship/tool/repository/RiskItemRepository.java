package com.internship.tool.repository;

import com.internship.tool.entity.RiskItem;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface RiskItemRepository extends JpaRepository<RiskItem, Long> {

    Page<RiskItem> findByDeletedFalse(Pageable pageable);

    List<RiskItem> findByDeletedFalse();

    @Query("SELECT r FROM RiskItem r WHERE r.deleted = false AND " +
           "(LOWER(r.title) LIKE LOWER(CONCAT('%', :q, '%')) OR " +
           "LOWER(r.description) LIKE LOWER(CONCAT('%', :q, '%')))")
    List<RiskItem> searchByQuery(String q);

    List<RiskItem> findByStatusAndDeletedFalse(String status);

    long countByDeletedFalse();

    long countByStatusAndDeletedFalse(String status);
}