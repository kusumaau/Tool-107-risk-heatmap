package com.internship.tool.service;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;
import org.springframework.boot.web.client.RestTemplateBuilder;

import java.time.Duration;
import java.util.Map;

@Service
public class AiServiceClient {

    private static final Logger logger = LoggerFactory.getLogger(AiServiceClient.class);

    private final RestTemplate restTemplate;

    @Value("${ai.service.url:http://localhost:5000}")
    private String aiServiceUrl;

    public AiServiceClient(RestTemplateBuilder builder) {
        this.restTemplate = builder
                .connectTimeout(Duration.ofSeconds(10))
                .readTimeout(Duration.ofSeconds(10))
                .build();
    }

    private HttpEntity<Map<String, String>> buildRequest(String text) {
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        return new HttpEntity<>(Map.of("text", text), headers);
    }

    public String describe(String text) {
        try {
            logger.info("Calling AI /describe endpoint");
            ResponseEntity<Map> response = restTemplate.postForEntity(
                aiServiceUrl + "/describe",
                buildRequest(text),
                Map.class
            );
            if (response.getBody() != null) {
                return (String) response.getBody().get("description");
            }
        } catch (Exception e) {
            logger.error("AI /describe call failed: {}", e.getMessage());
        }
        return null;
    }

    public String recommend(String text) {
        try {
            logger.info("Calling AI /recommend endpoint");
            ResponseEntity<Map> response = restTemplate.postForEntity(
                aiServiceUrl + "/recommend",
                buildRequest(text),
                Map.class
            );
            if (response.getBody() != null) {
                return (String) response.getBody().get("recommendations");
            }
        } catch (Exception e) {
            logger.error("AI /recommend call failed: {}", e.getMessage());
        }
        return null;
    }

    public String generateReport(String text) {
        try {
            logger.info("Calling AI /generate-report endpoint");
            ResponseEntity<Map> response = restTemplate.postForEntity(
                aiServiceUrl + "/generate-report",
                buildRequest(text),
                Map.class
            );
            if (response.getBody() != null) {
                return (String) response.getBody().get("report");
            }
        } catch (Exception e) {
            logger.error("AI /generate-report call failed: {}", e.getMessage());
        }
        return null;
    }
}