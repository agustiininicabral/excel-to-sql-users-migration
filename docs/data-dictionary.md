# Data dictionary

## Source worksheet: Users

| Column | Target | Rule |
|---|---|---|
| source_id | BIGINT UNSIGNED | Required unique source identifier |
| first_name | VARCHAR(100) | Trim; reject if blank |
| last_name | VARCHAR(100) | Trim; reject if blank |
| email | VARCHAR(254) | Trim, lowercase, validate, unique |
| phone | VARCHAR(40) NULL | Trim; blank becomes NULL |
| created_at | DATE | Parse supported formats; reject invalid |
| status | VARCHAR(20) | Lowercase; active/inactive/pending only |

Destination adds auto-increment `user_id` and database-managed `migrated_at`. Unique constraints protect both source ID and normalized email.
