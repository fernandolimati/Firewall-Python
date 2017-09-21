import subprocess as sub
from datetime import datetime

def main():
    try:
        now = datetime.now()
        arquivo = str(now)[:10] + ".txt"
        arq = open(arquivo, "w")
        p = sub.Popen(('sudo', 'tcpdump', '-nl', '-tttt'), stdout=sub.PIPE)
        for line in iter(p.stdout.readline, b''):
            outputTcpdump = line.split(',')
            outputTcpdump = outputTcpdump[0]
            dateTime, aux = outputTcpdump.split("IP")
            data = dateTime[0:10]
            time = dateTime[11:26]
            ipOrigem, ipDestino = aux.split('>')
            ipOrigem = ipOrigem[1:]
            aux = ipOrigem.split('.')
            portaOrigem = aux[4][:len(aux[4])-1]
            ipOrigem = aux[0] + "." + aux[1] + "." + aux[2] + "." + aux[3]
            ipDestino = ipDestino[1:]
            aux = ipDestino.split('.')
            portaDestino = aux[4]
            portaDestino = portaDestino.split(':')
            portaDestino = portaDestino[0]
            ipDestino = aux[0] + "." + aux[1] + "." + aux[2] + "." + aux[3]
            linhaArquivo = data+"|"+time+"|"+ipOrigem+"|"+portaOrigem+"|"+ipDestino+"|"+portaDestino+";"
            arq.write(linhaArquivo)
        arq.close()
    except Exception:
        pass


main()

