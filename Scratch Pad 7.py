"""import psutil, pprint


print("Network Interfaces:", "\n ")
pprint.pprint(psutil.net_if_stats())
print ("\n ", "\n ")

for i in (psutil.net_if_stats()):
    print(i)
    # print (e)"""


import psutil

usage = psutil.disk_usage("C:\\")

part = psutil.disk_partitions()



print (usage, "\n")

print(part)


for i in part:
    print(i.device + "\\")



