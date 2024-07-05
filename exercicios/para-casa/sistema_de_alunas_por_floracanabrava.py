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
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 6).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna():
    print("Insira os seguintes dados da aluna: ")
    nome = input("Nome da aluna: ")
    sobrenome = input("Agora, informe o sobrenome da aluna: ")
    while True:
        turma = input ("Informe qual a turma da aluna: ")
        if turma == "Turma A" or turma == "Turma B" or turma == "Turma C":
            break
        else:
            print("Turma inválida. Você deve digitar Turma A, Turma B ou Turma C")

    notas = obter_notas()
    presenca = obter_presenca()
    participacao = float(input("Participação da aluna: "))

    salvar_dados_alunas(nome, sobrenome, turma, notas, presenca, participacao)
    
    return (nome, sobrenome)

def consultar_lista_alunas():

    if not dataset:
        print("Ainda não há alunas cadastradas")
        return
    else:
        for chave in dataset.keys():
            print(f"\nAluna: {chave[0]} {chave[1]}")

def consultar_faltas_aluna():
    nome = input("Por favor, nos informe o nome da aluna: ")
    sobrenome = input("Agora informe o sobrenome da aluna: ")

    qtd_faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
    print(f"A quantidade de faltas de {nome} {sobrenome} é {qtd_faltas}.")

    
def consultar_notas_aluna():
    pass
    #TODO - Implentar a função
    
def consultar_status_aprovacao():
    pass
    #TODO - Implentar a função

def obter_notas():
    quantidade_notas = 3
    notas = []

    for contador in range(int(quantidade_notas)):
        while True:
            try:
                entrada = float(input(f"Insira a nota #{contador + 1}: "))
                if entrada < 0 or entrada > 10:
                    print("Entrada inválida. Você deve inserir um número entre 0 e 10.")
                else:
                    notas.append(entrada)
                    break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")

    return notas 

def obter_presenca():
    quantidade_aulas = 5
    aulas = [] 

    for contador in range(int(quantidade_aulas)):
        while True:
            entrada = input(f"Insira a presença da aula #{contador + 1}: ")
            try:
                presenca = eval(entrada)
                if isinstance(presenca, bool):
                    aulas.append(presenca)
                    break 
                else:
                    print("Entrada inválida. Por favor utilize True para presente e False para ausente.")
            except NameError:
                print("Entrada inválida. Por favor, insira True ou False.")

    return aulas 
   

def salvar_dados_alunas(nome, sobrenome, turma, notas, presenca, participacao):
    chave = (nome, sobrenome)
    dataset[chave] = {
        (nome, sobrenome):{
           "Turma": turma,
           "Notas": notas,
           "Presença": presenca,
           "Participação": participacao
    },}


    print("Aluna inclusa!") 


main()