from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    group_id='test-group'
)

# Get consumer lag and other metrics
print("Consumer Metrics:")
for topic_partition, offsets in consumer.metrics().items():
    print(topic_partition, offsets)
