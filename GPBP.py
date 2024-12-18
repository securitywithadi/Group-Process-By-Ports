processes = [("process1", 80), ("process2", 8080), ("process3", 80), ("process4", 443)]
port_to_processes = {}

for process, port in processes:
    port_to_processes.setdefault(port, []).append(process)

print(port_to_processes)
