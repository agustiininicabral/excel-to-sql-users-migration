# Migration design

1. Read the `Users` worksheet while preserving phone values as text.
2. Fail fast if required columns are missing.
3. Normalize names, email, phone, status, and dates.
4. Validate each row and preserve explicit rejection reasons.
5. Deduplicate valid rows by normalized email; first valid row wins.
6. Export accepted and rejected CSV reports.
7. In non-dry-run mode, insert accepted rows in one MySQL transaction.
8. Commit only after all statements succeed; rollback and re-raise on failure.

## Idempotency
The loader uses MySQL upsert behavior with unique constraints on source ID and email. Re-running the same sample does not create duplicate destination records.

## Production considerations
A real migration needs a data-owner-approved duplicate survivorship rule, source snapshot, backups, row-count reconciliation, structured logs, secret management, and a tested rollback plan. Those controls are deliberately out of scope for this learning exercise.
