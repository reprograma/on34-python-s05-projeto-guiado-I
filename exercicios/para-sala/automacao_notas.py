dataset = {}  # Dicionario com escopo global


def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---\n")
    print("Aqui você pode calcular a aprovação de uma aluna.\n")
    numero_de_aulas = int(input("Houveram quantas aulas?: "))

    while True:
        # Chamo a função de pegar dados da aluna
        nome = obter_dados_aluna(numero_de_aulas)
        # Chamo a função de calcular a média da aluna
        media_ponderada = obter_media_ponderada(nome)
        resultado = obter_resultado(nome, media_ponderada, numero_de_aulas)
        recup = recuperacao()
        if resultado == "aprovada" or resultado == "reprovada por falta":
            print(f"A aluna {nome} da turma {dataset[nome]['Turma']} está {
                  resultado}. A média final dela foi: {media_ponderada:.2f}.")
        else:
            recuperacao()
            print(f"A aluna {nome} da turma {dataset[nome]['Turma']} está {
                  recup}. A média final dela foi: {media_ponderada:.2f}.")


def obter_dados_aluna(numero_de_aulas):
    print("Insira os seguintes dados")
    nome = input("Nome da aluna: ")  # Recebo nome da aluna
    turma = input("Turma da aluna: ")  # Recebo nome a turma
    lista_presenca = presencas(numero_de_aulas)
    nota_participacao = float(input("Nota de participação da aluna: "))
    notas = obter_notas()

    # notas = obter_notas() #Chamo a função de pegar as notas para alimentar minha lista "notas"

    salvar_dados_aluna(nome, turma, notas, lista_presenca, nota_participacao)

    return nome


def presencas(numero_de_aulas):
    ata = []
    print("\nAgora vamos calcular a presença da estudante")

    for contador in range(numero_de_aulas):
        while True:
            entrada = input(f'Insira a presença da aluna do dia {
                            contador+1} (True ou False): ').strip().lower()
            if entrada == 'true':
                presenca_dia = True
                ata.append(presenca_dia)
                break
            elif entrada == 'false':
                presenca_dia = False
                ata.append(presenca_dia)
                break
            else:
                print("Entrada inválida. Por favor, insira True ou False.")

    valores_true = [i for i in ata if i]
    soma_true = len(valores_true)

    if soma_true >= numero_de_aulas * 0.8:
        lista_presenca = int(soma_true)
        print(f"Soma das presenças: {lista_presenca}")
    else:
        lista_presenca = int(soma_true)
        print("Estudante reprovada por falta.")

    return lista_presenca, numero_de_aulas


def obter_notas():
    # Recebo a quantidade de notas
    quantidade_notas = input("Quantidade de notas: ")
    notas = []  # Criei uma lista para receber as notas

    for contador in range(int(quantidade_notas)):
        # Usamos o for em contagens definidas - o contador vai de 0 até quantidade de notas
        while True:  # Usamos quando não sabemos a quantidade de repetições
            # Para cada nota, insiro o valor - {contador + 1} indica a nota atual
            entrada = input(f"Insira a nota #{contador + 1}: ")
            try:  # Faço uma tentativa de adicionar uma nota na lista
                nota = float(entrada)  # Converto a entrada em float
                notas.append(nota)  # Insiro a nota na minha lista "notas"
                break  # Caso ok, posso sair do loop e seguir com for
            except ValueError:  # Caso dê um problema, ele volta ao início do while e tenta novamente
                print("Entrada inválida. Por favor, insira um número válido.")

    return notas


def salvar_dados_aluna(nome, turma, notas, lista_presenca, nota_participacao):
    chave = (nome)  # Crio uma tupla com o nome
    dataset[chave] = {  # Adiciono no dicionário os dados que peguei na função obter_dados_aluna
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_presenca,
        "Participação": nota_participacao,
    }


def obter_media_ponderada(nome):
    notas = dataset[(nome)]["Notas"]  # Recupera a lista com as notas
    # sum = função do python que soma todos os elementos / len = função que retorna tamanho da lista (quantidade)
    media = float(sum(notas) / len(notas))
    return media


def obter_media_ponderada(nome):
    media_total = obter_media(nome)
    peso_media = 0.8
    peso_participacao = 0.2
    nota_participacao = dataset[(nome)]["Participação"]
    media_ponderada = (media_total * peso_media + nota_participacao *
                       peso_participacao) / (peso_media + peso_participacao)

    return media_ponderada


def obter_media(nome):
    notas = dataset[(nome)]["Notas"]  # Recupera a lista com as notas
    # sum = função do python que soma todos os elementos / len = função que retorna tamanho da lista (quantidade)
    media = float(sum(notas) / len(notas))
    return media


def obter_resultado(nome, media_ponderada, numero_de_aulas):
    lista_presenca, _ = dataset[nome]["Presença"]  # Desempacotar a tupla
    if lista_presenca <= numero_de_aulas * 0.8:  # Retorna reprovada para quantidade de faltas maior que 2
        return "reprovada por falta"
    elif media_ponderada >= 6:
        return "aprovada"
    else:
        return "reprovada"


def recuperacao():
    while True:
        situacao = input("Responda 'sim' ou 'não', você fez a prova de recuperação? ").strip().lower()
        if situacao == "sim":
            nota_rec = float(input("Digite sua nota de recuperação: "))
            print(f'Confirmando a sua nota de recuperação, ela é {nota_rec}.')
            break
        elif situacao == "não":
            return "reprovada"
            break
        else:
            print("Por favor digite 'sim' ou 'não'")


main()
