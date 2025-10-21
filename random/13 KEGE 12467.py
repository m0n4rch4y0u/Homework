from ipaddress import *

k = 0
for A in range(256):
    net = ip_network(f'183.192.{A}.0/255.255.252.0', 0)
    if all(f'{ip:b}'[16:].count('1') > 3 for ip in net):
        print(A)
        exit()
