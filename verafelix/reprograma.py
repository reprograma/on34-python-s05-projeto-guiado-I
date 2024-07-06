dataset = {
    ("Ana", "Silva"): {
        "Turma": "Turma A",
        "Notas": [7.5, 8.0, 9.0],
        "Presença": [True, True, False, True, True],
        "Participação": 8.5
    },
    ("Mariana", "Santos"): {
        "Turma": "Turma B",
        "Notas": [6.0, 7.5, 8.5],
        "Presença": [True, True, True, False, True],
        "Participação": 7.2
    },
    ("Carla", "Oliveira"): {
        "Turma": "Turma A",
        "Notas": [8.0, 7.5, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.2
    },
    ("Juliana", "Ferreira"): {
        "Turma": "Turma C",
        "Notas": [9.0, 8.5, 7.0],
        "Presença": [True, True, True, True, True],
        "Participação": 8.7
    },
    ("Patrícia", "Souza"): {
        "Turma": "Turma B",
        "Notas": [7.0, 7.0, 7.5],
        "Presença": [True, False, True, True, True],
        "Participação": 7.2
    },
    ("Aline", "Martins"): {
        "Turma": "Turma A",
        "Notas": [8.5, 8.0, 9.0],
        "Presença": [True, True, True, True, True],
        "Participação": 8.5
    },
    ("Fernanda", "Costa"): {
        "Turma": "Turma C",
        "Notas": [6.5, 7.0, 8.0],
        "Presença": [True, True, True, False, True],
        "Participação": 7.2
    },
    ("Camila", "Pereira"): {
        "Turma": "Turma B",
        "Notas": [7.5, 8.0, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.0
    },
    ("Luana", "Rodrigues"): {
        "Turma": "Turma A",
        "Notas": [9.0, 9.0, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.8
    },
    ("Beatriz", "Lima"): {
        "Turma": "Turma C",
        "Notas": [8.0, 7.5, 7.0],
        "Presença": [True, True, True, False, True],
        "Participação": 7.5
    }
}


def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")

    while True:
        cod_opcao = obter_opcao()  # Obtém a opção escolhida pelo usuário

        if cod_opcao == 1:
            incluir_nova_aluna()  # Chama a função para incluir nova aluna
        elif cod_opcao == 2:
            consultar_lista_alunas()  # Chama a função para consultar lista de alunas
        elif cod_opcao == 3:
            consultar_faltas_aluna()  # Chama a função para consultar faltas de uma aluna
        elif cod_opcao == 4:
            consultar_notas_aluna()  # Chama a função para consultar notas de uma aluna
        elif cod_opcao == 5:
            consultar_status_aprovacao()  # Chama a função para consultar status de aprovação
        elif cod_opcao == 6:
            print("Encerrando o programa...")
            break  # Encerra o programa


def obter_opcao():
    codigo_opcao = 0

    while codigo_opcao not in [1, 2, 3, 4, 5, 6]:
        try:
            # Solicita ao usuário para escolher uma opção
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
    # Solicita os dados da nova aluna
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    turma = input("Digite a turma da aluna: ")
    notas = list(
        map(float, input("Digite as notas da aluna separadas por espaço: ").split()))
    presenca = list(map(lambda x: x.lower() == 'true', input(
        "Digite as presenças da aluna (True/False) separadas por espaço: ").split()))
    participacao = float(input("Digite a nota de participação da aluna: "))

    # Valida que todas as notas estão no intervalo permitido
    if not all(0 <= nota <= 10 for nota in notas):
        print("Erro: Todas as notas devem estar entre 0 e 10.")
        return

    # Adiciona a nova aluna ao dataset
    dataset[(nome, sobrenome)] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presenca,
        "Participação": participacao
    }
    print(f"Aluna {nome} {sobrenome} adicionada com sucesso!")


def consultar_lista_alunas():
    if not dataset:
        # Informa se não há alunas cadastradas
        print("Não há alunas cadastradas.")
    else:
        print("\nLista de alunas cadastradas:")
        # Exibe a lista de alunas cadastradas
        for (nome, sobrenome) in dataset:
            print(f"- {nome} {sobrenome}")


def consultar_faltas_aluna():
    # Solicita o nome e sobrenome da aluna
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    aluna = dataset.get((nome, sobrenome))

    if aluna:
        faltas = aluna["Presença"].count(False)  # Conta o número de faltas
        print(f"A aluna {nome} {sobrenome} tem {faltas} faltas.")
    else:
        # Informa se a aluna não foi encontrada
        print(f"Aluna {nome} {sobrenome} não encontrada.")


def consultar_notas_aluna():
    # Solicita o nome e sobrenome da aluna
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    aluna = dataset.get((nome, sobrenome))

    if aluna:
        notas = aluna["Notas"]
        print(f"Notas da aluna {nome} {sobrenome}: {
              notas}")  # Exibe as notas da aluna
    else:
        # Informa se a aluna não foi encontrada
        print(f"Aluna {nome} {sobrenome} não encontrada.")


def consultar_status_aprovacao():
    # Solicita o nome e sobrenome da aluna
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    aluna = dataset.get((nome, sobrenome))

    if aluna:
        # Calcula a média das notas
        media_notas = sum(aluna["Notas"]) / len(aluna["Notas"])
        percentual_presenca = aluna["Presença"].count(
            True) / len(aluna["Presença"])  # Calcula o percentual de presença
        participacao = aluna["Participação"]

        # Verifica se a aluna está aprovada
        if media_notas >= 6 and percentual_presenca >= 0.8 and participacao > 6:
            status = "aprovada"
        else:
            status = "reprovada"

        print(f"A aluna {nome} {sobrenome} está {
              status} com média final {media_notas:.2f}.")
    else:
        # Informa se a aluna não foi encontrada
        print(f"Aluna {nome} {sobrenome} não encontrada.")


main()  # Executa a função principal
