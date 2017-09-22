import requests

def consultaIP(ip):
    api_key = 'CwUJoQrItYeBQR0PzwezKhO3afrvB8mM1GCNmEdb'
    request = 'https://www.abuseipdb.com/check/%s/json?key=%s' % (ip, api_key)

    r = requests.get(request)
    try:
        data = r.json()
        if data == []:
            return False
        else:
            #if (len(data)==1):
            #   print("IP:{} / Pais de Origem:{} / Categoria:{} / Adicionado:{}".format(ip,data['country'],data['category'],data['created']))
            #else:
                for record in data:
                   print(record['ip'])
                   #print("IP:{} / Pais de Origem:{} / Categoria:{} / Adicionado:{}".format(ip, record['country'],record['category'],record['created']))

        return True
    except (ValueError, KeyError, TypeError):
        print("Erro no JSON.")


#ip = raw_input("Digite ip para consulta: ")
print("APENAS 1 OCORRENCIA ----------------------------")
if(consultaIP('113.179.233.245')):print("CONSTA NO BANCO DE DADOS ABUSE")

print("MAIS DE 1 OCORRENCIA ----------------------------")
if(consultaIP('80.123.68.174')):print("CONSTA NO BANCO DE DADOS ABUSE")

print("NENHUMA OCORRENCIA ----------------------------")
if(consultaIP('191.191.150.8')):print("CONSTA NO BANCO DE DADOS ABUSE")
