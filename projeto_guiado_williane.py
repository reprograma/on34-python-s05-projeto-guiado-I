dataset = {}

print("-- Calculadora para média de notas -- \nPara realizar o cálculo, digite os dados da aluna e as notas que deseja calcular a média. \n Não são permitidos: \n⇨ Valores que não sejam números para as notas\n⇨ Inserir número negativo")

def dados_aluna ():
    nome = input("\nQual é o nome da aluna? ")
    turma = input("Qual é a turma da aluna? ")
    participacao = float(input("Qual a nota de participação da aluna? "))
    quantidade_notas = input("\nQuantas notas você deseja inserir para calcular a média? ")
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
    print(f"As notas inseridas foram: {notas_aluna}")

    inserir_frequencia(nome, turma, participacao, notas_aluna)

def inserir_frequencia(nome, turma, participacao, notas_aluna):
    frequencia = input("\nVocê deseja inserir a frequência da aluna? Digite 1 se sim e 2 caso não queira: ")
       
    if frequencia == '1':
        quantidade_dias_frequencia = int(input("Quantos dias de frequência serão inseridos? "))

        faltas_aluna = []
        for contador2 in range(quantidade_dias_frequencia):
            while True:
                print("Para registrar as faltas, digite True caso a aluna tenha faltado no dia e False caso ela não tenha faltado")
                entrada2 = input(f"Insira a falta #{contador2 + 1}: ").lower()  # Aceita 'true' ou 'false'
                falta_aluna = entrada2 == 'true'
                faltas_aluna.append(falta_aluna)
                break

        if quantidade_dias_frequencia > 0:
            percent_faltas = round((faltas_aluna.count(True)/ len(faltas_aluna)) * 100, 2)
            print(f"O percentual de presença da aluna é de: {percent_faltas}%")
        
        else:
            percent_faltas = 0
            faltas_aluna = []
    else:
        faltas_aluna = None
        percent_faltas = None
        print("\nEntão vamos seguir com os cálculos das médias!\n")

    media_notas(nome, turma, participacao, notas_aluna, faltas_aluna, percent_faltas)
    
def media_notas(nome, turma, participacao, notas_aluna, faltas_aluna, percent_faltas):
    media = ((sum(notas_aluna)/ len(notas_aluna))*0.8) + (participacao * 0.2)

    if  media < 3:
        nota_recuperacao = None
        print("\nA aluna", nome, "foi reprovada com média igual a:", round(media, 2))
        status_aluna = "Reprovada"

    elif  3 < media < 6:
        print("\nA aluna", nome, "foi para recuperação com média igual a:", round(media, 2))
        status_aluna = "Recuperação"
        fez_recuperacao = input("\nA média da aluna está baixa. Ela fez prova de recuperação? ").lower()
        if fez_recuperacao == 'sim':
                nota_recuperacao = float(input("Insira a nota de recuperação: "))
        else:
            nota_recuperacao = None
            print("Então essa aluna será reprovada por média.")


    else:
        print("\nA aluna", nome, "foi aprovada com média igual a:", round(media, 2))
        nota_recuperacao = None
        status_aluna = "Aprovada"

    continuar_programa = input("\nDigite 1 se deseja calcular uma nova média ou 2 caso deseje parar: ")

    if continuar_programa == '1':
        dados_aluna()
    else:
        print("Programa encerrado")
    
    salvar_dados_aluna(nome, turma, participacao, notas_aluna, status_aluna, media, faltas_aluna, percent_faltas, nota_recuperacao)   

def salvar_dados_aluna(nome, turma, participacao, notas_aluna, status_aluna, media, faltas_aluna, percent_faltas, nota_recuperacao):
    chave = (nome)
    dataset[chave] = {
        "Turma" : turma,
        "Nota participação": participacao,
        "Notas aluna": notas_aluna,
        "Status": status_aluna,
        "Media aluna": round(media, 2),
        "Faltas aluna" : faltas_aluna,
        "Percentual de faltas": percent_faltas,
        "Nota recuperação": nota_recuperacao
        }
    print(f"Dados aluna {chave}: {dataset[chave]}")

dados_aluna()