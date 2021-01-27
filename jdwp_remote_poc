# -*- coding:utf-8 -*-
import socket
import argparse

#can get the shell

def jdwp_remote_verify(ip,port):
    url = 'http://'+ip+':'+str(port)
    print('[+] Targeting  '+url)
    timeout=15
    try:
        socket.setdefaulttimeout(timeout)
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,int(port)))
        data = b"JDWP-Handshake"
        s.send(data)
        check_data = s.recv(14)
        if check_data == data:
            message = '[+] There is a vulnerability in the target IP on url: '
            return message,url
        else:
            pass
    except Exception as e:
        print(str(e))

    message = '[-] There is no vulnerability in the traget IP on url: '
    return message,url


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description="The script is used for valiation JDWP remote code Execution Vul")
    parse.add_argument('-t','--target',type=str,help='please enter Remote target IP',metavar='IPaddress',required=True)
    parse.add_argument('-p','--port',type=int,metavar='PORT',default=8000,help='please enter remote target Port')
    args = parse.parse_args()
    print(jdwp_remote_verify(args.target,args.port))
