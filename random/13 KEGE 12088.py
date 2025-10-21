from ipaddress import *

net = ip_network('112.154.132.0/255.255.252.0', 0)
s = 0
for ip in net:
    lt = f'{ip:b}'[:16]
    rt = f'{ip:b}'[16:]
    if rt.count('0') % 2 == 1:
        if lt.count('1') <= rt.count('0'):
            s += 1
print(s)