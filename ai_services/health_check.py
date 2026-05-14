from google.cloud import bigquery
from kafka import KafkaProducer
from ai_services.config import KAFKA_BROKER


def check_bigquery():
    try:
        client = bigquery.Client()
        query = "SELECT 1"
        client.query(query).result()
        return "healthy"
    except Exception as e:
        return f"unhealthy: {str(e)}"


def check_kafka():
    try:
        producer = KafkaProducer(
            bootstrap_servers=KAFKA_BROKER,
            request_timeout_ms=2000
        )
        producer.close()
        return "healthy"
    except Exception as e:
        return f"unhealthy: {str(e)}"


def check_airflow():
    try:
        import requests
        response = requests.get("http://localhost:8090/health")
        if response.status_code == 200:
            return "healthy"
        return "unhealthy"
    except Exception as e:
        return f"unhealthy: {str(e)}"


def system_health():
    return {
        "api": "healthy",
        "bigquery": check_bigquery(),
        "kafka": check_kafka(),
        "airflow": check_airflow()
    }