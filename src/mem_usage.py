import psutil

def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem
