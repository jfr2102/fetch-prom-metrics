from parides.prom_conv import from_prom_to_df
from parides.prom_conv import from_prom_to_csv
from datetime import datetime as dt, datetime
from datetime import timedelta
import os
from matplotlib import pyplot

# List of queries to fetch
from querylist import *
#from myquerylist import *

# Config
from config import *
#from myconfig import *

now = dt.now()
path= (now.strftime("%Y-%m-%d-%H_%M"))
os.mkdir(path)

for q in queries:
    df = from_prom_to_df(
        resolution    = resolution,
        start_time    = start_time,
        end_time      = end_time,
        url           = url,
        metrics_query = q[1]
    )
    df.to_csv(path + '/' + q[0] + '.csv')