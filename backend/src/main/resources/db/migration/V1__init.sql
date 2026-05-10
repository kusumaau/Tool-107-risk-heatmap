CREATE TABLE risk_item (
    id BIGSERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    likelihood VARCHAR(50),
    impact VARCHAR(50),
    risk_score DOUBLE PRECISION,
    status VARCHAR(50) DEFAULT 'OPEN',
    category VARCHAR(100),
    affected_areas TEXT,
    ai_description TEXT,
    ai_recommendations TEXT,
    ai_report TEXT,
    is_fallback BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    deleted BOOLEAN DEFAULT FALSE
);

CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(100) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) DEFAULT 'USER',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE audit_log (
    id BIGSERIAL PRIMARY KEY,
    action VARCHAR(100),
    entity_type VARCHAR(100),
    entity_id BIGINT,
    performed_by VARCHAR(100),
    performed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    details TEXT
);

CREATE INDEX idx_risk_item_status ON risk_item(status);
CREATE INDEX idx_risk_item_category ON risk_item(category);
CREATE INDEX idx_audit_log_entity ON audit_log(entity_type, entity_id);