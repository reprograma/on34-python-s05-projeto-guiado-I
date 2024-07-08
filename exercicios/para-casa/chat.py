from dataset_alunas import dataset
dataset

def main():
    print("\n---  Seja bem vinda à Escola do Reprograma!  ---")
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
    nome = str(input("Nome da aluna: ")) # Recebo nome da aluna
    sobrenome = str(input("Sobrenome da aluna: ")) # Recebo sobrenome da aluna
    turma = int(input("Turma da aluna (nº): ")) # Recebo a turma
    lista_presenca = input("Lista de presença (separada por vírgulas, com 'True' ou 'False'): ").split(',') # Recebo a lista de presença
    lista_presenca = [presenca.strip().lower() == 'true' for presenca in lista_presenca]
    lista_notas = [float(nota) for nota in input("Lista de notas (separada por vírgulas): ").split(',')] # Recebo a lista de notas
    nota_participacao = float(input("Participação da aluna: ")) # Recebo nota de participação

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
    if not dataset:
        print("Nenhuma aluna cadastrada.")
        return
    
    print("\nLista de Alunas:")
    # Percorro o dicionário dataset e exibo os dados das alunas
    for nome, dados in dataset.items():
        print(f"Nome: {nome}, Sobrenome: {dados['sobrenome']}, Turma: {dados['turma']}")
        
def consultar_faltas_aluna():
    nome = str(input('Digite o nome da Aluna: '))
    # Verifico se o nome da aluna está no dataset
    if nome in dataset:
        faltas = dataset[nome]['lista_presenca']
        print(f"Faltas de {nome}: {faltas}")
    else:
        print("Aluna não encontrada.")

def consultar_notas_aluna():
    nome = str(input('Digite o nome da Aluna: '))
    # Verifico se o nome da aluna está no dataset
    if nome in dataset:
        notas = dataset[nome]['lista_notas']
        print(f"Notas de {nome}: {notas}")
    else:
        print("Aluna não encontrada.")

def consultar_status_aprovacao():
    nome = str(input('Digite o nome da Aluna: '))
    # Verifico se o nome da aluna está no dataset
    if nome in dataset:
        dados = dataset[nome]
        media_notas = sum(dados['lista_notas']) / len(dados['lista_notas'])
        presencas = sum(dados['lista_presenca']) / len(dados['lista_presenca'])
        participacao = dados['nota_participacao']

        status_aprovacao = "Aprovada" if media_notas >= 7 and presencas >= 0.75 and participacao >= 7 else "Reprovada"
        print(f"Status de aprovação de {nome}: {status_aprovacao}")
    else:
        print("Aluna não encontrada.")

main()