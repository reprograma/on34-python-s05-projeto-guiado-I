dataset = {}  # Dicionário com escopo global para armazenar os dados das alunas, usado função, whilw, if, else, for, try, except ( Com os MVPS de 1 a 5 )

def main():
    print("\n--- Seja bem vinda à Escola do Reprograma! ---\n")
    print("Aqui você pode calcular a aprovação de uma aluna.\n")

    while True:
        nome = input("Nome da aluna (ou digite 'sair' para encerrar): ")
        if nome.lower() == 'sair':
            break

        turma = input("Turma da aluna: ")
        notas = obter_notas()
        frequencia = obter_frequencia()
        presencas = obter_presenca()

        salvar_dados_aluna(nome, turma, notas, frequencia, presencas)

        media_notas = sum(notas) / len(notas)
        media_ponderada = (media_notas * 0.8) + (frequencia * 0.2 / 100)

        if media_ponderada >= 6:
            resultado = "Aprovado"
        elif media_ponderada >= 4:
            resultado = "Recuperação"
        else:
            resultado = "Reprovado"

        if resultado == "Recuperação":
            fez_recuperacao = input("A aluna fez prova de recuperação? (sim/não): ").strip().lower()
            if fez_recuperacao == 'sim':
                nota_recuperacao = obter_nota_recuperacao()
                if nota_recuperacao > 0:
                    menor_nota = min(notas)
                    if nota_recuperacao > menor_nota:
                        notas[notas.index(menor_nota)] = nota_recuperacao
                        media_notas = sum(notas) / len(notas)
                        media_ponderada = (media_notas * 0.8) + (frequencia * 0.2 / 100)

                if media_ponderada >= 6:
                    resultado = "Aprovado"
                else:
                    resultado = "Reprovado"

        print(f"A aluna {nome} da turma {turma} está {resultado}.")
        print(f"Média das notas: {media_notas:.2f}")
        print(f"Frequência: {frequencia}%")
        print(f"Média Ponderada: {media_ponderada:.2f}\n")

def obter_notas(): #Obterndo notas 
    while True:
        try:
            quantidade = int(input("Quantidade de notas: "))
            notas = []
            for i in range(quantidade):
                nota = float(input(f"Insira a nota #{i + 1}: "))
                notas.append(nota)
            return notas
        except ValueError:
            print("Por favor, insira um número válido para a quantidade e notas.")

def obter_frequencia():
    while True:
        try:
            frequencia = float(input("Digite a frequência da aluna (em %): "))
            if 0 <= frequencia <= 100:
                return frequencia
            else:
                print("Frequência deve estar entre 0% e 100%. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido para a frequência.")

def obter_presenca(): # Obtendo presença.
    while True:
        try:
            quantidade_aulas = int(input("Quantidade de aulas: "))
            break
        except ValueError:
            print("Por favor, insira um número válido para a quantidade de aulas.")
    presencas = []
    for i in range(quantidade_aulas):
        while True:
            entrada = input(f"Insira a presença da aula #{i + 1} (True/False): ").strip().lower()
            if entrada in ['true', 'false']:
                presenca = entrada == 'true'
                presencas.append(presenca)
                break
            else:
                print("Entrada inválida. Por favor, insira True ou False.")
    
    return presencas

def obter_nota_recuperacao(): # Obtendo recuperação.
    while True:
        try:
            nota_recuperacao = float(input("Digite a nota da prova de recuperação: "))
            if 0 <= nota_recuperacao <= 10:
                return nota_recuperacao
            else:
                print("Nota de recuperação deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido para a nota de recuperação.")

def salvar_dados_aluna(nome, turma, notas, frequencia, presencas): # Dados alunos salvos 
    dataset[nome] = {
        "Turma": turma,
        "Notas": notas,
        "Frequencia": frequencia,
        "Presencas": presencas,
    }

main()
