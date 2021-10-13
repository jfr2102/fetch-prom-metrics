# fetch-prom-metrics

Fetch List of Prometheus Metrics into pandas df and save as csv.
### usage
- Include List of Tuples of format ("QUERYNAME", "PROM_QUERY") in querylist.py
```python
queries = [("QUERYNAME", "PROM_QUERY"),
           ("QUERYNAME", "PROM_QUERY")
]
```
- configure resolutiom, start + end time and url in fetch.py:
```python
resolution  = "10s"
start_time  = (dt.utcnow() - timedelta(minutes=5))
end_time    = dt.utcnow()
url         = "http://PROM_HOST:9090"
```