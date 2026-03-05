-- Returns only customers qualified for upgrade.

select
    customer_name,
    web_interaction,
    email_opened,
    white_paper_downloaded,
    new_employees_added,
    lead_score,
    lead_label
from {{ ref('supermodel_customer_upgrade_leads') }}
where lead_score = 10
