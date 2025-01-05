from kafka.admin import KafkaAdminClient, NewTopic

admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")

# Create a new topic
topic = NewTopic(name="new-topic", num_partitions=3, replication_factor=1)
admin_client.create_topics(new_topics=[topic], validate_only=False)

print("Topic created successfully.")

# List existing topics
topics = admin_client.list_topics()
print("Existing Topics:", topics)

# Delete a topic
admin_client.delete_topics(topics=["new-topic"])
print("Topic deleted.")
