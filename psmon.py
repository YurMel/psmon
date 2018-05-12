#!/usr/bin/env python

import psutil, sys

def psmon(data_type):
    if data_type == 'cpu':
	cpu = psutil.cpu_times()
	print "system cpu total", cpu.system
	print "system cpu idle", cpu.idle
	print "system cpu iowait", cpu.iowait
	print "system cpu user", cpu.user
	print "system cpu guest", cpu.guest
    elif data_type == 'mem':
	mem = psutil.virtual_memory()
	print "virtual total", mem.total
	print "virtual used", mem.used
	print "virtual free", mem.free
	print "virtual shared", mem.shared
    else:
	print("Wrong type of data")

if len(str(sys.argv[1:])) > 2:
    psmon(str(sys.argv[1]))
else:
    print("Variable not defined")
    sys.exit(1)
