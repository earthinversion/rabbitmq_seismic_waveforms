import asyncio
import json
from aio_pika import connect, IncomingMessage

QUEUE_NAME = "seismic_waveforms"

# Asynchronous processing of a message
async def process_message(message: IncomingMessage):
    async with message.process():  # Automatically acknowledges message
        data = json.loads(message.body)
        print(f"Received: {data}")
        await asyncio.sleep(0.5)  # Simulate message processing time

# Asynchronous consuming function
async def consume_waveforms():
    # Connect to RabbitMQ
    connection = await connect("amqp://admin:admin123@localhost/")
    async with connection:
        channel = await connection.channel()

        # Declare a durable queue
        queue = await channel.declare_queue(QUEUE_NAME, durable=True)

        print("Waiting for messages...")
        await queue.consume(process_message)  # Start consuming messages

        # Keep the connection open
        await asyncio.Future()

# Main event loop
if __name__ == "__main__":
    asyncio.run(consume_waveforms())
