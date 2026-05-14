from google.cloud import bigquery
from datetime import datetime

client = bigquery.Client()

TABLE_ID = "genai-realtime-data-lakehouse.ecommerce_analytics.ai_insights"


def save_insight(metrics_data, insight):

    rows = [{
        "timestamp": datetime.utcnow(),
        "revenue": metrics_data["revenue"],
        "total_orders": metrics_data["total_orders"],
        "avg_order_value": metrics_data["avg_order_value"],
        "insight": insight
    }]

    errors = client.insert_rows_json(TABLE_ID, rows)

    if errors:
        print("BigQuery Insert Error:", errors)
    else:
        print("Insight saved successfully")