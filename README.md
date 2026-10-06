# Monitor a Spark Job with Prometheus & Grafana

## Layout
```
configs.py                        enables Spark's Prometheus metrics
prometheus.yml                    scrape config for Spark driver + executor metrics
docker-compose.yml                Prometheus (:9090) + Grafana (:3000)
```

## 1. Start Prometheus and Grafana
```
docker compose up -d
```
Grafana: http://localhost:3000 (admin / admin). The Prometheus data source and the
If you run Prometheus without Docker, change the targets in `prometheus.yml`
from `host.docker.internal:4040` to `localhost:4040`.



## 2. Verify Prometheus receives Spark metrics
- While the job is running, open http://localhost:4040/metrics/prometheus/ and
  http://localhost:4040/metrics/executors/prometheus/ - both should return metrics.
- Prometheus -> Status -> Targets: `spark-driver` and `spark-executors` should be **UP**.
- Query `metrics_spark_driver_DAGScheduler_job_allJobs_Value` in the Prometheus UI.

