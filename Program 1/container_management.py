import docker

client = docker.from_env()

def list_containers():
    print("Active Containers:")
    for container in client.containers.list():
        print(f"{container.name} - {container.status} - {container.id}")

def stop_container(container_id):
    container = client.containers.get(container_id)
    container.stop()
    print(f"Stopped container: {container_id}")

def start_container(container_id):
    container = client.containers.get(container_id)
    container.start()
    print(f"Started container: {container_id}")

if __name__ == "__main__":
    list_containers()
    # Example: Stop a container
    stop_container("695519bed280b7fe2393acc1162b02096db461670a5105d802e478ce3d8d09d4")
    # Example: Start a container
    # start_container("5929446ec1ebc5cd37a3df6f5228eb1b271c04b6776a12d9fb4b38ebd472e41d")
