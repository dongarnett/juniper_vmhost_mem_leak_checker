import os
import paramiko
import re
import sys
import time
from pprint import pprint
import argparse
from lib_ssh_connectivity import Device
from lib_junos_memory_proc_check import get_system_proc_memory
from lib_junos_memory_proc_check import get_proc_mem_use


'''The following code can be used to execute this script file on 1 device under test.'''
cli_args = sys.argv[1:]
dut_ip = cli_args[0]
dut_user = cli_args[1]
dut_pass = cli_args[2]


'''DUT Login parameters'''
host_ip = dut_ip
user = dut_user
passwd = dut_pass
timeout = 30


def main():
    dut_host = Device(host_ip, user, passwd)
    try:
        pre_inputs = get_system_proc_memory(dut_host)
        #print(pre_inputs)
    except:
        print('An error has occurred')
    # PRE-TRIGGER: Call function to parse inputs and return list of 3 dictionaries (proc_name, pid, and res_mem_usage}
    pre_outputs_dict = get_proc_mem_use(pre_inputs)
    # PRE-TRIGGER: Extract and store each dictionary
    pre_trig_dict_proc_names = (pre_outputs_dict[0])
    pre_trig_dict_proc_id = (pre_outputs_dict[1])
    pre_trig_dict_proc_res_mem = (pre_outputs_dict[2])
    # POST-TRIGGER: Convert dictionary values to lists
    pre_trig_list_proc_names = list(pre_trig_dict_proc_names.values())
    pre_trig_list_proc_id = list(pre_trig_dict_proc_id.values())
    pre_trig_list_proc_res_mem = list(pre_trig_dict_proc_res_mem.values())

    #########################################
    ###### INSERT TRIGGER ACTIONS HERE#######
    #########################################
    time.sleep(30)
    #########################################
    #########################################
    #########################################

    try:
        post_inputs = get_system_proc_memory(dut_host)
        #print(post_inputs)
    except:
        print('An error has occurred')
    # POST-TRIGGER: Call function to parse inputs and return list of 3 dictionaries (proc_name, pid, and res_mem_usage}
    post_outputs_dict = get_proc_mem_use(post_inputs)
    # POST-TRIGGER: Extract and store each dictionary
    post_trig_dict_proc_names = (post_outputs_dict[0])
    post_trig_dict_proc_id = (post_outputs_dict[1])
    post_trig_dict_proc_res_mem = (post_outputs_dict[2])
    # POST-TRIGGER: Convert dictionary values to lists
    post_trig_list_proc_names = list(post_trig_dict_proc_names.values())
    post_trig_list_proc_id = list(post_trig_dict_proc_id.values())
    post_trig_list_proc_res_mem = list(post_trig_dict_proc_res_mem.values())

    # Compare pre and post-trigger memory usage values
    if len(pre_trig_list_proc_res_mem) == len(post_trig_list_proc_res_mem):
        count = len(pre_trig_list_proc_res_mem)
        i = 0
        while i < count:
            index = str(i)
            mem_used = int(post_trig_list_proc_res_mem[i]) - int(pre_trig_list_proc_res_mem[i])
            if mem_used > 0:
                print(f'Process {pre_trig_list_proc_names[i]} (PID: {pre_trig_list_proc_id[i]}) is still holding {mem_used}KB of resident memory after test execution completion.')
            i += 1



if __name__ == '__main__':
    main()
