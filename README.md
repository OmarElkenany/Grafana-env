# Monitor a Spark Job with Prometheus & Grafana

## Layout
```
configs.py            copy-paste code: enables Spark's Prometheus metrics
prometheus.yml   scrape config for Spark driver + executor metrics
docker-compose.yml    Spark (:4040), Prometheus (:9090), Grafana (:3000)
```

## 1. Start the services
```
docker compose up -d prometheus grafana
docker compose up spark
```
The job stays alive for 5 minutes at the end so Prometheus can scrape it.
Run `docker compose up spark` again to re-run it.

Without Docker: run `spark-submit spark_job.py` and change the targets in
`prometheus/prometheus.yml` from `spark:4040` to `localhost:4040`.

## 2. Verify Prometheus receives Spark metrics
* While the job is running, open http://localhost:4040/metrics/prometheus/ and
  http://localhost:4040/metrics/executors/prometheus/ - both should return metrics.
* Prometheus (http://localhost:9090) -> Status -> Targets: `spark-driver` and
  `spark-executors` should be UP.
* Query `metrics_spark_driver_DAGScheduler_job_allJobs_Value` in the Prometheus UI.

## 3. Grafana
Open http://localhost:3000 (admin / admin), add Prometheus as a data source
with URL `http://prometheus:9090`
