-- Supermodel: calculate a per-customer lead score (10 or under)
-- from Sales-partner-renewal interaction fields.

with source_customers as (
    select
        customer_name,
        web_interaction,
        email_opened,
        white_paper_downloaded,
        new_employees_added
    from {{ ref('sales_partner_renewal_customers') }}
),

scored_customers as (
    select
        customer_name,
        web_interaction,
        email_opened,
        white_paper_downloaded,
        new_employees_added,
        least(
            10,
            (
                case
                    when web_interaction >= 30 then 4
                    when web_interaction >= 20 then 3
                    when web_interaction >= 10 then 2
                    else 1
                end
                + case when email_opened = 1 then 2 else 0 end
                + case when white_paper_downloaded = 1 then 2 else 0 end
                + case
                    when new_employees_added >= 15 then 2
                    when new_employees_added >= 10 then 1
                    else 0
                end
            )
        ) as lead_score
    from source_customers
)

select
    customer_name,
    web_interaction,
    email_opened,
    white_paper_downloaded,
    new_employees_added,
    lead_score,
    case
        when lead_score = 10 then 'qualified lead for upgrade'
        else 'not qualified'
    end as lead_label
from scored_customers
