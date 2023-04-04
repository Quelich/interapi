''' InterAPI - A simple API for system monitoring '''
import cpu_usage as intercpu
import json
from fastapi import FastAPI

# todo get cpu, disk, memory, network usage
# todo post to the specified API endpoint
# JSON format: {system: "linux", cpu: {usage}}


# Initialize FastAPI

app = FastAPI()

# ENDPOINTS


@app.get("/")
async def root():

    return {"message": "Welcome to InterAPI"}


@app.get("/cpu-metrics")
async def cpu_metrics():
    cpu_dict = intercpu.get_cpu_percent(5, 1)
    cpu_json = json.dumps(cpu_dict) # todo stringfy
    return {"data": cpu_json, "status": "success"}
