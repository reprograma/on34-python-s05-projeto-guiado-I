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
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna():
    pass
    from dataset_alunas import dataset
    nome_completo = input("\nDigite o nome completo da nova aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    turma = input("Digite a turma da aluna: ")
    


    
def consultar_lista_alunas():
    pass
    if  dataset :
        print("\n Lista de Alunas Cadastradas:") 
    for idx, aluna in enumerate(dataset ):
            print(f"{idx}. {aluna['nome']} {aluna['sobrenome']} - Turma: {aluna['turma']}")
    else:
        print("\n não cadastrada:")
        
    
def consultar_faltas_aluna():
    nome= input("por favor, nos informe o nome da aluna: ")
    sobrenome= input(" agora  nos informe o sobrenome da aluna :")

    qtd_faltas = dataset[(nome, sobrenome)] ["presença"].count(False)
    print((f"A quantidade de faltas de {nome} {sobrenome} são {qtd_faltas[0]}, {qtd_faltas[1]}, {qtd_faltas[2]} "))
    pass
    #TODO - Implentar a função
    
def consultar_notas_aluna():
    nome = input("por favor, nos informe o nome da aluna: ")
    sobrenome= input(" agora  nos informe o sobrenome da aluna :")
    valor_notas = dataset[(nome, sobrenome )] ["notas"]
    print(f"As três notas de {nome} {sobrenome} é {valor_notas}. ")
    pass
    #TODO - Implentar a função
    
def consultar_status_aprovacao():
    pass
    #TODO - Implentar a função
    

main()