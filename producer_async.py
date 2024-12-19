import asyncio
import json
import random
import time
from aio_pika import connect, Message, DeliveryMode

QUEUE_NAME = "seismic_waveforms"

# Generate waveform data
def generate_waveform_data():
    return {
        "station": f"station_{random.randint(1, 100)}",
        "timestamp": time.time(),
        "waveform": [random.uniform(-1, 1) for _ in range(100)]  # Simulated waveform
    }

# Asynchronous publishing function
async def publish_waveforms():
    # Connect to RabbitMQ
    connection = await connect(
        "amqp://admin:admin123@localhost/"
    )
    async with connection:
        channel = await connection.channel()

        # Declare a queue
        await channel.declare_queue(QUEUE_NAME, durable=True)

        while True:
            # Generate and send waveform data
            data = generate_waveform_data()
            message = Message(
                json.dumps(data).encode(),
                delivery_mode=DeliveryMode.PERSISTENT  # Ensure message persistence
            )
            await channel.default_exchange.publish(message, routing_key=QUEUE_NAME)
            print(f"Sent: {data}")
            await asyncio.sleep(1)  # Simulate real-time streaming

# Main event loop
if __name__ == "__main__":
    asyncio.run(publish_waveforms())
