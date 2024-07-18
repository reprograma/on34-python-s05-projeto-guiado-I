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
    nome, sobrenome = nome_aluna()
    turma = input("Qual a turma da aluna?: ")
    notas = notas_aluna()
    presencas = presenca_das_alunas()
    participacao = participacao_alunas()

    dataset[(nome, sobrenome)] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presencas,
        "Participação": participacao
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

    for quantidade in range(int(quantidade_notas)):
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
            try:
                presenca_str = input(f'Insira "True" para presente e "False" para ausente para a {presente + 1}ª aula: ')
                presenca = eval(presenca_str)
                if isinstance(presenca, bool):
                    presencas.append(presenca)
                    break
                else:
                    print("Entrada inválida. Por favor utilize True para presente e False para ausente.")
            except:
                print("Entrada inválida. Por favor utilize True para presente e False para ausente.")
    return presencas

def participacao_alunas ():
    
    while True:
        participacao_str = input("Digite a nota de participação da aluna: ")
        try:
            participacao = float(participacao_str.replace(',', '.'))
    
            break
        
        except ValueError:
            print ("Entrada inválida. Digite números separados por vírgula ou ponto. Ex: 8.9 / 9,0")
    return participacao

    
def consultar_lista_alunas():
    if dataset:
        print("\n--- Lista de Alunas da Escola do Reprograma! 🎓  ---")
        for nome, sobrenome in sorted(dataset.keys()):
            print(f"Aluna: {nome} {sobrenome}")
    else:
        print("Não há alunas cadastradas.")

def consultar_faltas_aluna():
    nome_sobrenome = input("Qual o nome e sobrenome da aluna?: ")
    try:
        nome, sobrenome = nome_sobrenome.split(' ')
        chave_dicionario = (nome, sobrenome)

        if chave_dicionario in dataset:
            if "Presença" in dataset[chave_dicionario]:
                quantidade_faltas = dataset[chave_dicionario]["Presença"].count(False)
                print(f"A aluna {nome} {sobrenome} tem {quantidade_faltas} faltas.")
            else:
                print(f"A aluna {nome} {sobrenome} não possui registros de presença.")
        else:
            print(f"A aluna {nome} {sobrenome} não está cadastrada.")
    except ValueError:
        print("Entrada inválida. Digite um NOME e um SOBRENOME separado por espaço.")
    
def consultar_notas_aluna():
    nome_sobrenome = input("Qual o nome e sobrenome da aluna?: ")
    try:
        nome, sobrenome = nome_sobrenome.split(' ')
        chave_dicionario = (nome, sobrenome)

        if chave_dicionario in dataset:
            if "Notas" in dataset[chave_dicionario]:
                todas_notas = dataset[chave_dicionario]["Notas"]
                print(f"As notas da Aluna {nome} {sobrenome} são: {todas_notas} ")
            else:
                print(f"A aluna {nome} {sobrenome} não possui registro de notas.")
        else:
            print(f"A aluna {nome} {sobrenome} não está cadastrada.")
    except ValueError:
        print("Entrada inválida. Digite um NOME e um SOBRENOME separado por espaço.")
    
def consultar_status_aprovacao():
    nome_sobrenome = input("Qual o nome e sobrenome da aluna?: ")
    try:
        nome, sobrenome = nome_sobrenome.split(' ')
        chave_dicionario = (nome, sobrenome)

        if chave_dicionario in dataset:
            aluna = dataset[chave_dicionario]

            if "Presença" in aluna:
                presencas = aluna["Presença"]
                percentual_presenca = presencas.count(True) / len(presencas) * 100
            else:
                print(f"A aluna {nome} {sobrenome} não possui registros de presença.")
                return

            if "Participação" in aluna:
                nota_participacao = aluna["Participação"]
            else:
                print(f"A aluna {nome} {sobrenome} não possui registro de participação.")
                return

            if "Notas" in aluna:
                notas = aluna["Notas"]
                media = sum(notas) / len(notas)
            else:
                print(f"A aluna {nome} {sobrenome} não possui registro de notas.")
                return

            #Cálculo do status de aprovação
            if percentual_presenca >= 80 and nota_participacao > 6 and media >= 6:
                print(f"A aluna {nome} {sobrenome} foi aprovada com {percentual_presenca:.2f}% de presença, {nota_participacao} de participação e {media:.2f} de média.")
            else:
                motivos_reprovacao = []
                if percentual_presenca < 80:
                    motivos_reprovacao.append(f"presença insuficiente ({percentual_presenca:.2f}%)")
                if nota_participacao <= 6:
                    motivos_reprovacao.append(f"nota de participação baixa ({nota_participacao})")
                if media < 6:
                    motivos_reprovacao.append(f"média insuficiente ({media:.2f})")
                
                print(f"A aluna {nome} {sobrenome} foi reprovada por: {', '.join(motivos_reprovacao)}.")

        else:
            print(f"A aluna {nome} {sobrenome} não está cadastrada.")
    except ValueError:
        print("Entrada inválida. Digite um NOME e um SOBRENOME separado por espaço.")

main()