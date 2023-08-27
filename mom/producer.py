import pika
from config import RABBITMQ_HOST, QUEUE_NAME


def send_message(message_body):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    channel.basic_publish(
        exchange='', routing_key=QUEUE_NAME, body=message_body)
    print(f" [x] Sent '{message_body}'")

    connection.close()


if __name__ == "__main__":
    send_message("Hello World!")
