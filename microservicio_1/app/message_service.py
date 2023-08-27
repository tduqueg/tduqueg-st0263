# message_service.py
import pika


def publish_message(routing_key, message):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

    channel.basic_publish(exchange='topic_logs',
                          routing_key=routing_key, body=message)
    print(f" [x] Sent {routing_key}:{message}")
    connection.close()
