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
    print("Por favor insira estes dados: ")
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    turma = input("Turma da aluna: ")
    lista_presenca = obter_presenca()
    nota_participacao = float(input("Participação da aluna: "))
    notas = obter_notas()

    salvar_dados_aluna(nome, sobrenome, turma, lista_presenca, nota_participacao, notas)
    print("Aluna adicionada com sucesso!")

def obter_presenca():
    quantidade_aulas = input("Quantidade de aulas: ")
    aulas = []

    for contador in range(int(quantidade_aulas)):
        while True:
            entrada = input(f"Insira a presença da aula #{contador + 1} (True ou False): ")
            if entrada in ["True", "False"]:
                presenca = entrada == "True"
                aulas.append(presenca)
                break
            else:
                print("Entrada inválida. Por favor, insira True ou False.")

    return aulas

def obter_notas():
    quantidade_notas = input("Quantidade de notas: ")
    notas = []

    for contador in range(int(quantidade_notas)):
        while True:
            entrada = input(f"Insira a nota #{contador + 1}: ")
            try:
                nota = float(entrada)
                if nota >= 0 and nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
                    continue
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
             

    return notas

def salvar_dados_aluna(nome, sobrenome, turma, lista_presenca, nota_participacao, notas):
    chave = f"{nome} {sobrenome}"
    dataset[chave] = {
        "Nome": nome,
        "Sobrenome": sobrenome,
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_presenca,
        "Participação": nota_participacao
    }

def consultar_lista_alunas():
    if not dataset:
        print("Nenhuma aluna cadastrada.")
        return

    print("\nLista de alunas:")
    for nome in dataset:
        print(f"- {nome}")



def consultar_faltas_aluna():
    try:
        nome = input("Nome da aluna: ")
        sobrenome = input("Sobrenome da aluna: ")
        lista_presenca = dataset[(nome, sobrenome)]["Presença"]
        if (nome, sobrenome) in dataset:
            print(f"A aluna {nome} {sobrenome} está com {lista_presenca}")
        
    except:
        print("Aluna não encontrada!")    

    
def consultar_notas_aluna():
    try:
        nome = input("Nome da aluna: ")
        sobrenome = input("Sobrenome da aluna: ")
        notas_aluna = dataset[(nome, sobrenome)]["Notas"]
        if (nome, sobrenome) in dataset:
            print(f"A aluna {nome} {sobrenome} está com essas notas {notas_aluna}")

    except:
        print("Aluna não encontrada!")        

    
    
def consultar_status_aprovacao():
    while True:
        nome = input("Nome da aluna: ")
        sobrenome = input("Sobrenome da aluna: ")
        
        chave = (nome, sobrenome)
        
        if chave in dataset:
            dados = dataset[chave]
            notas = dados["Notas"]
            soma = sum(notas)
            participacao = dados["Participação"]
            qtd_presenca = sum(dados["Presença"])
            percentual_presenca = qtd_presenca / len(dados["Presença"])
            nota_media = soma / len(notas)

            print(f"A aluna {nome} {sobrenome} está com a nota média {nota_media:.2f}")
            if nota_media >= 6 and percentual_presenca >= 0.80 and participacao >= 6:
                print("Aluna aprovada!!")
            else:
                print("Aluna reprovada!!")
        else:
            print("Aluna não encontrada no dataset.")
        
        continuar = input("Deseja consultar outra aluna? (s/n): ")
        if continuar.lower() != 's':
            break
        


main()