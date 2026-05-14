import json

from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'ecommerce-events',
    bootstrap_servers='localhost:9096',
    auto_offset_reset='earliest',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

print('Listening for events...')

for message in consumer:
    print(message.value)