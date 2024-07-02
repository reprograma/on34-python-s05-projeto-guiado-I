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


        if resultado == "aprovada" or resultado == "reprovada por falta" or resultado == "reprovada":
            print(f"A aluna {nome} da turma {dataset[nome]['Turma']} está {resultado}. A média final dela foi: {media_ponderada:.2f}.")
        else:
            fez_recuperacao = obter_recuperacao(nome) #Verifica se a aluna fez prova de recuperação
            if fez_recuperacao == True:
                 newresultado = calcular_recuperacao(nome, numero_de_aulas)
            else:
                newresultado = "reprovada"

            print(f"A aluna {nome} da turma {dataset[nome]['Turma']} está {newresultado}. A média final dela foi: {obter_media_ponderada(nome):.2f}.")


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
    
    if media_ponderada < 6:
        if media_ponderada >= 4:
            return "em recuperação"
        else:
            return "reprovada"
    else:
        return "aprovada"
        
def resultado_da_final(media_ponderada):
    if media_ponderada < 6:
        return "reprovada na final"
    else:
        return "aprovada na final"

def obter_recuperacao(nome):
    while True:
        situacao = input("Responda 'sim' ou 'não', você fez a prova de recuperação? ").strip().lower()
        if situacao == "sim":
            nota_rec = float(input("Digite sua nota de recuperação: "))
            print(f'Confirmando a sua nota de recuperação, ela é {nota_rec}.')
            dataset[(nome)]['Recuperação'] = nota_rec #salvar nota de recuperação
            return True
        else:
            return False

def calcular_recuperacao(nome, numero_de_aulas):
    notas = dataset[(nome)]['Notas'] #recuperando a lista de notas
    nota_rec =  dataset[(nome)]['Recuperação']
    menor_nota = min(notas) #menor nota da lista de notas que será substituida pela nota de recuperação

    if menor_nota < nota_rec:
        for indice in range(len(notas)):
            if notas[indice] == menor_nota:
                notas[indice] = nota_rec
                break #para logo após fazer essa troca uma vez
            dataset[(nome)]["Notas"] = notas

    nova_media = obter_media_ponderada(nome)
    novo_resultado = resultado_da_final(nova_media)

    return novo_resultado




main()
