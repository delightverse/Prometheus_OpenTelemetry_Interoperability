#!/usr/bin/env python3

from fastapi import FastAPI
from prometheus_client import Histogram, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
import random, time


app = FastAPI()


REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request latency',
    ['endpoint']
)

@app.get("/simulate")
def simulate():
    start = time.time()
    delay = random.uniform(0.05, 0.3)
    time.sleep(delay)
    REQUEST_LATENCY.labels(endpoint='/simulate').observe(time.time() - start)
    return {"status": "ok", "latency": delay}


@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
