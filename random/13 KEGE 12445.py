from ipaddress import *

net = ip_network('192.168.32.48/255.255.255.240', 0)
s = 0
for ip in net:
    if f'{ip:b}'.count('1') % 2 == 1:
        s += 1
print(s)
