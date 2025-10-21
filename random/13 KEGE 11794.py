from ipaddress import *

for A in range(256):
    net = ip_network(f'223.167.{A}.167/255.255.255.192', 0)
    if all(f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0') for ip in net):
        print(A)
