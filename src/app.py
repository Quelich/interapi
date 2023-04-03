import os
import sys

print("-------------------")
print("Welcome to Interapi")
print("-------------------")
print("CPU usage: ",)


# todo get cpu, disk, memory, network usage
# todo post to the specified API endpoint


# JSON format: {system: "linux", cpu: {usage}}

def get_sys_config():
    print(f"System: {sys.platform} ")
