import requests

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


ip = raw_input("Digite ip para consulta: ")
if(consultaIP(ip)):print("CONSTA NO BANCO DE DADOS ABUSE")