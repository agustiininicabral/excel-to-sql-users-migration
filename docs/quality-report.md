# Data quality report

The workbook is synthetic and intentionally includes whitespace, mixed email casing, mixed date formats, a duplicate email, malformed email, missing names, an invalid date, and an unsupported status.

The pipeline classifies every source row as accepted or rejected and records pipe-delimited rejection reasons. The dry-run output is authoritative for counts; this document avoids hard-coded metrics that could become stale.

## Review checklist
- [ ] Accepted + rejected equals source row count.
- [ ] Accepted emails are lowercase and unique.
- [ ] Accepted rows have names, valid dates, and allowed statuses.
- [ ] Every rejected row has an explicit reason.
- [ ] MySQL row count reconciles with accepted rows after a clean load.
