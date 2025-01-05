from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')

topic = 'test-topic'
message = b'Hello Kafka!'
producer.send(topic, message)

producer.close()
print("Message sent to Kafka.")
