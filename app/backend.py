"""
FastApi based application template
"""
from fastapi import FastAPI
import psutil
import sys
import os
sys.path.insert(0, os.path.abspath('..'))
import libs.memory as mem
import time


app = FastAPI(title='#template#', version="0.2")


@app.get("/")
def root():
    return {
        "Project": "#template#",
        "API Specs": "/docs",
    }


@app.get("/health")
def health():

    def pretty(value, divider=1024 * 1024):
        return round(value / divider, 0)

    process = psutil.Process()
    workers = process.parent().children(recursive=True)
    parent_uptime = round(time.time() - process.parent().create_time(), 1)
    workers_count = len(workers)
    workers_data = dict()
    uptime_diff = 0
    for worker in workers:
        worker_uptime = round(time.time() - worker.create_time(), 1)
        workers_data[worker.pid] = {
            'name': worker.name(),
            'uptime': worker_uptime,
            'rss': pretty(worker.memory_info().rss)
        }

        if parent_uptime - worker_uptime > 0.5:
            uptime_diff = parent_uptime - worker_uptime

    memory_max_usage = pretty(mem.get_max_memory_usage())
    memory_usage = pretty(mem.get_memory_usage())
    memory_limit = pretty(mem.get_memory_limit())

    message = ['I am fine']
    if memory_limit > 0 and (memory_usage / memory_limit) > 0.8:
        message.append('Memory usage looks high')
    if uptime_diff > 0:
        message.append('Workers are lagging, compare uptimes')

    data = {
        "message": message,
        "info": "data sizes are in megabytes, timings are in seconds",
        'memory_max_usage': memory_max_usage,
        'memory_usage': memory_usage,
        'memory_limit': memory_limit,
        'workers_count': workers_count,
        'workers_data': workers_data,
        'parent': process.parent().name(),
        'parent_uptime': parent_uptime,
        'parent_rss': pretty(process.parent().memory_info().rss),
    }
    return data


@app.on_event("shutdown")
def shutdown_event():
    pass
