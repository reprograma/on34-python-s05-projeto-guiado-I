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
    print('\nInsira os seguintes dados: ')
    nome = input('Nome da aluna: ')
    sobrenome = input('Sobrenome da aluna: ')
    turma = input('Turma da aluna: ') 
    lista_de_presenca = presenca(nome, sobrenome) 
    nota_participacao = float(input('Nota de participação da aluna (0-10): ')) 
    notas = obter_notas(nome,sobrenome)

    salvar_dados_aluna(nome, sobrenome, turma, notas, lista_de_presenca, nota_participacao)
    return incluir_nova_aluna


def presenca(nome,sobrenome):
    print('\nInsira os seguintes dados: ')
    lista_de_presenca = []
    for i in range(1,6):
        while True:
            contagem = input(f'Aluna compareceu a aula do dia {i}? True/False: ')
            if contagem == 'True':
                lista_de_presenca.append(True)
                break
            elif contagem == 'False':
                lista_de_presenca.append(False)
                break
            else:
                print('Dado inválido. Por favor, insira True ou False.')

    return lista_de_presenca

def obter_notas(nome,sobrenome):
    print('\nInsira os seguintes dados: ')
    notas = []
    for contador in range(1,4): 
          while True: 
            entrada = input(f'Insira a nota da aula {contador}: ') 
            try: 
                nota = float(entrada) 
                notas.append(nota) 
                break
            except ValueError: 
                print('Dado inválido. Por favor, insira um número válido.')
    return notas
            

def salvar_dados_aluna(nome, sobrenome, turma, notas, lista_de_presenca, nota_participacao):
    
    dataset[nome,sobrenome] = { 
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_de_presenca,
        "Participação": nota_participacao
    }
    return(print('Aluna',nome,sobrenome,'foi adicionada com sucesso!'))


def consultar_lista_alunas():
    lista_de_alunas = dataset.keys()
    for item in lista_de_alunas:
        print('.',item[0],item[1])   
    if not lista_de_alunas:
        print('Não há cadastro no sistema. Escolha a opção abaixo para cadastrar uma nova aluna.')


def consultar_faltas_aluna():
    print('\nInsira os seguintes dados: ')
    frequencia_nome = input('Digite o nome da aluna: ')
    frequencia_sobrenome = input('Digite o sobrenome da aluna: ')
    frequencia = dataset.get((frequencia_nome,frequencia_sobrenome))
    if frequencia:
        faltas = frequencia["Presença"].count(False)  
        print('Quantidade de faltas da aluna:',faltas)
    else: 
     print('Não encontramos',frequencia_nome,frequencia_sobrenome,'no sistema. Escolha a opção abaixo para cadastrar a nova aluna.')

def consultar_notas_aluna():
    print('\nInsira os seguintes dados: ')
    nota_nome = input('Digite o nome da aluna: ')
    nota_sobrenome = input('Digite o sobrenome da aluna: ')
    nota = dataset.get((nota_nome,nota_sobrenome))
    nota_aluna = ('')
    if nota:
        notas = nota["Notas"]
        for item in notas:
            nota_aluna = nota_aluna + str(item) + (' ')
        print('Notas da aluna:',nota_aluna)
    else: 
     print('Não encontramos',nota_nome,nota_sobrenome,'no sistema. Escolha a opção abaixo para cadastrara a nova aluna.')
    
def consultar_status_aprovacao():
     print('\nInsira os seguintes dados: ')
     aprovacao_nome = input('Digite o nome da aluna: ')
     aprovacao_sobrenome = input('Digite o sobrenome da aluna: ')
     aprovacao = dataset.get((aprovacao_nome,aprovacao_sobrenome))
     if aprovacao:
        notas = aprovacao["Notas"]
        presenca = aprovacao["Presença"]
        participacao = aprovacao["Participação"]

        if len(notas) == 0:
            print('Não encontramos',aprovacao_nome,aprovacao_sobrenome,'no sistema. Escolha a opção abaixo para cadastrar a nova aluna.')
            return

        media = sum(notas) / len(notas)
        percentual = presenca.count(True) / len(presenca) * 100
        
        if participacao >= 6 and percentual >= 80 and media >= 6:
            status = 'APROVADA'
        elif 3 <= media < 6:
            status = 'RECUPERAÇÃO'   
        else:
            status = 'REPROVADA'

        print(f'Aluna {aprovacao_nome} {aprovacao_sobrenome} está {status} com média: {media:.2f}')
        if status == 'RECUPERAÇÃO':
            print(f'Aluna {aprovacao_nome} {aprovacao_sobrenome} precisa de nota para {media:.2f} aprovação.')
     else:
        print('Não encontramos',aprovacao_nome,aprovacao_sobrenome,'no sistema. Escolha a opção abaixo para cadastrar a nova aluna.')

main()