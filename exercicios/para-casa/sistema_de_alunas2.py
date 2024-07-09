from dataset_alunas2 import dataset

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1: incluir_nova_aluna()
        elif cod_opcao == 2: consultar_lista_aluna()
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
    
def incluir_nova_aluna():
    try:
        aluna = input("Insira o nome da aluna nova:")
        incluir_nova_aluna.append(aluna) 
    except NameError:
        print("Entrada inválida. Por favor, insira o nome da aluna nova.")

    pass
    
    
def consultar_faltas_aluna():
    nome = input("Nome da aluna:")
    sobrenome = input("Sobre nome da aluna:")

    dados = f"{nome} {sobrenome}"
    if dados in dataset:
        faltas = dataset[dados]["Presença"].count(False)
        print(f"A aluna {nome} {sobrenome} possui {faltas} faltas.")
    else:
        print("Opção invalida. Tente novamente.")
    pass
    
def consultar_notas_aluna():
    nome = input("Nome da aluna:")
    sobrenome = input("Sobrenome da aluna:")

    dados = f"{nome} {sobrenome}"
    if dados in dataset:
        notas = dataset[dados]["Notas"]
        print(f"As notas da aluna {nome} {sobrenome} são:{notas}")
    else:
        print("Aluna não encontrada.")
    pass
   
def consultar_lista_aluna():
    nome = input("Nome da aluna:")
    sobrenome = input("Sobrenome da aluna:")

    dados = f"{nome} {sobrenome}"
    if dados in dataset:
        consultar_lista_aluna = dataset[dados]["Lista"]
        print(f"A lista de alunas {nome} {sobrenome} é:{consultar_lista_aluna}")
    else:
        print("Aluna não encontrada.")
    pass
    
def consultar_status_aprovacao():
    nome = input("Nome da aluna:")
    sobrenome = input("Sobrenome da aluna:")

    qtd_faltas = dataset[(nome, sobrenome)]["Presença"].count(False) 
    if qtd_faltas > 2: 
        return "Reprovada"
    elif qtd_faltas < 6:
        return "Reprovada"
    else:
        return "Aprovada"
    pass
   
    
