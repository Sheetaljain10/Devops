from kubernetes import client, config

def monitor_pods():
    # Load kube config
    config.load_kube_config()

    # Connect to Kubernetes API
    v1 = client.CoreV1Api()

    # List all pods
    pods = v1.list_pod_for_all_namespaces(watch=True)
    for pod in pods.items:
        print(f"{pod.metadata.name} - {pod.status.phase}")

if __name__ == '__main__':
    monitor_pods()
