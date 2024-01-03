from confluent_kafka import Consumer
from yuptoo.lib.config import (
        KAFKA_AUTO_COMMIT,
        BOOTSTRAP_SERVERS,
        ANNOUNCE_TOPIC,
        KAFKA_CONSUMER_GROUP_ID,
        kafka_auth_config
    )


def init_consumer():
    connection_object = {
        'bootstrap.servers': ",".join(BOOTSTRAP_SERVERS),
        'group.id': KAFKA_CONSUMER_GROUP_ID,
        'enable.auto.commit': KAFKA_AUTO_COMMIT
    }
    kafka_auth_config(connection_object)
    consumer = Consumer(connection_object)
    consumer.subscribe([ANNOUNCE_TOPIC])

    return consumer
