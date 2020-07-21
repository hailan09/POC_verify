import socket

def get_localhost_ip():
    #查询本机ip地址

    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    s.connect(('8.8.8.8',80))
    localhost = s.getsockname()[0]
    return localhost

print(get_localhost_ip())
