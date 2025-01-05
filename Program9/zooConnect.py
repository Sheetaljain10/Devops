from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

# Create a znode
zk.ensure_path("/kafka")

# Get data from the znode
data, stat = zk.get("/kafka")
print(f"Data: {data}, Version: {stat.version}")

zk.stop()
