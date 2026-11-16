USE excel_migration;
SELECT COUNT(*) AS total_users FROM users;
-- Must return no rows.
SELECT email, COUNT(*) AS occurrences FROM users GROUP BY email HAVING COUNT(*) > 1;
-- Must return zero.
SELECT COUNT(*) AS invalid_required_values FROM users
WHERE first_name='' OR last_name='' OR email='' OR created_at IS NULL
 OR status NOT IN ('active','inactive','pending');
SELECT status, COUNT(*) AS users_count FROM users GROUP BY status ORDER BY status;
SELECT MIN(created_at) AS first_user_date, MAX(created_at) AS last_user_date FROM users;
