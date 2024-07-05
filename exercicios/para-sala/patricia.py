dataset = {} # Dicionario com escopo global

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---\n")
    print("Aqui você pode calcular a aprovação de uma aluna.\n")
    
    while True:
        nome = obter_dados_aluna() # Chamo a função de pegar dados da aluna
        media = obter_media(nome) # Chamo a função de calcular a média da aluna
        resultado = obter_resultado(media)
        
        print(f"A aluna {nome} da turma {dataset[nome]['Turma']} está {resultado}. A média dela foi: {media:.2f}.")
        
def obter_dados_aluna():
    print("Insira os seguintes dados: ")
    nome = input("Nome da aluna: ") # Recebo nome da aluna
    turma = input("Turma da aluna: ") # Recebo nome da turma
    
    notas = obter_notas() # Chamo a função de pegar as notas para alimentar minha lista "notas"
    notas_presenca = obter_presenca(len(notas)) # Chamo a função de pegar a presença
    nota_participacao = obter_participacao() # Chamo a função de pegar a nota de participação
    
    salvar_dados_aluna(nome, turma, notas, notas_presenca, nota_participacao)
    
    return nome
    
def obter_notas():
    quantidade_notas = input("Quantidade de notas: ") # Recebo a quantidade de notas
    while not quantidade_notas.isdigit() or int(quantidade_notas) <= 0:
        print("Entrada inválida. Por favor, insira um número válido e positivo.")
        quantidade_notas = input("Quantidade de notas: ")

    notas = [] # Criei uma lista para receber as notas
    
    for contador in range(int(quantidade_notas)): 
        while True: # Usamos quando não sabemos a quantidade de repetições    
            entrada = input(f"Insira a nota #{contador + 1}: ") # Para cada nota, insiro o valor - {contador + 1} indica a nota atual
            try: # Faço uma tentativa de adicionar uma nota na lista
                nota = float(entrada) # Converto a entrada em float
                if 0 <= nota <= 10:
                    notas.append(nota) # Insiro a nota na minha lista "notas"
                    break # Caso ok, posso sair do loop e seguir com for
                else:
                    print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
            except ValueError: # Caso dê um problema, ele volta ao início do while e tenta novamente
                print("Entrada inválida. Por favor, insira um número válido.")
    
    return notas

def obter_presenca(quantidade_notas):
    presenca = [] # Criei uma lista para receber a presença
    for contador in range(quantidade_notas):
        while True:
            entrada = input(f"A aluna esteve presente na aula #{contador + 1}? (True/False): ")
            if entrada.lower() in ["true", "false"]:
                presenca.append(entrada.lower() == "true")
                break
            else:
                print("Entrada inválida. Por favor, insira True ou False.")
    return presenca

def obter_participacao():
    while True:
        entrada = input("Insira a nota de participação da aluna (0 a 10): ")
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida. Por favor, insira um valor entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def salvar_dados_aluna(nome, turma, notas, presenca, participacao):
    dataset[nome] = { # Adiciono no dicionário os dados que peguei na função obter_dados_aluna
        "Turma": turma,
        "Notas": notas,
        "Presenca": presenca,
        "Participacao": participacao
    }

def obter_media(nome):
    notas = dataset[nome]["Notas"] # Recupera a lista com as notas
    participacao = dataset[nome]["Participacao"]
    
    media_notas = sum(notas) / len(notas)
    media_final = (media_notas * 0.8) + (participacao * 0.2)
    return media_final

def obter_resultado(media):
    if media >= 6:
        return "Aprovado"
    else:
        return "Reprovado"

main()
