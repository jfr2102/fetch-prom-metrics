from parides.prom_conv import from_prom_to_df
from parides.prom_conv import from_prom_to_csv
from datetime import datetime as dt, datetime
from datetime import timedelta
import os
from matplotlib import pyplot

# List of queries to fetch
#from querylist import *
from myquerylist import *

now = dt.now()
path= (now.strftime("%Y-%m-%d-%H_%M"))
os.mkdir(path)

resolution  = "10s"
start_time  = (dt.utcnow() - timedelta(minutes=5))
end_time    = dt.utcnow()
url         = "http://172.24.38.172:9090"

for q in queries:
    df = from_prom_to_df(
        resolution    = resolution,
        start_time    = start_time,
        end_time      = end_time,
        url           = url,
        metrics_query =q[1]
    )
    df.to_csv(path+'/storm_topology_Parser_Executed_count.csv')