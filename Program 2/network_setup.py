import docker

client = docker.from_env()

# Create custom bridge network
network_name = "custom_bridge"
network = client.networks.create(network_name, driver="bridge")
print(f"Network '{network_name}' created.")

# Run application container
app_container = client.containers.run(
    "python_web_app", detach=True, name="app_container", network=network_name
)
print(f"App container '{app_container.name}' started.")

# Run SQLite database container (stand-in container for demonstration)
db_container = client.containers.run(
    "busybox", "sh -c 'sleep 3600'", detach=True, name="db_container", network=network_name
)
print(f"Database container '{db_container.name}' started.")

# Inspect network
network_info = network.attrs
print(f"Network Info: {network_info}")

# List connected containers
print("Connected Containers:", network_info["Containers"].keys())

# Clean up
input("Press Enter to clean up and remove containers and network...")
app_container.stop()
db_container.stop()
app_container.remove()
db_container.remove()
network.remove()
print("Cleanup completed.")
