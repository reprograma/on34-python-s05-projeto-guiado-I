from dataset_alunas import dataset


def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = serviço_escolhido()
            
        if cod_opcao == 1: 
            obter_dados()       # Incluir nova aluna
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

def serviço_escolhido():
    while True:
        try:
            cod_opcao = int(input("\nEscolha uma opção:\n"
                                  "1 - Incluir uma nova aluna\n"
                                  "2 - Consultar lista de alunas\n"
                                  "3 - Consultar faltas da aluna\n"
                                  "4 - Consultar notas da aluna\n"
                                  "5 - Consultar status de aprovação\n"
                                  "6 - Sair do sistema\n"
                                  "Opção: "))
            if cod_opcao not in [1, 2, 3, 4, 5, 6]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 6).\n")
            else:
                return cod_opcao
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")


def obter_dados():
    nome = input('Qual o nome da nova aluna?: ').title()
    sobrenome = input(f'Qual sobrenome da {nome}?: ').title()
    turma = input(f'Qual turma a {nome, sobrenome} pertence?: ')
    lista_presença = obter_presença()
    nota_participação = float(input('Participação da nova aluna: '))
    notas = obter_notas()

    salvar_dados(nome, sobrenome, turma, lista_presença, nota_participação, notas)

def obter_notas():
    quantidade_notas = int(input('Quantas notas serão calculadas?: '))
    notas = []
    for contador in range(quantidade_notas):
        while True: 
            entrada = input(f'Nota do #{contador + 1}: ')
            try:
                nota = float(entrada)
                notas.append(nota)
                break
            except ValueError:
                print('Erro em processar o valor. Insira um número válido')
    
    return notas

def obter_presença():
    quantidade_aulas = int(input('Digite quantas aulas houveram: '))
    lista_presença = []

    for contador in range(quantidade_aulas):
        while True:
            entrada = input(f'Presença na aula #{contador +1} (True/False): ')
            if entrada in ['True', 'False']:
                lista_presença.append(eval(entrada))
                break
            else:
                print('Informação inválida. Insira apenas True ou False')

    return lista_presença

def salvar_dados(nome, sobrenome, turma, lista_presença, nota_participação, notas):
    chave = (nome, sobrenome)
    dataset[chave] = { 
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_presença,
        "Participação": nota_participação
    }
    print(f'Os dados da aluna {nome} {sobrenome} foram inseridos com sucesso.')

def consultar_lista_alunas():
    if dataset:
        print('Lista de todas as alunas')
        for chave in dataset.keys():
            print(f'Nome: {chave[0]} {chave[1]}')
    else:
        print('Não há novos cadastros')

def consultar_faltas_aluna():
    nome = input('Informe o primeiro nome da aluna: ').title()
    sobrenome = input('Informe o sobrenome da aluna: ').title()
    chave = (nome, sobrenome)
    if chave in dataset:
        faltas = dataset[chave]["Presença"].count(False)
        print(f'A aluna {nome} {sobrenome} está com {faltas} faltas')
    else:
        print('Aluna não encontrada.')

def consultar_notas_aluna():
    nome = input('Informe o primeiro nome da aluna: ').title()
    sobrenome = input('Informe o sobrenome da aluna: ').title()
    chave = (nome, sobrenome)
    if chave in dataset:
        notas = dataset[chave]["Notas"]
        print(f'A aluna {nome} {sobrenome} está com as notas: {notas}')
    else:
        print('Aluna não encontrada.')

def consultar_status_aprovacao():
    nome = input('Insira o primeiro nome da aluna: ').title()
    sobrenome = input('Insira o sobrenome da aluna: ').title()
    chave = (nome, sobrenome)
    if chave in dataset:
        dados = dataset[chave]
        media_notas = sum(dados["Notas"]) / len(dados["Notas"])
        presença = dados["Presença"].count(True) / len(dados["Presença"])
        participação = dados["Participação"]

        if media_notas >= 6 and presença >= 0.8 and participação > 6:
            status = 'Aprovada'
        else:
            status = 'Reprovada'
        print(f'A aluna {nome} {sobrenome} está {status} com média final: {media_notas:.2f}')
    else:
        print('Aluna não encontrada')

main()
