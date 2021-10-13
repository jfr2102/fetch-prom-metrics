from parides.prom_conv import from_prom_to_df
from parides.prom_conv import from_prom_to_csv
from datetime import datetime as dt, datetime
from datetime import timedelta
import os
from matplotlib import pyplot

now = dt.now()
path= (now.strftime("%Y-%m-%d-%H_%M"))
os.mkdir(path)

queries = [("storm_topology_Parser_Executed_count" ,"storm_topology_Parser_Executed_count{component_id=\"bolt\", exported_instance=\"3c04ef351e4c\", exported_job=\"storm\", host_name=\"3c04ef351e4c\", instance=\"pushgateway:9091\", job=\"pushgateway\", task_id=\"11\", topology_id=\"CheckTopology-2-1634124643\", worker_port=\"6703\"}" )
]

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