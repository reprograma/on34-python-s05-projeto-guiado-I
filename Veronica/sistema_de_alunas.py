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
    chaves = list(dataset.keys()) #Pega as chaves do dicionario

    for aluna in chaves:
        print("Aluna: ", aluna[0], aluna[1]) #Printa Aluna: (nome e sobrenome da aluna)

def consultar_faltas_aluna():
    pass
    #TODO - Implentar a função
    
def consultar_notas_aluna():
    pass
    #TODO - Implentar a função
    
def consultar_status_aprovacao():
    pass
    #TODO - Implentar a função
    

main()