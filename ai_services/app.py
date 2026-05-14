from fastapi import FastAPI
from openai import OpenAI
from dotenv import load_dotenv
import os
import time

from ai_services.metrics import record_request, get_metrics
from ai_services.prompt_templates import BUSINESS_INSIGHT_PROMPT
from ai_services.bigquery_client import fetch_sales_metrics
from ai_services.health_check import system_health
from ai_services.bigquery_writer import save_insight
from ai_services.logger import log_event

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.get("/metrics")
def metrics():
    return get_metrics()

@app.get("/health")
def health_check():
    return system_health()

@app.get("/")
def home():
    return {
        "message": "GenAI Realtime Data Lakehouse API is Running"
    }


@app.get("/generate-insights")
def generate_insights():

    start = time.time()

    try:
        metrics_data = fetch_sales_metrics()

        metrics = f"""
        Revenue: {metrics_data['revenue']}
        Total Orders: {metrics_data['total_orders']}
        Avg Order Value: {metrics_data['avg_order_value']}
        """

        prompt = BUSINESS_INSIGHT_PROMPT.format(metrics=metrics)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content

        record_request(start, "success")

        return {
            "metrics": metrics_data,
            "insights": result
        }

    except Exception as e:

        record_request(start, "failed")

        return {"error": str(e)}

        insights = """
        AI Service Fallback Response

        Revenue trends appear healthy.
        Customer order volume is increasing.
        Average order value indicates strong premium sales.

        Recommendation:
        Focus on high-performing product categories and optimize inventory planning.
        """

    return {
        "metrics": metrics_data,
        "insights": insights
    }