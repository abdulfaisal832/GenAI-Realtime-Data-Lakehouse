import os
from dotenv import load_dotenv

load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# BigQuery
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID", "genai-realtime-data-lakehouse")
BQ_DATASET = os.getenv("BQ_DATASET", "ecommerce_analytics")
BQ_TABLE = os.getenv("BQ_TABLE", "gold_sales_metrics")

# Kafka
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")

# Airflow
AIRFLOW_ENV = os.getenv("AIRFLOW_ENV", "local")