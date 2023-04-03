import sys
import psutil


print("Welcome to Interapi")
print("CPU usage: ",  psutil.cpu_times())


def get_cpu_percent(user_range, user_interval):
    for i in range(user_range):
        print(psutil.cpu_percent(interval=user_interval))
        
        
print(get_cpu_percent(5,1))