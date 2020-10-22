import socket

def get_localhost_ip():
    #查询本机ip地址

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    localhost = s.getsockname()[0]
    return localhost

print(get_localhost_ip())


dns = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dns.bind(('10.5.84.138', 53))
dns.listen(1)
while 1:
    s, addr = dns.accept()
    dsd = s.recv(1024)
    print(dsd)
