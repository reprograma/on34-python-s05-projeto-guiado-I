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
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 6).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna():
    chave_nome = obter_chave_nome() #Chamo uma função que retorna uma tupla com nome e sobrenome, Ex: ('Mayumi', 'Shingaki')
    turma = input('Insira a turma: ') #Recebo a turma
    notas = obter_lista_notas() #Chamo a função que retorna uma lista de notas, Ex: [7, 8, 9]
    presenca = obter_lista_presenca() #Chamo uma função que retorna uma lista de booleanos, representando a presença, Ex: [True, False, True, True, True]
    nota_participacao = input('Insira a nota de participação: ') #Recebo a nota de participação
    nota_participacao = validar_valor_nota(nota_participacao) #Validar se o valor da nota de participação é válido
    
    salvar_dados_aluna(chave_nome, turma, notas, presenca, nota_participacao) #Salvo os no dataset
    print('Dados da aluna salvos com sucesso! :)')
  
def obter_chave_nome():
    nome = input('Qual o nome da aluna?: ').title() #Recebe o nome e transforma a primeira letra em caixa alta
    sobrenome = input(f'Qual sobrenome da {nome}?: ').title()
    return (nome, sobrenome)

def obter_lista_notas():
    lista_notas = []
    quantidade_notas = 3
    
    for indice in range(1, quantidade_notas + 1): #Percorro um laço de repetição para a quantidade de notas
        nota = input(f'Digite a nota {indice}/{quantidade_notas} da aluna (de 0 a 10): ')
        nota = validar_valor_nota(nota) #Chamo a função de valida se o valor que inseri é um número entre 0 e 10
        lista_notas.append(nota) #Adiciono a nota na lista

    return lista_notas

def validar_valor_nota(nota):
    while True: #Enquanto o valor não for válido, vou continuar rodando esse loop
        try:
            nota = float(nota) #Tento converter o valor que recebi em float
            if nota >= 0 and nota <= 10: #Valido se o valor da nota está entre 0 e 10
                return nota #Se validei o intervalo e consegui converter sem erros, eu retorno o valor da nota            
            nota = input('Digite uma nota válida de 0 a 10: ') #Caso não consiga
            
        except ValueError: #Caso seja inserido uma letra, cai nessa exception
            nota = input('Digite um número válido: ') #Peço para inserir novamente
            
def obter_lista_presenca():
    lista_de_presenca = [] #Crio uma lista inicial para a presença
    quantidade_aulas = 5
    
    for indice in range(1, quantidade_aulas + 1): #Percorro um lado de repetição para a quantidade de aulas 
        while True: 
            presenca_aula = input(f'Aluna compareceu na aula #{indice} do total de {quantidade_aulas} aulas? Sim/Não: ').lower().strip() #Recebo sim ou não para a aula atual, lower torna todas as letras em letra minúscula e strip tira espaços no início e fim da string
            if presenca_aula == 'sim': #Se a presença for sim
                lista_de_presenca.append(True) #Insiro True na minha lista
                break
            elif presenca_aula == 'nao' or presenca_aula == 'não': #Se a presença for não
                lista_de_presenca.append(False) #Insiro False na lista
                break
            else:
                print('Dado inválido. Por favor, insira Sim ou Não.')
                
    return lista_de_presenca

def salvar_dados_aluna(chave_nome, turma, notas, presenca, nota_participacao):
    dataset[chave_nome] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presenca,
        "Participação": nota_participacao
    }
            
def consultar_lista_alunas():
    for nome, sobrenome in dataset:
        print(f'. {nome} {sobrenome}')
    
def consultar_faltas_aluna():
    chave_aluna = obter_chave_nome()
    quantidade_faltas = dataset[chave_aluna]["Presença"].count(False) #Recupero a quantidade de itens com False (faltas)
    print(f'\nA aluna {chave_aluna[0]} está com {quantidade_faltas} faltas.')
    
def consultar_notas_aluna():
    chave_aluna = obter_chave_nome()
    lista_notas = dataset[chave_aluna]["Notas"]
    
    print('A relação de notas da aluna é: ')
    for indice, nota in enumerate(lista_notas, start = 1): #Crio um iterador que gera uma tupla de dois elementos (indice e nota), pedi pra começar em 1
        print(f'Nota #{indice}: {nota}')    
    
    
def consultar_status_aprovacao():
    chave_aluna = obter_chave_nome()
    nota_final = calcular_nota_final(chave_aluna) #Chamo a função que calcula e retorna a minha nota final
    percentual_presenca = calcular_presenca(chave_aluna) #Chamo a função que calcula o percentual de presença
    nota_participacao = dataset[chave_aluna]["Participação"]
    
    if nota_final >= 6 and percentual_presenca >= 80 and nota_participacao >= 6:
        imprimir_mensagem_status('Aprovada', nota_final, percentual_presenca, nota_participacao)
    else:
        imprimir_mensagem_status('Reprovada', nota_final, percentual_presenca, nota_participacao)

def calcular_nota_final(nome):
    lista_notas = dataset[nome]["Notas"]
    return sum(lista_notas) / len(lista_notas)

def calcular_presenca(nome):
    lista_presenca = dataset[nome]["Presença"]
    return lista_presenca.count(True) / len(lista_presenca) * 100

def imprimir_mensagem_status(resultado, nota, presenca, participacao):
    print('--------------------------------------------------------')
    if resultado == 'Aprovada':
        print('✅ A aluna está APROVADA, com os seguintes dados: ')
    else: 
        print('❌ A aluna está REPROVADA, com os seguintes dados: ')
        
    print(f'Média: {nota}')
    print(f'Percentual de presença: {presenca}')
    print(f'Participação: {participacao}')
    
    print(f'\nCritérios de avaliação:')
    print(f'Média: Maior ou igual a 6')
    print(f'Presença: Maior ou igual a 80%')
    print(f'Nota de participação: Maior ou igual a 8')
    print('--------------------------------------------------------')
    
consultar_status_aprovacao()