#!/usr/bin/env python3

import psutil, sys

def psmon(data_type):
    if data_type == 'cpu':
        cpu = psutil.cpu_times()
        print("system cpu total {}".format(cpu.system))
        print("system cpu idle {}".format(cpu.idle))
        print("system cpu iowait {}".format(cpu.iowait))
        print("system cpu user {}".format(cpu.user))
        print("system cpu guest {}".format(cpu.guest))
    elif data_type == 'mem':
        mem = psutil.virtual_memory()
        print("virtual total {}".format(mem.total))
        print("virtual used {}".format(mem.used))
        print("virtual free {}".format(mem.free))
        print("virtual shared {}".format(mem.shared))
    elif data_type == 'swap':
        swap = psutil.swap_memory()
        print("swap total {}".format(swap.total))
        print("swap used {}".format(swap.used))
        print("swap free {}".format(swap.free))
        print("swap percent {}".format(swap.percent))
    elif data_type == 'disk':
        disk = psutil.disk_partitions()
        for i in disk:
            print("disk device {}".format(i.device))
            print("disk mountpoint {}".format(i.mountpoint))
            print("disk fstype {}".format(i.fstype))
            print("mount options {}".format(i.opts))
    else:
        print("Wrong type of data")

if len(str(sys.argv[1:])) > 2:
    psmon(str(sys.argv[1]))
else:
    print("Variable not defined")
    sys.exit(1)
