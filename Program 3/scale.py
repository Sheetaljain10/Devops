import subprocess

def scale_deployment(replica_count):
    command = f"kubectl scale deployment flask-deployment --replicas={replica_count}"
    subprocess.run(command, shell=True)

# Example: Scale to 3 replicas
scale_deployment(3)
