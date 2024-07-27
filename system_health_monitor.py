import psutil
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='system_health.log', level=logging.INFO, format='%(asctime)s - %(message)s')

# Thresholds
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 80.0  # in percentage
PROCESS_COUNT_THRESHOLD = 300  # arbitrary process count threshold

def check_cpu_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage detected: {cpu_usage}%')
    return cpu_usage

def check_memory_usage():
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage detected: {memory_usage}%')
    return memory_usage

def check_disk_space():
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        logging.warning(f'Low Disk space detected: {disk_usage}% used')
    return disk_usage

def check_running_processes():
    process_count = len(psutil.pids())
    if process_count > PROCESS_COUNT_THRESHOLD:
        logging.warning(f'High number of processes running: {process_count}')
    return process_count

def log_system_health():
    cpu = check_cpu_usage()
    memory = check_memory_usage()
    disk = check_disk_space()
    processes = check_running_processes()

    logging.info(f'System Health - CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%, Processes: {processes}')

if __name__ == '__main__':
    log_system_health()
