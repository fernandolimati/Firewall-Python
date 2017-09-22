import subprocess as sub
from datetime import datetime
import requests

def consultaWhiteList(ip):
    arq = open("whitelist.txt", "r")
    for linha in arq:
        ips = linha.split(";")
        for ipLido in ips:
            if(ipLido == ip):return True
    arq.close()
    return False

def consultaIP(ip):
    api_key = 'CwUJoQrItYeBQR0PzwezKhO3afrvB8mM1GCNmEdb'
    request = 'https://www.abuseipdb.com/check/%s/json?key=%s' % (ip, api_key)

    r = requests.get(request)
    #try:
    data = r.json()
    if data == []:
        return False
    else:

        try:
            for record in data:
                print("IP:{} / Pais de Origem:{} / Categoria:{} / Adicionado:{}".format(ip, record['country'],record['category'],record['created']))
        except (ValueError, KeyError, TypeError):
            try:
                print("IP:{} / Pais de Origem:{} / Categoria:{} / Adicionado:{}".format(ip, data['country'],data['category'],data['created']))
            except (ValueError, KeyError, TypeError):
                print("Erro JSON")
    return True

def main():
    try:
        now = datetime.now()
        arquivo = str(now)[:10] + ".txt"
        arq = open(arquivo, "a+")
        p = sub.Popen(('sudo', 'tcpdump', '-nl', '-tttt'), stdout=sub.PIPE)
        for line in iter(p.stdout.readline, b''):
            outputTcpdump = line.split(',')
            data,time = outputTcpdump[0][:19].split(" ")
            outputTcpdump = outputTcpdump[0][30:].split(":")
            outputTcpdump = outputTcpdump[0]
            outputTcpdump = outputTcpdump.split(">")
            outputTcpdump[0] = outputTcpdump[0][:len(outputTcpdump[0])-1]
            outputTcpdump[1] = outputTcpdump[1][1:]
            input = outputTcpdump[0].split(".")
            output = outputTcpdump[1].split(".")
            portIN =input[4]
            ipIN = input[0]+"."+input[1]+"."+input[2]+"."+input[3]
            portOut = output[4]
            ipOut = output[0]+"."+output[1]+"."+output[2]+"."+output[3]
            if(not consultaWhiteList(ipIN)):
                arq.write(data + "|" + time + "|" + ipIN + "|" + portIN + "|" + ipOut + "|" + portOut + ";")
                if (consultaIP(ipIN)): print("Blacklisted!")

        arq.close()
    except Exception:
        pass

main()

#nohup python capturar-pacotes-v2.py > /dev/null 2>&1&