import pika
import json
import time
import random

# Establish connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.PlainCredentials(username='admin', password='admin123')
    )
)

channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='seismic_waveforms')

# Simulate sending seismic waveform data
def generate_waveform_data():
    return {
        "station": f"station_{random.randint(1, 100)}",
        "timestamp": time.time(),
        "waveform": [random.uniform(-1, 1) for _ in range(100)]  # Simulated waveform
    }

while True:
    data = generate_waveform_data()
    channel.basic_publish(
        exchange='',
        routing_key='seismic_waveforms',
        body=json.dumps(data)
    )
    print(f"Sent: {data}")
    time.sleep(1)  # Simulate real-time streaming

connection.close()