# Data quality report

The committed synthetic workbook contains **32 source rows**. The cleaning rules produce **26 accepted rows and 6 rejected rows**.

| Rejection reason | Rows |
|---|---:|
| Duplicate normalized email | 1 |
| Malformed email | 1 |
| Missing last name | 1 |
| Missing first name | 1 |
| Invalid date | 1 |
| Unsupported status | 1 |

No row is silently discarded. Accepted and rejected outputs reconcile to the original 32 records. These figures describe only the deliberately constructed sample, not a real business dataset.

## Review checklist
- [x] Accepted + rejected equals source row count (26 + 6 = 32).
- [x] Accepted emails are lowercase and unique.
- [x] Accepted rows have names, valid dates, and allowed statuses.
- [x] Every rejected row has an explicit reason.
- [x] GitHub Actions loaded all 26 accepted rows into an ephemeral MySQL 8.0 instance and verified row count, normalized emails, required fields, and uniqueness.


## Database integration

The CI run executes the actual transactional loader against a disposable MySQL 8.0 service. It verifies 26 persisted users; no production database or personal data is used.
