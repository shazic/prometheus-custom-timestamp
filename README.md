# Prometheus custom timestamps

## Overview 
This prototype is to understand how Prometheus consumes data points with custom timestamp fields, instead of its own time-series based timestamps.  
In this prototype, we will generate a metrics named jenkins_lead_time_seconds with some labels, a value and a custom timestamp.  
For example
```
jenkins_lead_time_seconds{"pipeline_name": "ci-pipeline", "branch_name": "main"} 2900 1732152626
```
Here, the value `1732152626` at the end is the custom timestamp and `2900` is the value for `jenkins_lead_time_seconds`.
These metrics would be made available for Prometheus to scrape.

When Prometheus should store and display data based on the timestamp that has been provided by the metrics, instead of the scrape time.
## Implementation Details
We were able to send metrics to Prometheus using custom timestamp (not the scrape timestamp). 
For this, we had to do the following:
1. Write a custom collector
1. Write a custom exporter for this collector
1. On the Prometheus side, we had to make the following changes:
  - Add the scrape target
  - Use an experimental feature called `out_of_order_time_window` that allows timestamps from the past to be added.
## References
This prototype is heavily influenced by the blog post https://dasl.cc/2024/07/07/setting-custom-timestamps-for-prometheus-metrics/ 
