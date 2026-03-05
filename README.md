# Marketing Supermodel

This repository includes:

- `seeds/sales_partner_renewal_customers.csv` with Sales-partner-renewal customer fields.
- `models/supermodels/supermodel_customer_upgrade_leads.sql` that calculates a per-customer `lead_score` (10 or under).
- `models/supermodels/qualified_leads_for_upgrade.sql` that returns only customers where `lead_score = 10`.
- `scripts/build_model_output.py` to generate JSON model outputs for the web UI.
- `model_output/supermodel_customer_upgrade_leads.json` and `model_output/qualified_leads_for_upgrade.json` used by the webpage.
- `web/index.html` that displays customer records and includes a **Show qualified leads for upgrade** button.

## Generate web model output

```bash
python scripts/build_model_output.py
```

## Run the webpage
Serve the repository root so `/model_output/...` endpoints resolve:

```bash
python -m http.server 8765 --bind 0.0.0.0 --directory /workspace/Marketing
```

Then open:

- `http://127.0.0.1:8765/web/index.html`

## Qualified leads SQL logic

```sql
select *
from {{ ref('qualified_leads_for_upgrade') }}
```
