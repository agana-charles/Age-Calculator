import psutil
import time
from datetime import datetime
from plyer import notification

# Thresholds
CPU_THRESHOLD = 80
MEM_THRESHOLD = 90
DISK_THRESHOLD = 90

# Log file
LOG_FILE = "system_log.txt"

def log_message(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    message = f"CPU: {cpu}%, Memory: {mem}%, Disk: {disk}%"
    log_message(message)

    if cpu > CPU_THRESHOLD:
        notify(f"High CPU Usage: {cpu}%")
    if mem > MEM_THRESHOLD:
        notify(f"High Memory Usage: {mem}%")
    if disk > DISK_THRESHOLD:
        notify(f"Low Disk Space: {disk}% used")

def notify(message):
    notification.notify(
        title="System Health Alert",
        message=message,
        timeout=5
    )

if __name__ == "__main__":
    print("Monitoring started. Press Ctrl+C to stop.")
    try:
        while True:
            check_system_health()
            time.sleep(60)  # check every 60 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")
