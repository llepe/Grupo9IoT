import psutil

print(psutil.cpu_percent())

print(psutil.disk_partitions())

print(psutil.disk_usage("D:\\"))
