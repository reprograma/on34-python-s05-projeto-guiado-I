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
    nome = input("Digite o nome primeiro da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    turma = input("Digite a turma da aluna: ")
    
    try:
        notas = list(map(float, input("Digite as notas da aluna (separadas por espaço): ").split()))
        presencas = list(map(lambda x: x.lower() == 'true', input("Digite a presença da aluna (True/False separados por espaço): ").split()))
        participacao = float(input("Digite a nota de participação da aluna: "))
    except ValueError:
        print("Erro: Entrada inválida. Certifique-se de que os dados estão no formato correto.")
        return
    
    if any(nota < 0 or nota > 10 for nota in notas):
        print("Erro: As notas devem estar entre 0 e 10.")
        return
    
    dataset[(nome, sobrenome)] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presencas,
        "Participação": participacao
    }
    
    print(f"Aluna {nome} {sobrenome} adicionada com sucesso!")
    
def consultar_lista_alunas():
    if not dataset:
        print("Não há alunas cadastradas.")
    else:
        print("\nLista de alunas cadastradas:")
        for nome, sobrenome in dataset.keys():
            print(f"- {nome} {sobrenome}")
    
def consultar_faltas_aluna():
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    
    aluna = dataset.get((nome, sobrenome))
    if aluna:
        faltas = aluna["Presença"].count(False)
        print(f"A aluna {nome} {sobrenome} tem {faltas} faltas.")
    else:
        print(f"Erro: Aluna {nome} {sobrenome} não encontrada.")
    
def consultar_notas_aluna():
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    
    aluna = dataset.get((nome, sobrenome))
    if aluna:
        notas = aluna["Notas"]
        print(f"Notas da aluna {nome} {sobrenome}: {', '.join(map(str, notas))}")
    else:
        print(f"Erro: Aluna {nome} {sobrenome} não encontrada.")
    
def consultar_status_aprovacao():
    nome = input("Digite o nome da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    
    aluna = dataset.get((nome, sobrenome))
    if aluna:
        notas = aluna["Notas"]
        media = sum(notas) / len(notas)
        percentual_presenca = aluna["Presença"].count(True) / len(aluna["Presença"])
        participacao = aluna["Participação"]
        
        status_aprovacao = "aprovada" if media >= 6 and percentual_presenca >= 0.8 and participacao > 6 else "reprovada"
        print(f"A aluna {nome} {sobrenome} está {status_aprovacao} com média {media:.2f}.")
    else:
        print(f"Erro: Aluna {nome} {sobrenome} não encontrada.")
    

main()