import docker

client = docker.from_env()

def check_health():
    for container in client.containers.list():
        print(f"Checking health for container: {container.name}")
        logs = container.logs().decode('utf-8')
        print(f"Logs:\n{logs}")

if __name__ == "__main__":
    check_health()
