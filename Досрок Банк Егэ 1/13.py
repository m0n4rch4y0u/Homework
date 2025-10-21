from ipaddress import *

from ipaddress import *

n = ip_network('157.180.63.114/255.255.255.248', 0)
s = 0
for ip in n:
    if f'{ip:b}'.count('1') % 4 != 0:
        s += 1
print(s)
