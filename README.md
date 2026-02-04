# FastAPI + Prometheus + OTEL Collector Demo (Browser OTLP)

## Overview
This demo shows a FastAPI app exposing Prometheus histograms, which are scraped by Prometheus, transformed via OpenTelemetry Collector, and re-exposed for browser viewing as OTLP metrics. You can verify everything locally in your browser.

---

## Setup & Run

#### 1. **Clone or copy the project** locally so that the folder structure remains intact.

#### 2. **Run Docker Compose** to build and start all services:

```bash
docker-compose up --build
```

**This will start:**

  - FastAPI app: http://localhost:8000

  - Prometheus UI: http://localhost:9090

  - OTEL Collector Prometheus endpoint: http://localhost:9464/metrics

#### 3. Generate Metrics

 1. Open a new terminal and send some simulated requests to generate histogram metrics:

```bash
for i in {1..20}; do curl http://localhost:8000/simulate; done
```

2. Refresh /metrics endpoints in your browser to see the updated metrics:

  - FastAPI Prometheus metrics: http://localhost:8000/metrics

  - OTEL Collector converted OTLP metrics: http://localhost:9464/metrics

3. Optional: Open Prometheus UI (http://localhost:9090/targets
) to verify that the FastAPI app is being scraped successfully.

#### 4. Verification

- `/simulate` endpoint generates random request latencies.

- `/metrics` endpoints show Prometheus histograms.

- OTEL Collector transforms the Prometheus histogram into OTLP-style metrics and exposes them via its Prometheus endpoint.

- Everything can be checked directly in the browser, without reading console logs.

## Stop the Services

```bash
docker-compose down
```

This will stop and remove all containers while keeping your project files intact.
