# junos_vmhost_mem_leak_check


Purpose:
The purpose of this tool is to find any processes that have consumed, but not freed resident memory buffers.
This tool should be run as part a larger script where a device trigger or entire test case is inserted between the pre and post-trigger checks.
This tool can also be run without triggers to determine if memory is being consumed while the device is in steady state without invoking any trigger(s).

The following memory data points are collected:
1. Pre-trigger: Process names
2. Pre-trigger: Process IDs
3. Pre-trigger: Resident memory utilization (KB)
--- Device triggers should be performed here ---
4. Post-trigger: Resident memory utilization (KB)



Requirements:
The Paramiko SSH library is required for connectivity to the target device.
Juniper devices running VMHost releases are supported.
Juniper devices running standard and EVO release are not supported with this tool.


Usage:
you@your_computer# python3 junos_vmhost_mem_leak_check.py <ip-address> <username> <password> <interval-count>


Example Run:
me@my_computer# python3 junos_vmhost_mem_leak_check.py 10.0.0.21 user123 passwd123

Sending command: show system memory | match / | except : | no-more

Sending command: show system memory | match / | except : | no-more

Process /usr/sbin/eventd (PID: 12649) is still holding 32KB of resident memory after test execution completion.
Process /usr/sbin/jsd (PID: 13556) is still holding 4KB of resident memory after test execution completion.
Process /usr/sbin/na-grpcd (PID: 13560) is still holding 52KB of resident memory after test execution completion.
Process /usr/sbin/rpdtmd (PID: 13561) is still holding 4KB of resident memory after test execution completion.
