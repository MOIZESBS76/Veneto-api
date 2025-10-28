# consome mensagens e printa
import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_QUEUE = os.getenv("RABBITMQ_QUEUE", "mensagens")

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f"[✔] Mensagem recebida: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

def consume():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)
    print("[*] Aguardando mensagens...")
    channel.start_consuming()

if __name__ == "__main__":
    consume()
