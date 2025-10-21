from ipaddress import *

n = ip_network('136.36.240.16/255.255.255.248', 0)
s = 0
for ip in n:
    if f'{ip:b}'.count('101') == 0:
        s+=1
print(s)
