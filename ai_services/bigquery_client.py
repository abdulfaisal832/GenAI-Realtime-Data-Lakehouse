from google.cloud import bigquery


def fetch_sales_metrics():

    client = bigquery.Client()

    query = """
SELECT
    SUM(total_amount) AS revenue,
    COUNT(order_id) AS total_orders,
    AVG(total_amount) AS avg_order_value
FROM `genai-realtime-data-lakehouse.ecommerce_analytics.gold_sales_metrics`
"""

    query_job = client.query(query)

    results = query_job.result()

    for row in results:
        return {
            "revenue": row.revenue,
            "total_orders": row.total_orders,
            "avg_order_value": row.avg_order_value
        }