dataset = {} #Dicionario com escopo global

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---\n")
    print("Aqui você pode calcular a aprovação de uma aluna.\n")
    
    while True:
        nome = obter_dados_aluna() #Chamo a função de pegar dados da aluna
        media_ponderada = obter_media_ponderada(nome)
        resultado = obter_resultado(nome, media_ponderada)

        if resultado == "Em recuperação":
            calcula_recuperacao(nome)
        
        print(f"A aluna {nome} da turma {dataset[(nome)]["Turma"]} está {resultado}. A média dela foi: {media_ponderada}.")
            
    
def obter_dados_aluna():
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") #Recebo nome da aluna
    turma = input("Turma da aluna: ") #Recebo nome a turma
    
    notas = obter_notas() #Chamo a função de pegar as notas para alimentar minha lista "notas"
    presencas = obter_presenca()
    nota_participacao = float(input("Insira a nota de participação da aluna: "))
    
    salvar_dados_aluna(nome, turma, notas, presencas, nota_participacao)
    
    return nome
    
def obter_notas():
    quantidade_notas = input("Quantidade de notas: ") #Recebo a quantidade de notas
    notas = [] #Criei uma lista para receber as notas
    
    for contador in range(int(quantidade_notas)): 
        while True:    
            entrada = input(f"Insira a nota #{contador + 1}: ") 
            try: 
                nota = float(entrada) 
                notas.append(nota) 
                break 
            except ValueError: 
                print("Entrada inválida. Por favor, insira um número válido.")
    
    return notas

def salvar_dados_aluna(nome, turma, notas, presencas, nota_participacao):
    chave = (nome) #Crio uma tupla com o nome
    dataset[chave] = { #Adiciono no dicionário os dados que peguei na função obter_dados_aluna
        "Turma": turma,
        "Notas": notas,
        "Presenças": presencas,
        "Participação": nota_participacao
    }

def obter_media_ponderada(nome):
    media_total = obter_media(nome)
    peso_media = 0.8
    peso_participacao = 0.2
    nota_participacao = dataset[(nome)]["Participação"]
    media_ponderada = media_total * peso_media + nota_participacao * peso_participacao
    return media_ponderada
    
def obter_media(nome):
    notas = dataset[(nome)]["Notas"] #Recupera a lista com as notas
    media = float(sum(notas)/len(notas)) #sum = função do python que soma todos os elementos / len = função que retorna tamanho da lista (quantidade)
    return media

def obter_resultado(nome, media_ponderada):
    qtd_faltas = dataset[(nome)]["Presenças"].count(False)
    percentual_faltas = (qtd_faltas / len(dataset[(nome)]["Presença"])) * 100
    if percentual_faltas > 20:
        return "Reprovada por falta"
    elif media_ponderada >= 6:
        return "Aprovada"
    elif media_ponderada >= 4:
        return "Em recuperação"
    else:
        return "Reprovada"
    
def obter_presenca():
    quantidade_presenca = input("Informe a quantidade de aulas para que a presença possa ser computada: ")
    presencas = []
    for i in range(int(quantidade_presenca)):
        entrada = input(f"A aluna esteve presente na aula {i+1}? Responda Presente ou Ausente: ")
        if entrada == "Presente":
            presencas.append(True)
        elif entrada == "Ausente":
            presencas.append(False)
        else:
            print("Opção inválida. Você deve escrever Presente ou Ausente")
    return presencas

def calcula_recuperacao(nome):
    recuperacao = input("Aluna fez prova de recuperação? S/N: ")
    if recuperacao == "S":
        nota_recuperacao = float(input("Insira a nota da prova de recuperação: "))
        dataset[(nome)]["Recuperação"] = True
        dataset[(nome)]["Nota de recuperação"] = nota_recuperacao
        substitui_nota(nome)
    else:
        dataset[(nome)]["Recuperação"] = False

def substitui_nota(nome):
    if dataset[(nome)]["Nota de recuperação"] > min(dataset[(nome)]["Notas"]):
        lista_notas = dataset[(nome)]["Notas"]
        indice_min = lista_notas.index(min(lista_notas))
        lista_notas[indice_min] = dataset[(nome)]["Nota de recuperação"]
    nova_media = obter_media_ponderada(nome)
    novo_resultado = obter_resultado(nome, nova_media)
    return novo_resultado
main()