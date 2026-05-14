GenAI Real-Time Data Lakehouse (End-to-End Data Engineering + AI System)

Overview

This project is a **real-time data engineering + AI-powered analytics system** built using modern data stack tools.

It simulates an end-to-end **e-commerce analytics platform** that:
- Ingests streaming data using Kafka
- Processes data using Spark (Medallion Architecture)
- Orchestrates pipelines using Airflow
- Stores data in BigQuery (Lakehouse layer)
- Generates AI-powered business insights using OpenAI
- Exposes results via FastAPI

---

##  Architecture

Kafka → Spark → BigQuery → Airflow → FastAPI → OpenAI → Insights API


---

## ⚙️ Tech Stack

- Python
- Apache Kafka
- Apache Spark / PySpark
- Apache Airflow
- Google BigQuery
- FastAPI
- OpenAI API
- Docker

---

##  Features

###  Data Engineering
- Real-time streaming ingestion using Kafka
- ETL pipelines using Spark (Bronze / Silver / Gold layers)
- Data orchestration using Airflow DAGs

###  AI Layer
- Generates business insights using OpenAI
- Converts raw metrics into actionable insights

###  Observability
- Health check endpoint (`/health`)
- Metrics endpoint (`/metrics`)
- System monitoring for Kafka, BigQuery, Airflow

###  Storage Layer
- BigQuery used as cloud data warehouse
- AI insights stored for historical analysis

---

## How to Run This Project

### Clone the repository

```bash
git clone https://github.com/your-username/GenAI-Realtime-Data-Lakehouse.git
cd GenAI-Realtime-Data-Lakehouse

Create virtual environment
python3 -m venv venv
source venv/bin/activate

Install dependencies
pip install -r requirements.txt

Set environment variables

Create .env file:

OPENAI_API_KEY=your_key
GCP_PROJECT_ID=your_project
KAFKA_BROKER=localhost:9092

Start Airflow (Docker)
docker-compose up -d

Run FastAPI service
uvicorn ai_services.app:app --reload

Key Learning Outcomes:
Real-time data pipeline design
Medallion architecture implementation
AI integration in data engineering workflows
Distributed system orchestration using Airflow
Cloud warehouse integration (BigQuery)
Observability & system monitoring

Author

Abdul Faisal
Data Engineer (2+ years experience)






