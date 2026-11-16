CREATE DATABASE IF NOT EXISTS excel_migration CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE excel_migration;
CREATE TABLE IF NOT EXISTS users (
 user_id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
 source_id BIGINT UNSIGNED NOT NULL,
 first_name VARCHAR(100) NOT NULL,
 last_name VARCHAR(100) NOT NULL,
 email VARCHAR(254) NOT NULL,
 phone VARCHAR(40) NULL,
 created_at DATE NOT NULL,
 status VARCHAR(20) NOT NULL,
 migrated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
 PRIMARY KEY (user_id),
 CONSTRAINT uq_users_source_id UNIQUE (source_id),
 CONSTRAINT uq_users_email UNIQUE (email),
 CONSTRAINT chk_users_status CHECK (status IN ('active','inactive','pending')),
 INDEX idx_users_status (status),
 INDEX idx_users_created_at (created_at)
) ENGINE=InnoDB;
