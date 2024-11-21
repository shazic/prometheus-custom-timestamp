import requests
import random
import time
from prometheus_client.core import GaugeMetricFamily

class CustomTimestampCollector:
    def __init__(self, data_source_url):
        self.data_source_url = data_source_url

    def fetch_pipeline_data(self):
        """Fetch pipeline data from an external source."""
        # try:
        #     response = requests.get(self.data_source_url)
        #     response.raise_for_status()
        #     return response.json()  # Assuming the API returns JSON data
        # except requests.RequestException as e:
        #     print(f"Error fetching pipeline data: {e}")
        #     return []
        return [
            {"pipeline_name": "ci-pipeline", "branch_name": "main", "status": "SUCCESS", "lead_time_seconds": random.uniform(0.5, 2.0), "commit_timestamp": int(time.time()) - random.randint(60, 3600)},
            {"pipeline_name": "feature-pipeline", "branch_name": "main", "status": "FAILED", "lead_time_seconds": random.uniform(0.5, 2.0), "commit_timestamp": int(time.time()) - random.randint(60, 3600)}
        ]

    def collect(self):
        # Create a metric family
        metric_family = GaugeMetricFamily(
            "jenkins_lead_time_seconds",
            "Lead time for code integration",
            labels=["pipeline_name", "branch_name", "status"]
        )

        # Fetch data dynamically
        pipeline_data = self.fetch_pipeline_data()

        # Add metrics with custom timestamps
        for pipeline in pipeline_data:
            metric_family.add_metric(
                labels=[
                    pipeline["pipeline_name"],
                    pipeline["branch_name"],
                    pipeline["status"],
                ],
                value=pipeline["lead_time_seconds"],
                timestamp=pipeline["commit_timestamp"]
            )

        yield metric_family


