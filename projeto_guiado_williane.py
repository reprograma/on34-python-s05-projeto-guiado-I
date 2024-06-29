dataset = {}

print("-- Calculadora para média de notas -- \nPara realizar o cálculo, digite os dados da aluna e as três notas que deseja calcular a média. \n Não são permitidos: \n⇨ Valores que não sejam números para as notas\n⇨ Inserir número negativo")

def dados_aluna ():
    global nome
    nome = input("Insira o nome da aluna: ")
    turma = input("Insira a turma da aluna: ")

    quantidade_notas = input("Insira a quantidade de notas: ")
    notas_aluna = []
 
    for contador in range(int(quantidade_notas)):
        while True:
            entrada = input(f"Insira a nota #{contador + 1}: ")
            try:
                nota = float(entrada)
                notas_aluna.append(nota)
                break
            except ValueError:
                print("Entrada inválida")
    
    print(f"Notas inseridas: {notas_aluna}")

    media_notas(nome, turma, notas_aluna)
    
def media_notas(nome, turma, notas_aluna):
    media = sum(notas_aluna)/ len(notas_aluna)
            
    if media < 6:
        print("A aluna", nome, "foi reprovada com média igual a:", round(media, 2))
            
    else:
        print("A aluna", nome, "foi aprovada com média igual a:", round(media, 2))

    continuar_programa = input("Digite 1 se deseja calcular uma nova média ou 2 caso deseje parar: ")

    if continuar_programa == '1':
        dados_aluna()
    else:
        print("Programa encerrado")
    
    salvar_dados_aluna(nome, turma, notas_aluna, media)   

def salvar_dados_aluna(nome, turma, notas_aluna, media):
    chave = (nome)
    dataset[chave] = {
        "Turma" : turma,
        "Notas aluna": notas_aluna,
        "Media aluna": media       
        }
    print(f"Dados aluna {chave}: {dataset[chave]}")

dados_aluna()