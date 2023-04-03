import os
import sys
import psutil


print("Welcome to Interapi")
print("CPU usage: ",  psutil.cpu_times())

# todo get cpu, disk, memory, network usage
# todo post to the specified API endpoint


def get_sys_config():
    print(f"System: {sys.platform} ")


def get_cpu_percent(user_range, user_interval):
    for i in range(user_range):
        print(psutil.cpu_percent(interval=user_interval))


print(get_cpu_percent(5, 1))
