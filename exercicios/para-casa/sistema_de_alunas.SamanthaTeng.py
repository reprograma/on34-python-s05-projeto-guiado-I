from dataset_alunas import dataset
dataset = {} #Dicionario com escopo global
def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1: incluir_nova_aluna()
        elif cod_opcao == 2: consultar_lista_alunas()
        elif cod_opcao == 3: consultar_faltas_aluna()
        elif cod_opcao == 4: consultar_notas_aluna()
        elif cod_opcao == 5: consultar_status_aprovacao()
        elif cod_opcao == 6: print("Encerrando o programa..."); break

def obter_opcao():
    codigo_opcao = 0

    while codigo_opcao not in [1, 2, 3, 4, 5, 6]:
        try:
            codigo_opcao = int(input("\nEscolha uma opção:\n"
                                    "1 - Incluir uma nova aluna\n"
                                    "2 - Consultar lista de alunas\n"
                                    "3 - Consultar faltas da aluna\n"
                                    "4 - Consultar notas da aluna\n"
                                    "5 - Consultar status de aprovação\n"
                                    "6 - Sair do sistema\n"
                                    "Opção: "))
                
            if codigo_opcao not in [1, 2, 3, 4, 5, 6]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao

def incluir_nova_aluna():
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") 
    sobrenome = input ("Sobrenome: ")
    turma = input("Turma da aluna: ") 
    lista_presenca = obter_presenca() 
    nota_participacao = float(input("Participação da aluna: "))
    notas = obter_notas() 
    salvar_dados_aluna(nome,sobrenome, turma, notas, lista_presenca, nota_participacao) 
    return nome


def obter_presenca():
    quantidade_aulas = input("Quantidade de aulas: ") 
    aulas = [] 
    
    for contador in range(int(quantidade_aulas)): 
        
        while True:    
            entrada = input(f"Insira a presença da aula #{contador + 1}: ") 
            try: 
                presenca = eval(entrada) 
                aulas.append(presenca) 
                break 
            except NameError: 
                print("Entrada inválida. Por favor, insira True ou False.")
   
    return aulas
    
def obter_notas():

    quantidade_notas = input("Quantidade de notas: ") 
    notas = [] 
    
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

def salvar_dados_aluna (nome,sobrenome, turma, notas, lista_presenca, nota_participacao):
    chave = (nome) 
    dataset[chave] = { 
        "Sobrenome": sobrenome,
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_presenca,
        "Participação": nota_participacao
    }
    print ("Aluna foi adicionada no sistema com sucesso!")

    
def consultar_lista_alunas():
    print ("Os nomes inseridos foram:")
    for key in dataset.keys():
        print(key)
    
def consultar_faltas_aluna():
    nome = input("Insira o nome da aluna: ")
    sobrenome = input("Insira o sobrenome da aluna: ") 
    nome_completo = dataset[nome]['Sobrenome']
    if sobrenome != nome_completo:
        print("Aluna não encontrada")
        return ValueError
    nome_completo = nome + ' ' + nome_completo
    faltas = dataset[nome]['Presença']
    contador = 0
    for f in faltas:
        if not f:
            contador += 1
    faltas = str(contador)
    print('nome completo: ' + nome_completo + ' ' + 'quantidade de faltas: ' + faltas)

    #TODO - Implentar a função
    
def consultar_notas_aluna():
    nome = input("Insira o nome da aluna: ")
    sobrenome = input("Insira o sobrenome da aluna: ") 
    nome_completo = dataset[nome]['Sobrenome']
    if sobrenome != nome_completo:
        print("Aluna não encontrada")
        return ValueError
    nome_completo = nome + ' ' + nome_completo
    notas = dataset[nome]['Notas']
    print('nome completo: ' + nome_completo + ' ' + 'Notas da aluna: ' + str(notas))
    #TODO - Implentar a função
    
def consultar_status_aprovacao():
    nome = input("Insira o nome da aluna: ")
    sobrenome = input("Insira o sobrenome da aluna: ") 
    nome_completo = dataset[nome]['Sobrenome']
    if sobrenome != nome_completo:
        print("Aluna não encontrada")
        return ValueError
    nota_participação = dataset[nome]['Participação']
    nome_completo = nome + ' ' + nome_completo
    media = obter_media_ponderada(nome)
    resultado_participação = obter_resultado(nome, nota_participação)
    print(nome_completo + ' media da aluna: ' + str(media) + ' Status da aprovação: ' + resultado_participação)

    
def obter_media(nome):
    notas = dataset[(nome)]["Notas"] #Recupera a lista com as notas
    media = float(sum(notas)/len(notas)) #sum = função do python que soma todos os elementos / len = função que retorna tamanho da lista (quantidade)
    return media
    #TODO - Implentar a função

def obter_resultado(nome, nota_participacao):

    qtd_faltas = dataset[(nome)]["Presença"].count(False) #Count conta a quantidade de vezes que o False aparece na lista
    qtd_aulas = len(dataset[(nome)]["Presença"])
    percentual_de_faltas = (qtd_faltas / qtd_aulas) * 100
    
    if percentual_de_faltas > 20: #Retorna reprovada para quantidade de faltas maior que 2
        return "Reprovada por falta"
    
    if nota_participacao >= 6:
        return "Aprovada"
    else:
           return "Reprovada"

def obter_media_ponderada(nome):
    media_total = obter_media(nome) #Calculo media
    peso_media = 0.8 #Coloco o peso das notas
    peso_participacao = 0.2 #Coloco o peso de participação
    nota_participacao = dataset[(nome)]["Participação"] #Recupero a nota de participação
    media_ponderada = (media_total * peso_media + nota_participacao * peso_participacao) / (peso_media + peso_participacao) #Calculo a media ponderada
    
    return media_ponderada

main()