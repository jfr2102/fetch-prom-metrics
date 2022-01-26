queries = [("QUERYNAME", "PROM_QUERY"),
           ("QUERYNAME", "PROM_QUERY")
]

# Example:
# queries = [ ("storm_topology_Parser_Executed_count_KAFKA", "storm_topology_Parser_Executed_count{component_id=\"bolt\", topology_id=~\".*Kafka.*\"}")
# ,   ("storm_topology_WindowBolt_Executed_count_KAFKA", "storm_topology_WindowBolt_Executed_count{topology_id=~\".*Kafka.*\"}")
# ,   ("storm_topology_Windowbolt_Throughput_sum", "sum(rate(storm_topology_WindowBolt_Executed_count{topology_id=~\".*Kafka.*\"}[20s]))")
# ,   ("storm_topology_Windowbolt_Throughput", "rate(storm_topology_WindowBolt_Executed_count{topology_id=~\".*Kafka.*\"}[20s])")
# ,   ("node_cpu_seconds_total_1m", "avg without (mode,cpu) (1 - rate(node_cpu_seconds_total{mode=\"idle\"}[1m]))")
# ]
                                                                                                                    