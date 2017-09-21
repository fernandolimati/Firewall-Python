import subprocess as sub
from datetime import datetime

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
            arq.write(data+"|"+time+"|"+ipIN+"|"+portIN+"|"+ipOut+"|"+portOut+";")
        arq.close()
    except Exception:
        pass


main()