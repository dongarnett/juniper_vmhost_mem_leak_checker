import paramiko
from lib_ssh_connectivity import Device
from lib_ssh_connectivity import create_handle_quiet
import os
import re
import sys
import time
from pprint import pprint
import argparse
from collections import defaultdict



'''Get VMHost system memory values from device'''
def get_system_proc_memory(dut_host):
    '''Command sets for device configuration'''
    #command_set_1 = [f'show system memory | match "/" | except ":" | no-more']
    command_set_1 = [f'show system memory | match / | except : | no-more']
    '''Create handle'''
    dut_host_session = create_handle_quiet(dut_host)
    dut_host_terminal = dut_host_session.invoke_shell()
    '''Start execution'''
    for command in command_set_1:
        print(f'Sending command: {command}\n')
        try:
            dut_host_terminal.send(f'{command}\n')
            time.sleep(3)
        except:
            print(f"An error occurred.")
            time.sleep(1)
        output = dut_host_terminal.recv(100000).decode('utf-8')
    output_recv = output.split('\r\n')
    dut_host_terminal.send('exit\n')
    return output


'''Parse output from memory data retrieved'''
def get_proc_mem_use(inputs):
    processes = ['proc_name']
    proc_dict = {}
    proc_name_dict = {}
    proc_id_dict = {}
    proc_res_mem_dict = {}
    i = 0

    init_proc_name = re.findall(r'\)\s+\/[a-z]+\/\S+', inputs, re.MULTILINE)
    init_proc_pid = re.findall(r'^\s+[0-9]+', inputs, re.MULTILINE)
    init_proc_res_mem_use = re.findall(r'\d+\(\d+.\d+\)\s+\/', inputs, re.MULTILINE)
    proc_res_mem_use = []

    for init_line in init_proc_res_mem_use:
        line = re.findall(r'\d+\(', init_line)
        for l in line:
            k = l.replace('(', '')
            #print(k)
            proc_res_mem_use.append(k)

    mem_name_list = [line.replace(') ', '') for line in init_proc_name]
    mem_pid_list = [line.replace(' ', '') for line in init_proc_pid]

    count = len(mem_name_list) + 1

    process_id = list(range(1,count))

    for proc in processes:
        for proc_id in process_id:
            proc_suffix = str(proc_id)
            proc_name_dict[proc + "_" + proc_suffix] = mem_name_list[i]
            proc_id_dict[proc + "_" + proc_suffix+"_"+"pid"] = mem_pid_list[i]
            proc_res_mem_dict[proc + "_" + proc_suffix+"_"+"res_mem"] = proc_res_mem_use[i]
            i += 1

    res_mem_use_val_list = []
    for proc in processes:
        for proc_id in process_id:
            proc_suffix = str(proc_id)
            res_mem_use = proc_res_mem_dict.get(proc + "_" + proc_suffix+"_"+"res_mem")
            res_mem_use_val_list.append(res_mem_use)

    pid_val_list = []
    for proc in processes:
        for proc_id in process_id:
            proc_suffix = str(proc_id)
            pid_val = proc_id_dict.get(proc + "_" + proc_suffix+"_"+"pid")
            pid_val_list.append(pid_val)

    return [proc_name_dict, proc_id_dict, proc_res_mem_dict]
