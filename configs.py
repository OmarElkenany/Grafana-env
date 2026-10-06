from pyspark.sql import SparkSession, functions as F

# Spark session + Prometheus metrics (http://localhost:4040/metrics/prometheus/)
spark = (
    SparkSession.builder.appName("spark_job")
    .config("spark.ui.prometheus.enabled", "true")
    .config("spark.metrics.namespace", "spark")
    .config("spark.metrics.conf.*.sink.prometheusServlet.class",
            "org.apache.spark.metrics.sink.PrometheusServlet")
    .config("spark.metrics.conf.*.sink.prometheusServlet.path", "/metrics/prometheus")
    .getOrCreate()
)