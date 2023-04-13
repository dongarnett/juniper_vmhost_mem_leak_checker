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


pre_inputs = '''
don@milnet-r4> show system memory | match "/" | except ":"
      1         0(00.00)        0(00.00) /sbin/init --
  18817     31012(88.29)    12396(00.61) /usr/sbin/eventd -r -s -A
  18821      3088(55.14)     2412(00.12) /sbin/jlaunchhelperd
  18823      7340(44.40)     4856(00.24) /sbin/jlaunchd -N
  18834      1884(91.63)     1296(00.06) /usr/libexec/bslockd -mp -N
  18835      6556(70.92)     3932(00.19) /usr/sbin/tnetd -N -l
  18837    191428(04.57)    95300(04.67) /usr/sbin/chassisd -N
  18838     21844(00.52)    12916(00.63) /usr/sbin/sdk-vmmd -N
  18840     18632(00.44)    11084(00.54) /usr/sbin/craftd -N
  18841     65092(01.55)    45280(02.22) /usr/sbin/mgd -N
  18844      7324(00.00)     4056(00.20) /usr/sbin/inetd -N -w -R 512
  18848     25284(00.60)    16244(00.80) /usr/sbin/ppmd -N
  18854     25648(00.61)    16120(00.79) /usr/sbin/bfdd -N
  18855     27464(00.66)    16776(00.82) /usr/sbin/clksyncd -N
  18856     25680(00.61)    17584(00.86) /usr/sbin/lacpd -N
  18857     19724(00.47)    12248(00.60) /usr/sbin/lfmd -N
  18858     26344(00.63)    16352(00.80) /usr/libexec32/smid -N
  18860     71108(01.70)    11620(00.57) /usr/sbin/shm-rtsdbd -N
  18861     17284(00.00)     6040(00.30) /usr/sbin/gstatd -N
  18864     16188(00.00)     4496(00.22) /usr/sbin/rpcbind -N -I -h 128.0.0.1
  18870     12336(00.00)     2960(00.14) /usr/sbin/pmcd -N
  18871     21936(00.52)    14420(00.71) /usr/bin/python3 /usr/sbin/jsysmond -N
  18873     16692(00.00)     4624(00.23) /usr/sbin/mountd -N -s -p 6666
  18874     21752(00.00)     7756(00.38) /usr/sbin/pmond -N
  18875     65852(01.57)    24892(01.22) /usr/libexec32/bbe-smgd -b -N
  18887     29232(00.70)    11692(00.57) /usr/sbin/appidd -N
  18892     13876(00.00)     4248(00.21) /usr/sbin/cron -s
  18901     11324(00.00)     1892(00.09) /bin/sh /usr/sbin/charged -N
  18935     24468(00.00)     9568(00.47) /usr/sbin/bbe-up-pfcp-proxyd -N
  18939         0(00.00)        0(00.00) /usr/sbin/license-check -U -M -p 10 -i 10
  18941     16604(00.00)     4848(00.24) /usr/sbin/na-mqttd -c /opt/telemetry/na-mqttd/na-mqtt.conf
  18944     13992(00.33)     7692(00.38) /usr/sbin/mgd-api -N
  18948     20416(00.49)    11576(00.57) /usr/sbin/jsqlsyncd -N
  18951      4648(00.11)     1704(00.08) /sbin/watchdog -t-1
  18986     11900(00.00)     2744(00.13) /usr/libexec/getty.junos 3wire ttyv0
  19040    864636(20.63)   109476(05.36) /usr/sbin/rpd -N
  19041     56396(00.00)    26956(01.32) /usr/sbin/l2ald -N
  19042     19348(00.46)    11816(00.58) /usr/sbin/apsd -N
  19043    751876(17.94)    51204(02.51) /usr/libexec32/cosd
  19046     15256(00.36)     7420(00.36) /usr/sbin/lmpd
  19049     13808(00.33)     6992(00.34) /usr/sbin/fsad -N
  19050     14280(00.34)     7332(00.36) /usr/sbin/rdd -N
  19051     14176(00.34)     7224(00.35) /usr/sbin/pppd -N
  19052     31252(00.75)    18664(00.91) /usr/sbin/dfcd -N
  19053     41008(00.98)    28212(01.38) /usr/sbin/l2cpd -N
  19054     19288(00.46)    11816(00.58) /usr/sbin/oamd -N
  19055     20724(00.49)    11112(00.54) /usr/sbin/mplsoamd -N
  19056     16456(00.39)     8088(00.40) /usr/sbin/sendd -N
  19057     13916(00.33)     6844(00.34) /usr/sbin/iccpd -N
  19058     21336(00.51)    11524(00.56) /usr/sbin/jddosd -N
  19062     18908(00.45)     8648(00.42) /usr/sbin/commit-syncd -N
  19063     13848(00.33)     6980(00.34) /usr/sbin/mspd -N
  19064     25820(00.00)     9432(00.46) /usr/sbin/jkdsd -N
  19067     15088(00.36)     8828(00.43) /usr/sbin/jinsightd -N
  19069     37932(00.91)    23340(01.14) /usr/sbin/jsd -N
  19072     20916(00.50)    10560(00.52) /usr/sbin/xmlproxyd -N
  19073     28852(00.69)    11772(00.58) /usr/sbin/overlayd -N
  19074     20056(00.48)    10696(00.52) /usr/sbin/ntf-agent -N -c /var/etc/ntf-agent.conf
  19075     44724(01.07)    34888(01.71) /usr/sbin/na-grpcd -c /opt/telemetry/na-grpcd/na-grpc-server.ini
  19076     61672(00.00)    23952(01.17) /usr/sbin/rpdtmd -N
  19077     21996(00.52)    12760(00.62) /usr/sbin/pkid -N
  19079     27064(00.65)    16920(00.83) /usr/sbin/alarmd -N
  19080     20468(00.49)    12908(00.63) /usr/sbin/snmpd -N
  19081     58908(01.41)    47024(02.30) /usr/sbin/mib2d -N
  19082    756228(18.05)    50080(02.45) /sbin/dcd -N
  19083      5696(00.14)     2552(00.12) /usr/sbin/tnp.sntpd -N
  19084     30748(00.73)    18912(00.93) /usr/libexec32/pfed -N
  19085     39048(00.93)    19024(00.93) /usr/libexec32/dfwd -N
  19086     14076(00.34)     7104(00.35) /usr/sbin/irsd -N
  19087     23900(00.57)    13676(00.67) /usr/sbin/stats-agentd -N
  19088    129972(03.10)    17328(00.85) /usr/sbin/transportd -N
  19089     24404(00.58)    17408(00.85) /usr/sbin/agentd -N
  19109    111496(02.66)    11708(00.57) /usr/sbin/alarm-mgmtd -N
  19110     54700(00.00)    15120(00.74) /usr/sbin/bbe-smg-upd -N
  19111     26004(00.00)    10112(00.50) /usr/sbin/jkhmd -N
  19112     66416(01.59)    32524(01.59) /usr/sbin/dot1xd -N
  19113     24068(00.57)    14784(00.72) /usr/libexec32/bbe-statsd -N
  19115     43944(00.00)    12984(00.64) /usr/sbin/rep-clientd -N
  19117     26668(00.00)    10800(00.53) /usr/sbin/rep-serverd -N
  19220     13808(00.33)     6972(00.34) /usr/sbin/datapath-traced -N
'''


