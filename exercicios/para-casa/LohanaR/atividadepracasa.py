def main():
    dataset = {'discentes': []}
    print("\n---  Olá, seja bem-vinde à Escola do Reprograma!  ---")
    print("Sistema de informações de discentes")

    while True:
        cod_opcao = obter_opcao()
        if cod_opcao == 1:
            incluir_nova_discente(dataset)
        elif cod_opcao == 2:
            consultar_lista_discentes(dataset)
        elif cod_opcao == 3:
            consultar_faltas_discente(dataset)
        elif cod_opcao == 4:
            consultar_notas_discente(dataset)
        elif cod_opcao == 5:
            consultar_status_aprovacao(dataset)
        elif cod_opcao == 6:
            print("Encerrando o programa...")
            encerramento()
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

def incluir_nova_discente(dataset):
    nome = input("Por favor, digite o nome da discente: ")
    try:
        faltas = int(input("Por favor, digite o número de faltas: "))
    except ValueError:
        print("Esse número de faltas é inválido. Por favor, digite um número inteiro.")
        return

    notas = []
    print("Por favor, digite as notas da discente. Se desejar encerrar, digite 'finalizar' para concluir.")
    while True:
        nota = input("Nota: ")
        if nota.lower() == 'finalizar':
            break
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10: 
                notas.append(nota_float)
            else:
                print("Essa nota não atende o critério do intervalo aceitável (0 a 10).")
        except ValueError:
            print("Essa entrada é inválida. Por favor, digite um número válido ou 'finalizar' para concluir.")

    if len(notas) == 0:
        print("Discente não incluída.")
        return

    dataset['discentes'].append({
        'nome': nome,
        'faltas': faltas,
        'notas': notas
    })
    print("Discente incluída!")

def consultar_lista_discentes(dataset):
    if len(dataset['discentes']) == 0:
        print("\nSem cadastro de discentes.")
        return

    print("\nDiscentes:")
    for discente in dataset['discentes']:
        print(f"Nome: {discente['nome']}, Faltas: {discente['faltas']}, Notas: {discente['notas']}")

def consultar_faltas_discente(dataset):
    if len(dataset['discentes']) == 0:
        print("\nSem cadastro de discentes.")
        return

    nome = input("Por favor, digite o nome da discente: ")
    for discente in dataset['discentes']:
        if discente['nome'] == nome:
            print(f"Discente: {discente['nome']}, Faltas: {discente['faltas']}")
            return
    print("Ops, essa discente não consta no sistema.")

def consultar_notas_discente(dataset):
    if len(dataset['discentes']) == 0:
        print("\nSem cadastro de discentes.")
        return

    nome = input("Por favor, digite o nome da discente: ")
    for discente in dataset['discentes']:
        if discente['nome'] == nome:
            print(f"Discente: {discente['nome']}, Notas: {discente['notas']}")
            return
    print("Ops, essa discente não consta no sistema.")

def consultar_status_aprovacao(dataset):
    if len(dataset['discentes']) == 0:
        print("\nOps, não consta discentes registradas no sistema.")
        return

    nome = input("Por favor, digite o nome da discente: ")
    for discente in dataset['discentes']:
        if discente['nome'] == nome:
            media = sum(discente['notas']) / len(discente['notas'])
            presenca = 1 - (discente['faltas'] / 100)
            if media >= 6 and presenca >= 0.8:
                status = "Aprovada (;"
            else:
                status = "Reprovada ):"
            print(f"Discente: {discente['nome']}, Média: {media:.2f}, Status: {status}")
            return
    print("Essa discente não consta no sistema.")

def encerramento():
    print("\nObrigada por usar o sistema de informações de discentes da Escola do Reprograma!")
    print("Esperamos vê-lo(a) novamente em breve. Tenha um ótimo dia!\n")

main()
