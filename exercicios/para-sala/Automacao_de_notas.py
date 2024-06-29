dataset = {} #Dicionario com escopo global

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---\n")
    print("Aqui você pode calcular a aprovação de uma aluna.\n")

    while True:
        nome = obter_dados_aluna() #Chamo a função de pegar dados da aluna
        media_ponderada = obter_media_ponderada(nome) #Chamo a função de calcular a média da aluna
        resultado = obter_resultado(nome, media_ponderada) #Chamo a função para obter resultado
        
        print(f"A aluna {nome} da turma {dataset[(nome)]["Turma"]} está {resultado}. A média dela foi: {media_ponderada}.")
        
def obter_dados_aluna():
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") #Recebo nome da aluna
    turma = input("Turma da aluna: ") #Recebo nome a turma
    lista_presenca = obter_presenca() #Recebo a lista de presença com 'True' ou 'False'
    nota_participacao = float(input("Participação da aluna: ")) #Recebo nota de participação
    notas = obter_notas() #Chamo a função de pegar as notas para alimentar minha lista "notas"
    
    salvar_dados_aluna(nome, turma, notas, lista_presenca, nota_participacao)
    
    return nome

def obter_presenca():
    quantidade_aulas = input("Quantidade de aulas: ") #Recebo a quantidade de aulas
    aulas = [] #Criei uma lista para receber a presença
    
    for contador in range(int(quantidade_aulas)): 
        #Usamos o for em contagens definidas - o contador vai de 0 até quantidade de aulas
        while True: #Usamos quando não sabemos a quantidade de repetições    
            entrada = input(f"Insira a presença da aula #{contador + 1}: ") #Para cada nota, insiro o valor - {contador + 1} indica a aula atual
            try: #Faço uma tentativa de adicionar uma nota na lista
                presenca = eval(entrada) #Valido se entrada é booleana
                aulas.append(presenca) #Insiro a aula na minha lista "aulas"
                break #Caso ok, posso sair do loop e seguir com for
            except ValueError: #Caso dê um problema, ele volta ao início do while e tenta novamente
                print("Entrada inválida. Por favor, insira True ou False.")
   
    return aulas

def obter_notas():
    quantidade_notas = input("Quantidade de notas: ") #Recebo a quantidade de notas
    notas = [] #Criei uma lista para receber as notas
    
    for contador in range(int(quantidade_notas)): 
        #Usamos o for em contagens definidas - o contador vai de 0 até quantidade de notas
        while True: #Usamos quando não sabemos a quantidade de repetições    
            entrada = input(f"Insira a nota #{contador + 1}: ") #Para cada nota, insiro o valor - {contador + 1} indica a nota atual
            try: #Faço uma tentativa de adicionar uma nota na lista
                nota = float(entrada) #Converto a entrada em float
                notas.append(nota) #Insiro a nota na minha lista "notas"
                break #Caso ok, posso sair do loop e seguir com for
            except ValueError: #Caso dê um problema, ele volta ao início do while e tenta novamente
                print("Entrada inválida. Por favor, insira um número válido.")
    
    return notas

def salvar_dados_aluna(nome, turma, notas, lista_presenca, nota_participacao):
    chave = (nome) #Crio uma tupla com o nome
    dataset[chave] = { #Adiciono no dicionário os dados que peguei na função obter_dados_aluna
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_presenca,
        "Participação": nota_participacao
    }

def obter_media_ponderada(nome):
    media_total = obter_media(nome) #Calculo media
    peso_media = 0.8 #Coloco o peso das notas
    peso_participacao = 0.2 #Coloco o peso de participação
    nota_participacao = dataset[(nome)]["Participação"] #Recupero a nota de participação
    media_ponderada = (media_total * peso_media + nota_participacao * peso_participacao) / (peso_media + peso_participacao) #Calculo a media ponderada

    return media_ponderada

def obter_media(nome):
    notas = dataset[(nome)]["Notas"] #Recupera a lista com as notas
    media = float(sum(notas)/len(notas)) #sum = função do python que soma todos os elementos / len = função que retorna tamanho da lista (quantidade)
    return media

def obter_resultado(nome, media):
    qtd_faltas = dataset[(nome)]["Presença"].count(False) #Count conta a quantidade de vezes que o False aparece na lista
    if qtd_faltas > 2: #Retorna reprovada para quantidade de faltas maior que 2
        return "Reprovada"
    elif media >= 6:
        return "Aprovada"
    elif media >=4:
        return "Recuperação"
    else:
        return "Reprovada"

main()