post_inputs = '''
don@milnet-r4> show system memory | match "/" | except ":"
      1         0(00.00)        0(00.00) /sbin/init --
  18817     31012(88.29)    62396(00.61) /usr/sbin/eventd -r -s -A
  18821      3088(55.14)     2412(00.12) /sbin/jlaunchhelperd
  18823      7340(44.40)     4856(00.24) /sbin/jlaunchd -N
  18834      1884(91.63)     1296(00.06) /usr/libexec/bslockd -mp -N
  18835      6556(70.92)     3932(00.19) /usr/sbin/tnetd -N -l
  18837    191428(04.57)    95300(04.67) /usr/sbin/chassisd -N
  18838     21844(00.52)    12916(00.63) /usr/sbin/sdk-vmmd -N
  18840     18632(00.44)    11084(00.54) /usr/sbin/craftd -N
  18841     65092(01.55)    45280(02.22) /usr/sbin/mgd -N
  18844      7324(00.00)     4056(00.20) /usr/sbin/inetd -N -w -R 512
  18848     25284(00.60)    16244(00.80) /usr/sbin/ppmd -N
  18854     25648(00.61)    16120(00.79) /usr/sbin/bfdd -N
  18855     27464(00.66)    16776(00.82) /usr/sbin/clksyncd -N
  18856     25680(00.61)    17584(00.86) /usr/sbin/lacpd -N
  18857     19724(00.47)    12248(00.60) /usr/sbin/lfmd -N
  18858     26344(00.63)    16352(00.80) /usr/libexec32/smid -N
  18860     71108(01.70)    11620(00.57) /usr/sbin/shm-rtsdbd -N
  18861     17284(00.00)     16040(00.30) /usr/sbin/gstatd -N
  18864     16188(00.00)     4496(00.22) /usr/sbin/rpcbind -N -I -h 128.0.0.1
  18870     12336(00.00)     2960(00.14) /usr/sbin/pmcd -N
  18871     21936(00.52)    14420(00.71) /usr/bin/python3 /usr/sbin/jsysmond -N
  18873     16692(00.00)     4624(00.23) /usr/sbin/mountd -N -s -p 6666
  18874     21752(00.00)     7756(00.38) /usr/sbin/pmond -N
  18875     65852(01.57)    24892(01.22) /usr/libexec32/bbe-smgd -b -N
  18887     29232(00.70)    11692(00.57) /usr/sbin/appidd -N
  18892     13876(00.00)     4248(00.21) /usr/sbin/cron -s
  18901     11324(00.00)     1892(00.09) /bin/sh /usr/sbin/charged -N
  18935     24468(00.00)     9568(00.47) /usr/sbin/bbe-up-pfcp-proxyd -N
  18939         0(00.00)        0(00.00) /usr/sbin/license-check -U -M -p 10 -i 10
  18941     16604(00.00)     4848(00.24) /usr/sbin/na-mqttd -c /opt/telemetry/na-mqttd/na-mqtt.conf
  18944     13992(00.33)     7692(00.38) /usr/sbin/mgd-api -N
  18948     20416(00.49)    11576(00.57) /usr/sbin/jsqlsyncd -N
  18951      4648(00.11)     1704(00.08) /sbin/watchdog -t-1
  18986     11900(00.00)     2744(00.13) /usr/libexec/getty.junos 3wire ttyv0
  19040    864636(20.63)   109476(05.36) /usr/sbin/rpd -N
  19041     56396(00.00)    26956(01.32) /usr/sbin/l2ald -N
  19042     19348(00.46)    11816(00.58) /usr/sbin/apsd -N
  19043    751876(17.94)    51204(02.51) /usr/libexec32/cosd
  19046     15256(00.36)     57420(00.36) /usr/sbin/lmpd
  19049     13808(00.33)     6992(00.34) /usr/sbin/fsad -N
  19050     14280(00.34)     7332(00.36) /usr/sbin/rdd -N
  19051     14176(00.34)     7224(00.35) /usr/sbin/pppd -N
  19052     31252(00.75)    18664(00.91) /usr/sbin/dfcd -N
  19053     41008(00.98)    28212(01.38) /usr/sbin/l2cpd -N
  19054     19288(00.46)    11816(00.58) /usr/sbin/oamd -N
  19055     20724(00.49)    11112(00.54) /usr/sbin/mplsoamd -N
  19056     16456(00.39)     8088(00.40) /usr/sbin/sendd -N
  19057     13916(00.33)     6844(00.34) /usr/sbin/iccpd -N
  19058     21336(00.51)    11524(00.56) /usr/sbin/jddosd -N
  19062     18908(00.45)     8648(00.42) /usr/sbin/commit-syncd -N
  19063     13848(00.33)     6980(00.34) /usr/sbin/mspd -N
  19064     25820(00.00)     9432(00.46) /usr/sbin/jkdsd -N
  19067     15088(00.36)     8828(00.43) /usr/sbin/jinsightd -N
  19069     37932(00.91)    23340(01.14) /usr/sbin/jsd -N
  19072     20916(00.50)    10560(00.52) /usr/sbin/xmlproxyd -N
  19073     28852(00.69)    11772(00.58) /usr/sbin/overlayd -N
  19074     20056(00.48)    10696(00.52) /usr/sbin/ntf-agent -N -c /var/etc/ntf-agent.conf
  19075     44724(01.07)    34888(01.71) /usr/sbin/na-grpcd -c /opt/telemetry/na-grpcd/na-grpc-server.ini
  19076     61672(00.00)    23952(01.17) /usr/sbin/rpdtmd -N
  19077     21996(00.52)    12760(00.62) /usr/sbin/pkid -N
  19079     27064(00.65)    16920(00.83) /usr/sbin/alarmd -N
  19080     20468(00.49)    12908(00.63) /usr/sbin/snmpd -N
  19081     58908(01.41)    47024(02.30) /usr/sbin/mib2d -N
  19082    756228(18.05)    50080(02.45) /sbin/dcd -N
  19083      5696(00.14)     12552(00.12) /usr/sbin/tnp.sntpd -N
  19084     30748(00.73)    18912(00.93) /usr/libexec32/pfed -N
  19085     39048(00.93)    19024(00.93) /usr/libexec32/dfwd -N
  19086     14076(00.34)     7104(00.35) /usr/sbin/irsd -N
  19087     23900(00.57)    13676(00.67) /usr/sbin/stats-agentd -N
  19088    129972(03.10)    17328(00.85) /usr/sbin/transportd -N
  19089     24404(00.58)    17408(00.85) /usr/sbin/agentd -N
  19109    111496(02.66)    11708(00.57) /usr/sbin/alarm-mgmtd -N
  19110     54700(00.00)    15120(00.74) /usr/sbin/bbe-smg-upd -N
  19111     26004(00.00)    10112(00.50) /usr/sbin/jkhmd -N
  19112     66416(01.59)    32524(01.59) /usr/sbin/dot1xd -N
  19113     24068(00.57)    14784(00.72) /usr/libexec32/bbe-statsd -N
  19115     43944(00.00)    12984(00.64) /usr/sbin/rep-clientd -N
  19117     26668(00.00)    10800(00.53) /usr/sbin/rep-serverd -N
  19220     13808(00.33)     6972(00.34) /usr/sbin/datapath-traced -N
'''



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
    # dut_host = Device(host_ip, user, passwd)
    # try:
    #     pre_inputs = get_system_proc_memory(dut_host)
    #     #print(pre_inputs)
    # except:
    #     print('An error has occurred')
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
    time.sleep(5)
    #########################################
    #########################################
    #########################################

    # try:
    #     pre_inputs = get_system_proc_memory(dut_host)
    #     #print(pre_inputs)
    #     post_inputs = get_system_proc_memory(dut_host)
    #     #print(post_inputs)
    # except:
    #     print('An error has occurred')
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
    # print(pre_trig_list_proc_names)
    # print(pre_trig_list_proc_id)
    # print(pre_trig_list_proc_res_mem)
    # print(post_trig_list_proc_names)
    # print(post_trig_list_proc_id)
    # print(post_trig_list_proc_res_mem)

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
