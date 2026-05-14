import json
import random
import time
from datetime import datetime

from faker import Faker
from kafka import KafkaProducer

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers='localhost:9096',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

EVENT_TYPES = [
    'page_view',
    'add_to_cart',
    'purchase',
    'refund',
    'login'
]

PRODUCT_CATEGORIES = [
    'electronics',
    'fashion',
    'books',
    'gaming',
    'home'
]


def generate_event():
    return {
        'event_id': fake.uuid4(),
        'user_id': random.randint(1000, 5000),
        'event_type': random.choice(EVENT_TYPES),
        'product_category': random.choice(PRODUCT_CATEGORIES),
        'amount': round(random.uniform(100, 5000), 2),
        'city': fake.city(),
        'event_timestamp': datetime.utcnow().isoformat()
    }

if __name__ == '__main__':
    while True:
        event = generate_event()

        producer.send('ecommerce-events', event)

        print(f'Produced Event: {event}')

        time.sleep(2)