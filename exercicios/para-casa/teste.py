from dataset_alunas import dataset

dataset

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")

    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1:
            incluir_nova_aluna()
        elif cod_opcao == 2:
            consultar_lista_alunas()
        elif cod_opcao == 3:
            consultar_faltas_aluna()
        elif cod_opcao == 4:
            consultar_notas_aluna()
        elif cod_opcao == 5:
            consultar_status_aprovacao()
        elif cod_opcao == 6:
            print("Encerrando o programa...")
            break

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
    nome = str(input("Nome da aluna: ")) #Recebo nome da aluna
    sobrenome = str(input("Sobrenome da aluna: ")) #Recebo sobrenome da aluna
    turma = int(input("Turma da aluna (nº): ")) #Recebo nome a turma
    lista_notas = (input('Digite as notas da aluna separadas por vírgula: '))
    lista_presenca = bool(input('Digite True para a presença da aluna e False para a sua ausência: '))    
    nota_participacao = (input("Participação da aluna: ")) #Recebo nota de participação
    print('Aluna adicionada com sucesso!' )
    
    
    # Armazeno os dados da aluna no dicionário dataset
    dataset[nome] = {
        'sobrenome': sobrenome,
        'turma': turma,
        'lista_presenca': lista_presenca,
        'lista_notas': lista_notas,
        'nota_participacao': nota_participacao
    }
    print('Aluna adicionada com sucesso!')

def consultar_lista_alunas():
    lista_alunas = dataset
    print(lista_alunas.keys())
    return lista_alunas

def consultar_faltas_aluna():
    nome = str(input("Nome da aluna: ")) #Recebo nome da aluna
    sobrenome = str(input("Sobrenome da aluna: ")) #Recebo sobrenome da aluna    
    if (nome, sobrenome) in dataset:
        faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
        percentual_presenca = faltas / len(dataset[(nome, sobrenome)]["Presença"])
        percentual_presenca >=  80
        print(f'Faltas de {nome}: {faltas}')
        return percentual_presenca
    else:
        print('Aluna não encontrada')   
   
def consultar_notas_aluna():
    nome = str(input('Nome da aluna: '))
    sobrenome = str(input('Sobrenome da aluna: '))
    notas = dataset[(nome, sobrenome)]['Notas']
    if (nome, sobrenome) in dataset:
        media = sum(notas) / len(notas)
        print(f'Notas da {nome}: {notas}')
        return media
    else:
        print('Aluna não encontrada')   
    
def consultar_status_aprovacao():
    nome = str(input('Nome da aluna: '))
    sobrenome = str(input('Sobrenome da aluna: '))
    if (nome, sobrenome) in dataset:
        notas = dataset[(nome, sobrenome)]['Notas']           
        faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
        participacao = dataset[(nome, sobrenome)]["Participação"]
        media = (sum(notas)) / len(notas) 
        percentual_presenca = faltas / len(dataset[(nome, sobrenome)]["Presença"])
             
        media >= 6 and faltas >=80 and participacao >= 6             
        print(f'Média: {media}, Percentual de presença: {faltas}% e Participação: {participacao} - Situação da aluna {nome}: APROVADA!!!')
    else:
        print(f'Média: {media:.2f},\n Percentual de presença: {faltas}% \nParticipação: {participacao} - Situação da aluna {nome}: REPROVADA.')


main()