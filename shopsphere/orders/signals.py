import pika
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order


@receiver(post_save, sender=Order)
def order_created(sender, instance, created, **kwargs):

    if created:

        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost')
        )

        channel = connection.channel()

        channel.queue_declare(queue='orders')

        message = f"Order {instance.id} created"

        channel.basic_publish(
            exchange='',
            routing_key='orders',
            body=message
        )

        connection.close()