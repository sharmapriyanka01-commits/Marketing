import csv
import json
from pathlib import Path

seed_path = Path('seeds/sales_partner_renewal_customers.csv')
all_output_path = Path('model_output/supermodel_customer_upgrade_leads.json')
qualified_output_path = Path('model_output/qualified_leads_for_upgrade.json')

rows = list(csv.DictReader(seed_path.open()))


def calculate_lead_score(row):
    web_interaction = int(row['web_interaction'])
    email_opened = int(row['email_opened'])
    white_paper_downloaded = int(row['white_paper_downloaded'])
    new_employees_added = int(row['new_employees_added'])

    web_points = 4 if web_interaction >= 30 else 3 if web_interaction >= 20 else 2 if web_interaction >= 10 else 1
    email_points = 2 if email_opened == 1 else 0
    white_paper_points = 2 if white_paper_downloaded == 1 else 0
    employee_points = 2 if new_employees_added >= 15 else 1 if new_employees_added >= 10 else 0

    return min(10, web_points + email_points + white_paper_points + employee_points)


scored_rows = []
for row in rows:
    lead_score = calculate_lead_score(row)
    scored_rows.append(
        {
            'customer_name': row['customer_name'],
            'web_interaction': int(row['web_interaction']),
            'email_opened': int(row['email_opened']),
            'white_paper_downloaded': int(row['white_paper_downloaded']),
            'new_employees_added': int(row['new_employees_added']),
            'lead_score': lead_score,
            'lead_label': 'qualified lead for upgrade' if lead_score == 10 else 'not qualified',
        }
    )

qualified_rows = [row for row in scored_rows if row['lead_score'] == 10]

all_output_path.write_text(json.dumps(scored_rows, indent=2) + '\n')
qualified_output_path.write_text(json.dumps(qualified_rows, indent=2) + '\n')

print(f'wrote {all_output_path} ({len(scored_rows)} rows)')
print(f'wrote {qualified_output_path} ({len(qualified_rows)} rows)')
