from datetime import datetime as dt, datetime
from datetime import timedelta

resolution  = "10s"
start_time  = dt.utcnow() - timedelta(minutes=5)
end_time    = dt.utcnow()
url         = "http://PROM_HOST:9090"