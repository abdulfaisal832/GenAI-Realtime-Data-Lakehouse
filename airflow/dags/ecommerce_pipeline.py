from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {
    "owner": "abdul",
    "depends_on_past": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=1)
}


def validate_kafka():
    print("Kafka validation successful")


def bronze_pipeline():
    print("Bronze pipeline completed")


def silver_pipeline():
    print("Silver pipeline completed")


def gold_pipeline():
    print("Gold metrics pipeline completed")


with DAG(
    dag_id="ecommerce_realtime_pipeline",
    default_args=default_args,
    description="Real-time GenAI Lakehouse Pipeline",
    schedule="@hourly",
    start_date=datetime(2026, 5, 1),
    catchup=False
) as dag:


    bronze_task = BashOperator(
    task_id="bronze_layer_pipeline",
    bash_command="python3 /opt/airflow/dags/scripts/bronze_job.py"
)

    silver_task = BashOperator(
    task_id="silver_layer_pipeline",
    bash_command="python3 /opt/airflow/dags/scripts/silver_job.py"
)

    gold_task = BashOperator(
    task_id="gold_layer_pipeline",
    bash_command="python3 /opt/airflow/dags/scripts/gold_job.py"
)
    
    bigquery_task = BashOperator(
    task_id="bigquery_load",
    bash_command="python3 /opt/airflow/dags/scripts/bigquery_load.py"
)

    (
    bronze_task
    >> silver_task
    >> gold_task
    >> bigquery_task
)