from ipaddress import ip_network

for a in range(1,256):
    net = ip_network(f'252.63.194.3/255.255.{a}.O')
    for adress in net:
        if bin(int(adress))[:-16].count('1') >= bin(int(adress))[-16:].count('1'):
            print(a)
            break
