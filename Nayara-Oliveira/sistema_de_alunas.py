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

    while codigo_opcao not in [1, 2, 3, 4, 5]:
        try:
            codigo_opcao = int(input("\nEscolha uma opção:\n"
                                    "1 - Incluir uma nova aluna\n"
                                    "2 - Consultar lista de alunas\n"
                                    "3 - Consultar faltas da aluna\n"
                                    "4 - Consultar notas da aluna\n"
                                    "5 - Consultar status de aprovação\n"
                                    "6 - Sair do sistema\n"
                                    "Opção: "))
                
            if codigo_opcao not in [1, 2, 3, 4, 5]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 5).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna():
    print("Insira os seguintes dados para cadastrar uma nova aluna:")
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    turma = input("Turma da aluna: ")
    quantidade_notas = input("Quantidade de notas: ")
    try:
        notas = []
        for i in range(int(quantidade_notas)):
            try:
                nota = float(input(f"Insira a nota #{i+1}: "))
                if nota >= 0 and nota <= 10:
                    notas.append(nota)
                else:
                    print("Entrada inválida. A nota deve ser um número entre 0 e 10.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.\n")
        if len(notas) != int(quantidade_notas):
            notas = []
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.\n")
    quantidade_aulas = input("Quantidade de aulas: ")
    try:
        presencas = []
        for i in range(int(quantidade_aulas)):
            presenca = input(f"A aluna esteve presente na aula #{i+1}? Digite P para presente ou A para ausente: ")
            if presenca == "P":
                presencas.append(True)
            elif presenca == "A":
                presencas.append(False)
            else:
                print("Opção inválida. Por favor, escolha uma opção válida (P ou A).")
        if len(presencas) != int(quantidade_aulas):
            presencas = []
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro\n")
    nota_participacao = False
    try:
        nota_participacao_float = float(input("Nota de participação da aluna: "))
        if nota_participacao_float >= 0 and nota_participacao_float <= 10:
            nota_participacao = nota_participacao_float
        else:
            print("Entrada inválida. A nota deve ser um número entre 0 e 10.")
    except:
        print("Entrada inválida. Por favor, digite um número")
    
    if notas and presencas and nota_participacao:
        dataset[(nome, sobrenome)] = {
            "Turma": f"Turma {turma}",
            "Notas": notas,
            "Presença": presencas,
            "Participação": nota_participacao
        }
        print(f"A aluna {nome} {sobrenome} foi adicionada com sucesso.")
    else:
        print("Não foi possível incluir a aluna na base de dados. Tente novamente")
    
def consultar_lista_alunas():
    nomes_completos = dataset.keys()
    lista_nomes = [nome_completo[0] for nome_completo in nomes_completos]
    print("A lista com os nomes das alunas cadastradas é: ")
    nomes = [print("-", nome) for nome in lista_nomes]
    
def consultar_faltas_aluna():
    nome = input("Informe o nome da aluna: ")
    sobrenome = input("Informe o sobrenome da aluna: ")
    try:
        faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
        if faltas == 1:
            print(f"A aluna {nome} {sobrenome} possui {faltas} falta")
        else:
            print(f"A aluna {nome} {sobrenome} possui {faltas} faltas")
    except KeyError:
        print("Não foi possível consultar as faltas da aluna. O nome completo informado não corresponde a uma aluna cadastrada.")
    
def consultar_notas_aluna():
    nome = input("Informe o nome da aluna: ")
    sobrenome = input("Informe o sobrenome da aluna: ")
    try:
        notas = dataset[(nome, sobrenome)]["Notas"]
        for i in range(len(notas)):
            print(f"Na avaliação #{i+1}, a nota da aluna {nome} {sobrenome} foi {notas[i]}")
    except KeyError:
        print("Não foi possível consultar as notas da aluna. O nome completo informado não corresponde a uma aluna cadastrada.")
    
def consultar_status_aprovacao():
    nome = input("Informe o nome da aluna: ")
    sobrenome = input("Informe o sobrenome da aluna: ")
    try:
        notas = dataset[(nome, sobrenome)]["Notas"]
        nota_participacao = dataset[(nome, sobrenome)]["Participação"]
        media = (sum(notas) + nota_participacao) / (len(notas) + 1)
        presencas = dataset[(nome, sobrenome)]["Presença"]
        percentual_presenca = (presencas.count(True) / len(presencas)) * 100
        if percentual_presenca >= 80 and media >= 6:
            status = "aprovada"
        else:
            status = "reprovada"
        print(f"A aluna {nome} {sobrenome} está {status}. A sua média final é {media}")
    except KeyError:
        print("Não foi possível consultar o status de aprovação. O nome completo informado não corresponde a uma aluna cadastrada.")

main()