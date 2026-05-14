import logging
import json

logging.basicConfig(level=logging.INFO)

def log_event(event, data=None):
    log = {
        "event": event,
        "data": data
    }
    logging.info(json.dumps(log))