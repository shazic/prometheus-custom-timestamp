from custom_timestamp_collector import CustomTimestampCollector
from prometheus_client import make_wsgi_app, REGISTRY
from wsgiref.simple_server import make_server

data_source_url = "http://localhost:9091/metrics"
collector = CustomTimestampCollector(data_source_url)
REGISTRY.register(collector)

def start_exporter():
    app = make_wsgi_app(REGISTRY)
    httpd = make_server('', 9091, app)
    print("Custom exporter running on port 9091...")
    httpd.serve_forever()

if __name__ == "__main__":
    start_exporter()
