from ipaddress import *

net = ip_network('142.108.56.118/255.255.255.240', False)
k = 0
for adress in net:
    if bin(int(adress))[:16].count('1') < bin(int(adress))[-16:].count('1'):
        k += 1
print(k)
