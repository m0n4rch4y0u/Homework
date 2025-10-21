from ipaddress import ip_network

net = ip_network('106.184.0.0/255.248.0.0', False)

k = 0
for adress in net:
    if bin(int(adress)).count('1') % 2 != 0:
        k += 1
print(k)
