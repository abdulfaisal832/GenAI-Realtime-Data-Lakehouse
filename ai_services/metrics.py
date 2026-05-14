import time

# In-memory metrics (simple but interview-friendly)

METRICS = {
    "request_count": 0,
    "last_latency": 0,
    "last_status": "unknown"
}


def record_request(start_time, status="success"):
    METRICS["request_count"] += 1
    METRICS["last_latency"] = round(time.time() - start_time, 4)
    METRICS["last_status"] = status


def get_metrics():
    return METRICS