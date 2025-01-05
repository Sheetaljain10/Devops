import docker

client = docker.from_env()

# Build the Docker image
client.images.build(path=".", tag="flask-app")

# Run the Docker container
container = client.containers.run("flask-app", ports={"5000/tcp": 5000}, detach=True)
print(f"Container started with ID: {container.id}")
