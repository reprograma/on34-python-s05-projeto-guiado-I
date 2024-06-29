dataset = {} #Dicionario com escopo global

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---\n")
    print("Aqui você pode calcular a aprovação de uma aluna.\n")
    
    while True:
        nome = obter_dados_aluna() #Chamo a função de pegar dados da aluna
        media = obter_media(nome) #Chamo a função de calcular a média da aluna
        resultado = obter_resultado(media)
        
        print(f"A aluna {nome} da turma {dataset[(nome)]["Turma"]} está {resultado}. A média dela foi: {media}.")
    
def obter_dados_aluna():
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") #Recebo nome da aluna
    turma = input("Turma da aluna: ") #Recebo nome a turma
    
    notas = obter_notas() #Chamo a função de pegar as notas para alimentar minha lista "notas"
    
    salvar_dados_aluna(nome, turma, notas)
    
    return nome
    
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

def salvar_dados_aluna(nome, turma, notas):
    chave = (nome) #Crio uma tupla com o nome
    dataset[chave] = { #Adiciono no dicionário os dados que peguei na função obter_dados_aluna
        "Turma": turma,
        "Notas": notas,
    }
    
def obter_media(nome):
    notas = dataset[(nome)]["Notas"] #Recupera a lista com as notas
    media = float(sum(notas)/len(notas)) #sum = função do python que soma todos os elementos / len = função que retorna tamanho da lista (quantidade)
    return media

def obter_resultado(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

main()