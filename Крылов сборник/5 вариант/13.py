from ipaddress import ip_network

cnt = 0
net = ip_network('252.67.33.87/255.252.0.0', False)
for adress in net:
    if (2 * bin(int(adress))[:-16].count('1')) < bin(int(adress))[-16:].count('1'):
        cnt += 1
print(cnt)
