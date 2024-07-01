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
    
def incluir_nova_aluna():
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") #Recebo nome da aluna
    sobrenome = input("Sobrenome da aluna: ") #Recebo sobrenome da aluna
    turma = input("Turma da aluna (nº): ") #Recebo nome a turma
    #lista_presenca = obter_presenca() #Recebo a lista de presença com 'True' ou 'False'
    #lista_notas = obter_notas() #Chamo a função de pegar as notas para alimentar minha lista "notas"
    nota_participacao = float(input("Participação da aluna: ")) #Recebo nota de participação
    proximo = (input("ATENÇÃO: PRIMEIRO COMMIT - ainda faltam parrtes por implementar!"))
    #salvar_dados_aluna(nome, turma, lista_notas, lista_presenca, nota_participacao)
    salvar_dados_aluna(nome, turma, nota_participacao)
    
    return nome

def salvar_dados_aluna(nome, turma, notas, nota_participacao):
    chave = (nome) #Crio uma tupla com o nome
    dataset[chave] = { #Adiciono no dicionário os dados que peguei na função obter_dados_aluna
        "Turma": turma,
        "Notas": notas,
        "Participação": nota_participacao
    }
#print(consultar_lista_alunas)
def consultar_lista_alunas():
    pass
    #TODO - Implentar a função
    
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