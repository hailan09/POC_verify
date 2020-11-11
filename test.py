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


#通过js代码在控制台将cookie插入到浏览器
function setCookie(str) {
        const arr = str.split('; ');
        arr.forEach(item => {
            const name = item.split('=')[0];
            const value = item.split('=')[1];
            const exdate = new Date();
            exdate.setDate(exdate.getDate() + 7);
            const period = `expires=${exdate.toUTCString()}; `;
            document.cookie = `${name}=${value}; ${period}path=/`;
        })
    }
setCookie("cookie value")
