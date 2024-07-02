### Exercico Casa/S05 - sem "opcinal" sugerido pelo desafio.

def main():
    print("\n---  Seja bem-vinda à Escola do Reprograma!  ---")
    print('Sou a Assistente virtual Jennifer, vamos trabalhar?')
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = obter_opcao()  
        if cod_opcao == 1:
            incluir_nova_aluna(dataset)  
        elif cod_opcao == 2:
            consultar_lista_alunas(dataset)  
        elif cod_opcao == 3:
            consultar_faltas_aluna(dataset)  
        elif cod_opcao == 4:
            consultar_notas_aluna(dataset)  
        elif cod_opcao == 5:
            consultar_status_aprovacao(dataset)  
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
    
def incluir_nova_aluna(dataset):
    nome = input("Digite o nome da aluna: ")
    try:
        faltas = int(input("Digite o número de faltas: "))
    except ValueError:
        print("Número de faltas inválido. Por favor, digite um número inteiro.")
        return

    notas = []
    print("Digite as notas da aluna. Digite 'fim' para terminar.")
    while True:
        nota = input("Nota: ")
        if nota.lower() == 'fim':
            break
        try:
            nota_float = float(nota)
            if 0 <= nota_float <= 10: 
                notas.append(nota_float)
            else:
                print("Nota fora do intervalo permitido (0 a 10).") ## Validação do intervalo das notas, exemplo letra ou negativo e +de 10.
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido ou 'fim' para terminar.")

    if len(notas) == 0:
        print("Nenhuma nota válida foi adicionada. Aluna não incluída.")
        return

    dataset['alunas'].append({
        'nome': nome,
        'faltas': faltas,
        'notas': notas
    })
    print("Aluna incluída com sucesso!")

def consultar_lista_alunas(dataset):
    if len(dataset['alunas']) == 0:
        print("\nNão há registros de alunas cadastradas.")
        return

    print("\nLista de Alunas:")
    for aluna in dataset['alunas']:
        print(f"Nome: {aluna['nome']}, Faltas: {aluna['faltas']}, Notas: {aluna['notas']}")

def consultar_faltas_aluna(dataset):
    if len(dataset['alunas']) == 0:
        print("\nNão há registros de alunas cadastradas.")
        return

    nome = input("Digite o nome da aluna: ")
    for aluna in dataset['alunas']:
        if aluna['nome'] == nome:
            print(f"Aluna: {aluna['nome']}, Faltas: {aluna['faltas']}")
            return
    print("Aluna não encontrada.")

def consultar_notas_aluna(dataset):
    if len(dataset['alunas']) == 0:
        print("\nNão há registros de alunas cadastradas.")
        return

    nome = input("Digite o nome da aluna: ")
    for aluna in dataset['alunas']:
        if aluna['nome'] == nome:
            print(f"Aluna: {aluna['nome']}, Notas: {aluna['notas']}")
            return
    print("Aluna não encontrada.")

def consultar_status_aprovacao(dataset):
    if len(dataset['alunas']) == 0:
        print("\nNão há registros de alunas cadastradas.")
        return

    nome = input("Digite o nome da aluna: ")
    for aluna in dataset['alunas']:
        if aluna['nome'] == nome:
            media = sum(aluna['notas']) / len(aluna['notas'])
            presenca = 1 - (aluna['faltas'] / 100)  
            if media >= 6 and presenca >= 0.8:  ## Calcula a presença / 80 porcentagem para aprovação.
                status = "Aprovada"
            else:
                status = "Reprovada"
            print(f"Aluna: {aluna['nome']}, Média: {media:.2f}, Status: {status}")
            return
    print("Aluna não encontrada.")

main()



