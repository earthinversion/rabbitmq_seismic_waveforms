import pika
import json

# Establish connection
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        credentials=pika.PlainCredentials(username='admin', password='admin123')
    )
)
channel = connection.channel()

# Declare the same queue
channel.queue_declare(queue='seismic_waveforms')

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"Received: {data}")

# Consume messages
channel.basic_consume(queue='seismic_waveforms', on_message_callback=callback, auto_ack=True)

print('Waiting for seismic waveforms...')
channel.start_consuming()
