### Exercico Casa/S05 - sem "opcional" sugerido pelo desafio.

from dataset_alunas import dataset
dataset.keys

def main():
    print("\n---  Seja bem-vinda à Escola do Reprograma!  ---")
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
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 6).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")

    return codigo_opcao

def incluir_nova_aluna():
    nome, sobrenome = nome_aluna()
    turma = input("Qual a turma da aluna?: ")
    notas = notas_aluna()
    presencas = presenca_das_alunas()
    participacao = participacao_alunas()

    dataset[(nome, sobrenome)] = {
        "Turma": turma,
        "Notas": notas,
        "Presenca": presencas,
        "Participacao": participacao
    }

    print(f"A aluna {nome} {sobrenome} foi adicionada à turma {turma}!")

def nome_aluna():
    while True:
        try:
            nome_sobrenome = input("Qual o nome e sobrenome da nova aluna?: ")
            nome, sobrenome = nome_sobrenome.split(' ')
            break
        except ValueError:
            print("Digite um NOME e um SOBRENOME separado por espaço")
    return nome, sobrenome

def notas_aluna():
    quantidade_notas = int(input("Qual a quantidade de notas?: "))
    notas = []

    for quantidade in range(quantidade_notas):
        while True:
            try:
                nota = input(f"Insira a {quantidade + 1}ª nota:")
                nota = float(nota.replace(',', '.'))
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
    return notas

def presenca_das_alunas():
    quantidade_presenca = int(input("Qual a quantidade de aulas?: "))
    presencas = []

    for presente in range(quantidade_presenca):
        while True:
            presenca_str = input(f'Insira "True" para presente e "False" para ausente para a {presente + 1}ª aula: ')
            if presenca_str.lower() == "true":
                presencas.append(True)
                break
            elif presenca_str.lower() == "false":
                presencas.append(False)
                break
            else:
                print("Entrada inválida. Por favor utilize True para presente e False para ausente.")
    return presencas

def participacao_alunas():
    while True:
        participacao_str = input("Digite a nota de participação da aluna: ")
        try:
            participacao = float(participacao_str.replace(',', '.'))
            break
        except ValueError:
            print("Entrada inválida. Digite números separados por vírgula ou ponto. Ex: 8.9 / 9,0")
    return participacao

def consultar_lista_alunas():
    if not dataset:
        print("Nenhuma aluna cadastrada.")
    else:
        print("\nLista de Alunas:")
        for (nome, sobrenome), dados in dataset.items():
            print(f"Nome: {nome} {sobrenome}, Turma: {dados['Turma']}")

def consultar_faltas_aluna():
    nome, sobrenome = nome_aluna()
    if (nome, sobrenome) in dataset:
        presencas = dataset[(nome, sobrenome)].get('Presenca')
        if presencas is not None:
            faltas = presenca_das_alunas.count(False)
            print(f"A aluna {nome} {sobrenome} teve {faltas} falta(s).")
        else:
            print("Não foi possível obter informações de presença para esta aluna.")
    else:
        print("Aluna não encontrada.")

def consultar_notas_aluna():
    nome, sobrenome = nome_aluna()
    if (nome, sobrenome) in dataset:
        notas = dataset[(nome, sobrenome)]['Notas']
        print(f"Notas de {nome} {sobrenome}: {notas}")
    else:
        print("Aluna não encontrada.")
        
def consultar_status_aprovacao(): ### Retornado média 
    print("Inserir dados")
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    quantidade_notas = int(input("Quantidade de notas: "))
    
    notas = []
    for i in range(quantidade_notas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        notas.append(nota)
    
    media_das_notas = sum(notas) / len(notas)
    print(f"A média das notas de {nome} {sobrenome} é: {media_das_notas:.2f}")

main()
