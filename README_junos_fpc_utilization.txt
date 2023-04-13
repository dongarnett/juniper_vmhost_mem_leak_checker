# juniper_automation_fpc_util_avg
This tool obtains a list of FPCs currently online and returns the following over a user supplied interval period:

-CPU Utilization
1. Maximum CPU Utilization %
2. Average CPU Utilization %
3. Average Total Memory (in MB)
4. Average Memory Heap %
5. Average Memory Buffer %



Usage:
you@your_computer# python3 junos_fpc_utilization.py <ip-address> <username> <password> <interval-count>


Example Run:
me@my_computer# python3 junos_fpc_utilization.py 10.0.0.21 user123 passwd123 10
Sending command: show chassis fpc

There are 4 FPC(s) online in 10.0.0.21
FPC 1 state is Online. Current CPU utilization is 51. Current memory utilization is 2048MB, buffer use % is 28, and heap use % is 66.
FPC 2 state is Online. Current CPU utilization is 31. Current memory utilization is 2048MB, buffer use % is 28, and heap use % is 65.
FPC 3 state is Online. Current CPU utilization is 29. Current memory utilization is 2048MB, buffer use % is 20, and heap use % is 71.
FPC 4 state is Online. Current CPU utilization is 15. Current memory utilization is 3168MB, buffer use % is 26, and heap use % is 35.
Sending command: show chassis fpc

Interval 0
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 31%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 15%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 1
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 15%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 2
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 15%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 3
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 15%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 4
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 5
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 6
Sending command: show chassis fpc

FPC 1 CPU Utilization: 27%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 41%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 7
Sending command: show chassis fpc

FPC 1 CPU Utilization: 30%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 28%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 8
Sending command: show chassis fpc

FPC 1 CPU Utilization: 30%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 32%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 28%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 9
Sending command: show chassis fpc

FPC 1 CPU Utilization: 30%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 30%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 28%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
Interval 10
Sending command: show chassis fpc

FPC 1 CPU Utilization: 30%
FPC 1 CPU Utilization - Total Memory: 2048MB
FPC 1 CPU Utilization - Memory Heap: 66%
FPC 1 CPU Utilization - Memory Buffer: 28%
FPC 2 CPU Utilization: 30%
FPC 2 CPU Utilization - Total Memory: 2048MB
FPC 2 CPU Utilization - Memory Heap: 65%
FPC 2 CPU Utilization - Memory Buffer: 28%
FPC 3 CPU Utilization: 28%
FPC 3 CPU Utilization - Total Memory: 2048MB
FPC 3 CPU Utilization - Memory Heap: 71%
FPC 3 CPU Utilization - Memory Buffer: 20%
FPC 4 CPU Utilization: 16%
FPC 4 CPU Utilization - Total Memory: 3168MB
FPC 4 CPU Utilization - Memory Heap: 35%
FPC 4 CPU Utilization - Memory Buffer: 26%
########################################################
FPCs online in slots: ['1', '2', '3', '4']
########################################################
################# FPC SLOT 1 SUMMARY ###################
########################################################
FPC CPU utilizations after 10x 1 second iterations:
########################################################
FPC 1 CPU Utilization (Maximum): 30%
FPC 1 CPU Utilization (Average): 28.09%
FPC 1 CPU Utilization - Total Memory (Average): 2048MB
FPC 1 CPU Utilization - Memory Heap (Average): 66.0%
FPC 1 CPU Utilization - Memory Buffer (Average): 28.0%
########################################################
########################################################
########################################################
########################################################
################# FPC SLOT 2 SUMMARY ###################
########################################################
FPC CPU utilizations after 10x 1 second iterations:
########################################################
FPC 2 CPU Utilization (Maximum): 32%
FPC 2 CPU Utilization (Average): 31.55%
FPC 2 CPU Utilization - Total Memory (Average): 2048MB
FPC 2 CPU Utilization - Memory Heap (Average): 65.0%
FPC 2 CPU Utilization - Memory Buffer (Average): 28.0%
########################################################
########################################################
########################################################
########################################################
################# FPC SLOT 3 SUMMARY ###################
########################################################
FPC CPU utilizations after 10x 1 second iterations:
########################################################
FPC 3 CPU Utilization (Maximum): 41%
FPC 3 CPU Utilization (Average): 36.27%
FPC 3 CPU Utilization - Total Memory (Average): 2048MB
FPC 3 CPU Utilization - Memory Heap (Average): 71.0%
FPC 3 CPU Utilization - Memory Buffer (Average): 20.0%
########################################################
########################################################
########################################################
########################################################
################# FPC SLOT 4 SUMMARY ###################
########################################################
FPC CPU utilizations after 10x 1 second iterations:
########################################################
FPC 4 CPU Utilization (Maximum): 16%
FPC 4 CPU Utilization (Average): 15.64%
FPC 4 CPU Utilization - Total Memory (Average): 3168MB
FPC 4 CPU Utilization - Memory Heap (Average): 35.0%
FPC 4 CPU Utilization - Memory Buffer (Average): 26.0%
########################################################
########################################################
########################################################
