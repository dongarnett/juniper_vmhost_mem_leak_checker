import os
import paramiko
import re
import sys
import time
from pprint import pprint
import argparse


'''Create device class to handle connectivity'''
class Device:
    #def __init__(self, hostname, username, password, session_timeout):
    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        #self.session_timeout = session_timeout

'''Create device handle instance'''
def create_handle(self):
    # Connection Parameters
    print(f'Connecting to host {self.hostname}')
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=self.hostname, username=self.username, password=self.password)
    #client.load_system_host_keys(filename="/home/don/.ssh/id_rsa")
    #self.key_file = "/home/don/.ssh/id_rsa"
    #self.key = paramiko.RSAKey.from_private_key_file(key_file)
    #client.connect(hostname=switch_a, username=username, password=password)
    return client


'''Create device handle instance'''
def create_handle_quiet(self):
    # Connection Parameters
    #print(f'Connecting to host {self.hostname}')
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=self.hostname, username=self.username, password=self.password)
    #client.load_system_host_keys(filename="/home/don/.ssh/id_rsa")
    #self.key_file = "/home/don/.ssh/id_rsa"
    #self.key = paramiko.RSAKey.from_private_key_file(key_file)
    #client.connect(hostname=switch_a, username=username, password=password)
    return client
