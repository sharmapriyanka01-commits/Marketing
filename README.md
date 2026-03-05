# Marketing Supermodel

This repository includes:

- `seeds/sales_partner_renewal_customers.csv` with Sales-partner-renewal customer fields:
  - Customer name
  - Web interaction
  - Email opened
  - White paper downloaded
  - New employees added
- `models/supermodels/supermodel_customer_upgrade_leads.sql` that calculates a per-customer `lead_score` (10 or under) from interaction behavior and growth signals.
- `models/supermodels/qualified_leads_for_upgrade.sql` that returns only customers where `lead_score = 10`.
- `web/index.html` that displays customer records and includes a **Show qualified leads for upgrade** button to filter to customers with `lead_score = 10`.

## Qualified leads logic
When users ask to show **qualified leads for upgrade** in SQL, use:

```sql
select *
from {{ ref('qualified_leads_for_upgrade') }}
```
