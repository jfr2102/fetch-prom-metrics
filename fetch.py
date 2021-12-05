from parides.prom_conv import from_prom_to_df
from datetime import datetime as dt, datetime
from datetime import timedelta
import os
import sys
from matplotlib import pyplot

# List of queries to fetch
#from querylist import *
from myquerylist import *

# Config
#from config import *
from myconfig import *
try:
    os.mkdir("prom-metrics")
    print("created prom-metrics directory")
except FileExistsError:
    print("prom-metrics directory already exists")
now = dt.now()
if len(sys.argv) == 2:
    path = sys.argv[1]
else:
    path = (now.strftime("%Y-%m-%d-%H_%M"))
os.mkdir("prom-metrics/"+path)
for q in queries:
    df = from_prom_to_df(
        resolution    = resolution,
        start_time    = start_time,
        end_time      = end_time,
        url           = url,
        metrics_query = q[1]
    )
    df.to_csv("prom-metrics/" + path + '/' + q[0] + '.csv')
