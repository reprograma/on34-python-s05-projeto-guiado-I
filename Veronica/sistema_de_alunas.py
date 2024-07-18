from dataset_alunas import dataset

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

    while codigo_opcao not in [1, 2, 3, 4, 5]:
        try:
            codigo_opcao = int(input("\nEscolha uma opção:\n"
                                    "1 - Incluir uma nova aluna\n"
                                    "2 - Consultar lista de alunas\n"
                                    "3 - Consultar faltas da aluna\n"
                                    "4 - Consultar notas da aluna\n"
                                    "5 - Consultar status de aprovação\n"
                                    "6 - Sair do sistema\n"
                                    "Opção: "))
                
            if codigo_opcao not in [1, 2, 3, 4, 5]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna(dataset): #Pegando os dados: nome, sobrenome, turma, notas presença e participação 
    try:
        nome = input("Digite o nome da aluna... ")
    except ValueError:
        print("Entrada invalida, digite apenas o nome... ")

    try:
        sobrenome = input("Digite o sobrenome da aluna... ")
    except ValueError:
        print("Entrada invalida, digite apenas o sobrenome... ")

    try:
        turma = input("Digite a turma que a aluna pertence...")
    except ValueError:
        print("Entrada invalida, digite apenas a turma... ")

    try:
        notas = input("Digite as notas da aluna separadas por espaço... ")
    except ValueError:
        print("Entrada invalida, digite as notas separadas por espaço... ")

    try:
        presenca = input("Indique a presença da aluna utilizando: A para ausente e P para presente separando por espaço... ")
    except ValueError:
        print("Entrada invalida, digite A para ausente, e P para presente... ")

    try:
        participacao = input("Digite a nota de participação da aluna... ")
    except ValueError:
        print("Entrada invalida digite apenas uma nota de participação para aluna... ")

#TRATAMENTO DE DADOS


#Pegando notas digitadas como strings e convertendo para lista de strings
    notas = notas.split(" ")


#Covertendo lista str para Lista int
    notas_int = []
    for nota in notas:
        notas_int.append(int(nota)) #pegando todas as string notas do professor e convertendo para numero inteiro
    notas = notas_int


#Convertendo presenças A e P para booleanos
    presenca = presenca.split(" ")
    presenca_convertida = []
    for A_P in presenca:
        if A_P == "A":
            presenca_convertida.append(False)
        elif A_P == "P":
            presenca_convertida.append(True)
        else:
            presenca_convertida.append("Presença invalida.")

    presenca = presenca_convertida


#Inclusão da aluna no dataset

    dataset[nome, sobrenome] = {"Turma": turma, "Notas": notas, "Presença": presenca, "Participação": participacao}

def consultar_lista_alunas(dataset):
    chaves = list(dataset.keys()) #Pegando as chaves do dicionario

    for aluna in chaves:
        print("Aluna: ", aluna[0], aluna[1]) #Print aluna: (nome e sobrenome da aluna)

def consultar_faltas_aluna(dataset):
    nome_aluna_escolhida = input("Digite o nome e o sobrenome da alunas que querira consultar as faltas: ")
    nome_aluna = tuple(nome_aluna_escolhida.split(" ")) #Pegando a string com nome e sobrenome e convertendo em uma tupla

    presenca = dataset[nome_aluna]["Presença"]
    n_faltas = 0
    n_presencas = 0

    for pren in presenca:
        if pren == False: n_faltas += 1
        else: n_presencas += 1
    print("A aluna", nome_aluna_escolhida, "tem", n_faltas, "faltas.")

    porcentagem_presenca = (n_presencas / (n_faltas + n_presencas)) * 100

    return porcentagem_presenca

def consultar_notas_aluna(dataset):
    nome_aluna_escolhida = input("Digite o nome e o sobrenome da alunas que querira consultar as faltas: ")
    nome_aluna = tuple(nome_aluna_escolhida.split(" ")) #Pegando a string com nome e sobrenome e converte em uma tupla

    notas = dataset[nome_aluna]["Notas"]
    avaliacao = 1
    print("A aluna", nome_aluna_escolhida, "teve às seguintes notas:")
    for nota in notas:
        print("Avaliação:", avaliacao, "Nota:", nota)
        avaliacao += 1

    return notas

def consultar_status_aprovacao():
    nome_aluna_escolhida = input("Digite o nome e sobrenome da aluna que queira consultar o status de aprovação: ")
    nome_aluna = tuple(nome_aluna_escolhida.split(" ")) #Pegando a string com nome e sobrenome e converte em uma tupla

    nota_corte = 6

    print("Para sabermos o status de aprovação da aluna vamos ter que consultar sua nota, participação e presença em aulas")
    print("Vamos começar pela nota.")

    notas = consultar_notas_aluna(dataset) #Chamando a função para consultar as notas da aluna
    media_notas = sum(notas) / len(notas) #Calculando a média: com a somas das notas, dividido pelo numero de notas

    print("Agora sua participação.")
    participacao = dataset[nome_aluna]["Participação"]
    print("A aluna", nome_aluna_escolhida, "teve nota", participacao, "de participação.")

    print("Por ultimo a presença.")
    porcentagem_presenca = consultar_faltas_aluna(dataset)
    print("A aluna", nome_aluna_escolhida, "teve", int(porcentagem_presenca), "% de presença.")

    print("")

    if media_notas >= 6 and porcentagem_presenca >= 80 and participacao >= 6:
        print("A aluna", nome_aluna_escolhida, "esta aprovada.")
    else: print("A aluna", nome_aluna_escolhida, "esta reprovada.")



main()