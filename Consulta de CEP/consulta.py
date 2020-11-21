import requests
while True:
    try:
        CEP = int(input("Informe o seu CEP sem traço ou espaço: "))
        CEP = str(CEP)
        if len(CEP) != 8:
            print("Insira um valor válido.\n")
            continue
    except ValueError:
        print("Insira um valor válido.\n")
    else:
        conexao = requests.get("https://viacep.com.br/ws/" + CEP + "/json/", auth=('', ''))
        dados = conexao.json()
        for each in dados:
            print(each.upper() + ': ' + dados[each])
        break
