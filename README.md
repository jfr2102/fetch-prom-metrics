# fetch-prom-metrics

Fetch List of Prometheus Metrics into and save as csv with help of: [parides](https://github.com/goettl79/parides)

### prerequisites:

Install [parides](https://github.com/goettl79/parides)
```bash
pip install parides
```

### usage
- Include List of Tuples of format ("QUERYNAME", "PROM_QUERY") in [querylist.py](querylist.py):
```python
queries = [("QUERYNAME", "PROM_QUERY"),
           ("QUERYNAME", "PROM_QUERY")
]
```
- configure resolutiom, start + end time and url in [config.py](config.py):
```python
resolution  = "10s"
start_time  = (dt.utcnow() - timedelta(minutes=5))
end_time    = dt.utcnow()
url         = "http://PROM_HOST:9090"
```
- run e.g. ```bash python3 fetch.py``` 
-> All queries are executed and results stored in prom-metrics/*EXECUTIONTIME*/*QUERYNAME*.csv
