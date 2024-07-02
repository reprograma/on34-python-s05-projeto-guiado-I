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
       # elif cod_opcao == 5: consultar_status_aprovacao()
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
    nome = input("Nome da aluna: ") #Recebo nome da aluna
    sobrenome = input("Sobrenome da aluna: ") #Recebo sobrenome da aluna
    turma = input("Turma da aluna (nº): ") #Recebo nome a turma
    #lista_presenca = consultar_faltas_aluna() #Recebo a lista de presença com 'True' ou 'False'
    #lista_notas = consultar_notas_aluna() #Chamo a função de pegar as notas para alimentar minha lista "notas"
    nota_participacao = float(input("Participação da aluna: ")) #Recebo nota de participação
    
    #salvar_dados_aluna(nome, sobrenome, turma, nota_participacao)
    print('Aluna adicionada com sucesso!' )
    
    return nome

incluir_nova_aluna()
nova_aluna = incluir_nova_aluna




def consultar_faltas_aluna():
    quantidade_aulas = input("Quantidade de aulas: ") #Recebo a quantidade de aulas
    aulas = [] #Criei uma lista para receber a presença
    
    for contador in range(int(quantidade_aulas)):
        while True:    
            presenca = input(f"Insira a presença da aula #{contador + 1}: ")        
            try: #Faço uma tentativa de adicionar uma nota na lista
                chamada = bool(presenca) #Valido se entrada é booleana
                aulas.append(presenca) #Insiro a aula na minha lista "aulas"                
                break #Caso ok, posso sair do loop e seguir com for
            except ValueError: #Caso dê um problema, ele volta ao início do while e tenta novamente
                        print("Entrada inválida. Por favor, insira True ou False.")
                    
    print(aulas)
         
consultar_faltas_aluna()

def consultar_notas_aluna():
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

    print(notas)          
    return notas

consultar_notas_aluna()

def consultar_lista_alunas():
    if incluir_nova_aluna == True:
        print(incluir_nova_aluna)
    else:
        print('Não há registros.')

consultar_lista_alunas()

main()