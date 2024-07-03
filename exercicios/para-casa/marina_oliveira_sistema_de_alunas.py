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
    print("\nInsira os dados da aula! ")
    nome = input("Nome da aluna:")
    sobrenome = input("Sobrenome da aluna: ")
    turma = input("Turma da aluna: ")
    notas = obter_nota()
    presenca = obter_presenca()
    participacao = float(input("Nota de participação da aluna: "))

    salvar_dados_alunas(nome, sobrenome, turma, notas, presenca, participacao)

    return nome

def obter_nota():
    quantidade_notas = input("Quantas notas deseja inserir? ")
    notas = []

    for i in range(int(quantidade_notas)):
        while True:
            entrada = input(f"Insira a nota {i + 1}: ")   
            try: 
                nota = float(entrada)
                notas.append(nota)
                break
            except ValueError:
                print("Entrada inválida. Por favor, insira true ou false.")

    return notas 

def obter_presenca(): 
    quantidade_aulas = input("Insira a quantidade de aulas da aluna: ")
    presenca = []

    for i in range(int(quantidade_aulas)):
        while True:
            entrada = input(f"Presença na aula {i + 1} (True/False): ")
            if entrada.lower() == 'true':
                presenca.append(True)
                break
            elif entrada.lower() == 'false':
                presenca.append(False)
                break
            else:
                print("Entrada inválida. Por favor, digite 'True' ou 'False'.")

    return presenca    

def salvar_dados_alunas(nome, sobrenome, turma, notas, presenca, participacao):
    chave = (nome, sobrenome)
    dataset[chave] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presenca,
        "Participação": participacao,
    }
    
    print(f"Aluna {nome} {sobrenome} adicionada com sucesso!")
    
    
def consultar_lista_alunas():
    if dataset:
        print("\nAlunas cadastradas:")
        for nome in dataset:
            print(nome)
    else:
        print("\nNão há alunas cadastradas.")
    
def consultar_faltas_aluna():
    nome_aluna = input("Insira o nome completo da aluna: ")
    if nome_aluna in dataset:
        faltas = dataset[nome_aluna]["Presença"].count(False)
        print(f"\nA aluna {nome_aluna} teve {faltas} faltas.")
    else:
        print(f"\nA aluna {nome_aluna} não foi encontrada.")
    
def consultar_notas_aluna():
    nome_aluna = input("Insira o nome completo da aluna: ")
    if nome_aluna in dataset:
        notas = dataset[nome_aluna]["Notas"]
        print(f"\nAs notas da aluna {nome_aluna} são: {notas}")
    else:
        print(f"\nA aluna {nome_aluna} não foi encontrada.")
    
def consultar_status_aprovacao():
    nome_aluna = input("Insira o nome completo da aluna: ")

    if nome_aluna in dataset:
        dados_aluna = dataset[nome_aluna]
        notas = dados_aluna.get("Notas", [])
        presenca = dados_aluna.get("Presença", [])
        participacao = dados_aluna.get("Participação", 0)

        media = sum(notas) / len(notas) if notas else 0
        presenca_percentual = (presenca.count(True) / len(presenca)) * 100 if presenca else 0
        
        if media >= 6.0 and presenca_percentual >= 80 and participacao > 6:
            print(f"\nA aluna {nome_aluna} está Aprovada com média {media:.2f}.")
        else:
            print(f"\nA aluna {nome_aluna} está Reprovada com média {media:.2f}.")
    else:
        print(f"\nA aluna {nome_aluna} não foi encontrada.")
    

main()