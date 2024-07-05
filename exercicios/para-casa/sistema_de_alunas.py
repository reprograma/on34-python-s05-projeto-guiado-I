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
    nome = input("Insira o nome:\n")
    sobrenome = input("Insira o sobrenome:\n")
    turma = input("Insira a turma:\n")

    notas_input = input("Insira as notas separadas por vírgula:\n")
    notas = notas_input.split(",")

    presenca_input = input("Insira as presenças separadas por vírgula (1 para presença, 0 para falta)")
    presenca_lista = presenca_input.split(",")
    presenca = [True if cada.strip() == "1" else False for cada in presenca_lista]   

    participacao = float(input("Insira a nota de participação"))

    if notas and all(0 <= len(nota) <= 10 for nota in notas):
        global dataset
        dataset[(nome, sobrenome)] = {
            "Turma": turma,
            "Notas": notas,
            "Presença": presenca,
            "Participação": participacao
        }
        print("Aluna adicionada com sucesso!")
    else:
        print("Verifique as notas.")
    
def consultar_lista_alunas():
    if not dataset:
        print("Não há alunas cadastradas.")
    else:
        for nome, sobrenome in dataset.keys():
            print(f"{nome} {sobrenome}")

    
def consultar_faltas_aluna():
    nome_completo = input("Nome completo da aluna: ")

    aluna_encontrada = False
    for key in dataset.keys():
        if f"{key[0]} {key[1]}" == nome_completo:
            faltas = dataset[key]["Presença"].count(False)
            print(f"A aluna {nome_completo} possui {faltas} faltas.")
            aluna_encontrada = True
            break
    
    if not aluna_encontrada:
        print(f"A aluna {nome_completo} não foi encontrada.")

    
def consultar_notas_aluna():
    nome_completo = input("Nome completo da aluna: ")
    
    aluna_encontrada = False
    for key in dataset.keys():
        if f"{key[0]} {key[1]}" == nome_completo:
            notas = dataset[key]["Notas"]
            print(f"As notas de {nome_completo} são: {notas}")
            aluna_encontrada = True
            break
    
    if not aluna_encontrada:
        print(f"A aluna {nome_completo} não foi encontrada.")

    
def consultar_status_aprovacao():
    nome_completo = input("Nome completo da aluna: ")
    
    aluna_encontrada = False
    for key in dataset.keys():
        if f"{key[0]} {key[1]}" == nome_completo:
            notas = dataset[key]["Notas"]
            presenca = dataset[key]["Presença"]
            participacao = dataset[key]["Participação"]
            
            media = sum(notas) / len(notas)
            
            if media >= 6 and (presenca.count(True) / len(presenca)) >= 0.8 and participacao > 6:
                status = "Aprovada"
            else:
                status = "Reprovada"
            
            print(f"Status de {nome_completo}: {status} | Média: {media:.2f}")
            aluna_encontrada = True
            break
    
    if not aluna_encontrada:
        print(f"A aluna {nome_completo} não foi encontrada.")

main()