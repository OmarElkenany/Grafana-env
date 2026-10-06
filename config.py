import time
from pyspark.sql import SparkSession

# Spark session with Prometheus metrics
#   http://localhost:4040/metrics/prometheus/
#   http://localhost:4040/metrics/executors/prometheus/
spark = (
    SparkSession.builder.appName("spark_job")
    .config("spark.ui.prometheus.enabled", "true")
    .config("spark.metrics.namespace", "spark")
    .config("spark.metrics.conf.*.sink.prometheusServlet.class",
            "org.apache.spark.metrics.sink.PrometheusServlet")
    .config("spark.metrics.conf.*.sink.prometheusServlet.path", "/metrics/prometheus")
    .getOrCreate()
)







time.sleep(300)  
spark.stop()
