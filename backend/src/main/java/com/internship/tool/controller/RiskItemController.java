package com.internship.tool.controller;

import com.internship.tool.entity.RiskItem;
import com.internship.tool.service.RiskItemService;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/risks")
@RequiredArgsConstructor
@Tag(name = "Risk Items", description = "Risk Heatmap CRUD operations")
@CrossOrigin(origins = "*")
public class RiskItemController {

    private final RiskItemService service;

    @GetMapping
    @Operation(summary = "Get all risk items paginated")
    public ResponseEntity<Page<RiskItem>> getAll(Pageable pageable) {
        return ResponseEntity.ok(service.getAll(pageable));
    }

    @GetMapping("/{id}")
    @Operation(summary = "Get risk item by ID")
    public ResponseEntity<RiskItem> getById(@PathVariable Long id) {
        return ResponseEntity.ok(service.getById(id));
    }

    @PostMapping
    @Operation(summary = "Create a new risk item")
    public ResponseEntity<RiskItem> create(@Valid @RequestBody RiskItem item) {
        return ResponseEntity.status(HttpStatus.CREATED).body(service.create(item));
    }

    @PutMapping("/{id}")
    @Operation(summary = "Update a risk item")
    public ResponseEntity<RiskItem> update(@PathVariable Long id,
                                           @Valid @RequestBody RiskItem item) {
        return ResponseEntity.ok(service.update(id, item));
    }

    @DeleteMapping("/{id}")
    @Operation(summary = "Soft delete a risk item")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        service.delete(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/search")
    @Operation(summary = "Search risk items")
    public ResponseEntity<List<RiskItem>> search(@RequestParam String q) {
        return ResponseEntity.ok(service.search(q));
    }

    @GetMapping("/stats")
    @Operation(summary = "Get risk item statistics")
    public ResponseEntity<Map<String, Object>> getStats() {
        return ResponseEntity.ok(service.getStats());
    }
}