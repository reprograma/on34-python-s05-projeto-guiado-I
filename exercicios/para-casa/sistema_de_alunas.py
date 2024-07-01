from dataset_alunas import dataset
import pprint

def main():
    print("\n₊ ⊹🫐 ✧˚. ᵎᵎ 🪻  Bem-vinda a Escola Reprograma ₊ ⊹🪻✧˚. ᵎᵎ 🫐 \n👩‍💼 Espero que esteja gostando da experiência de EducaTec.")
    print("\nSistema de informações de alunas")
    
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
                
            if codigo_opcao not in [1, 2, 3, 4, 5, 6]:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 6).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
            
        return codigo_opcao
    
def incluir_nova_aluna():
    print("Para incluir uma nova estudante responda as seguintes perguntas: ")
    nome = input("Digite o primeiro nome da aluna: ").strip().capitalize()
    sobrenome = input("Digite o sobrenome da aluna: ").strip().capitalize()
    turma = input("Digite a turma da aluna: ")
    notas = obter_notas()
    presenca = presencas()
    participacao = float(input("Digite a nota de participação da aluna: " ))

    for nota in notas: # notas é uma lista, por isso o uso do for
        if nota < 0 or nota > 10:
            print(f"A aluna não foi adicionada porque a nota {nota} está fora do intervalo permitido (0-10).")
            return False
    
    if len(presenca) != 5:
        print("A aluna não foi adicionada porque a lista de presença deve conter exatamente 5 respostas (aulas).")
        return False
    
    if participacao < 0 or participacao > 10:
        print("A aluna não foi adicionada porque a nota de participação está fora do intervalo permitido (0-10).")
        return False
    
    global dataset #considerando o dataset_alunas e definindo onde as informações serão adicionadas
    dataset[(nome, sobrenome)] = {
        "Turma": turma,
        "Notas": notas,
        "Presença": presenca,
        "Participação": participacao
    }
    
    print(f"Aluna {nome} {sobrenome} adicionada com sucesso!")

def obter_notas():
    notas = []
    for i in range(3): #range cria uma lista ordenada até o número passado como parâmetro
        while True: #não sabemos a quantidade de repetições
            entrada = input(f'⋆.˚ Insira a nota #{i+1}: ')
            try:
                nota = (round(float(entrada), 2))
                notas.append(nota)
                break #sai do while e segue com for
            except ValueError:
                print("❌🤖 Entrada inválida. Insira um número válido.")

    print(f'🧸ྀི  Confirmando as notas recebidas: {notas} 📂')
    return notas

def presencas():
    ata = []

    for i in range(5):
        while True:
            entrada = input(f'⋆.˚ Digite a presença da aluna do dia {i+1} (true/false): ').strip().lower()
            if entrada == 'true':
                presenca_dia = True
                ata.append(presenca_dia)
                break
            elif entrada == 'false':
                presenca_dia = False
                ata.append(presenca_dia)
                break
            else:
                print("Entrada inválida. Por favor, insira True ou False.")
    
    print(f'🧸ྀི  Confirmando as presenças recebidas: {ata} 📂')
    return ata
    
def consultar_lista_alunas():
    print("Lista de alunas:")
    for (nome, sobrenome), info in dataset.items():
        pprint.pprint(f"Nome: {nome} {sobrenome}, Turma: {info['Turma']}")
    
def consultar_faltas_aluna():
    nome = input("Digite o primeiro nome da aluna: ").strip().capitalize()
    sobrenome = input("Digite o sobrenome da aluna: ").strip().capitalize()
    chave = (nome, sobrenome)
    if chave in dataset:
        presenca = dataset[chave]["Presença"]
        faltas = presenca.count(False)
        print(f"A quantidade de faltas da aluna {nome} {sobrenome} é de {faltas} faltas.")
    else:
        print("Aluna não foi encontrada.")
    
def consultar_notas_aluna():
    nome = input("Digite o primeiro nome da aluna: ").strip().capitalize()
    sobrenome = input("Digite o sobrenome da aluna: ").strip().capitalize()
    chave = (nome, sobrenome)
    if chave in dataset:
        notas = dataset[chave]["Notas"]
        print(f"Notas da aluna {nome} {sobrenome}: {notas}")
    else:
        print("Aluna não foi encontrada.")
    
def consultar_status_aprovacao():
    nome = input("Digite o primeiro nome da aluna: ").strip().capitalize()
    sobrenome = input("Digite o sobrenome da aluna: ").strip().capitalize()
    chave = (nome, sobrenome)
    if chave in dataset:
        notas = dataset[chave]["Notas"]
        presenca = dataset[chave]["Presença"]
        participacao = dataset[chave]["Participação"]
        
        media = sum(notas) / len(notas)
        num_presenca = presenca.count(True)
        
        if media >= 6 and participacao >= 6 and num_presenca >= 0.8*len(presenca):
            print(f"A aluna {nome} {sobrenome} foi aprovada! Sua média é de {media}.")
        else:
            print(f"A aluna {nome} {sobrenome} não foi aprovada. Sua média é de {media}, nota de participação é de {participacao} e presença é {num_presenca}.")
    else:
        print("Aluna não foi encontrada.")

main()