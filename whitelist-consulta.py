

def consultaWhiteList(ip):
    arq = open("whitelist.txt", "r")
    for linha in arq:
        ips = linha.split(";")
        for ipLido in ips:
            if(ipLido == ip):return True
        print(ips)
    arq.close()