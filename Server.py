import psutil
import time

def get_system_info():
    # Get CPU information
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()

    # Get memory information
    memory = psutil.virtual_memory()
    memory_total = memory.total
    memory_used = memory.used
    memory_percent = memory.percent

    # Get disk information
    disk = psutil.disk_usage('/')
    disk_total = disk.total
    disk_used = disk.used
    disk_percent = disk.percent

    # Get network information
    network = psutil.net_io_counters()
    bytes_sent = network.bytes_sent
    bytes_received = network.bytes_recv

    return {
        "CPU Usage": cpu_percent,
        "CPU Cores": cpu_count,
        "Memory Total (bytes)": memory_total,
        "Memory Used (bytes)": memory_used,
        "Memory Usage (%)": memory_percent,
        "Disk Total (bytes)": disk_total,
        "Disk Used (bytes)": disk_used,
        "Disk Usage (%)": disk_percent,
        "Bytes Sent": bytes_sent,
        "Bytes Received": bytes_received
    }

if __name__ == "__main__":
    while True:
        system_info = get_system_info()
        for key, value in system_info.items():
            print(f"{key}: {value}")
        print("=" * 30)
        time.sleep(5)  # Print system information every 5 seconds
