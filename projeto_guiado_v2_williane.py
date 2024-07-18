# Definindo o dataset diretamente no programa
dataset = {}

def main():
    print("\n---  Seja bem vinda à Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1:
            incluir_nova_aluna()
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

def obter_opcao():
    while True:
        try:
            codigo_opcao = int(input("\nEscolha uma opção:\n"
                                    "1 - Incluir uma nova aluna\n"
                                    "2 - Consultar lista de alunas\n"
                                    "3 - Consultar faltas da aluna\n"
                                    "4 - Consultar notas da aluna\n"
                                    "5 - Consultar status de aprovação\n"
                                    "6 - Sair do sistema\n"
                                    "Opção: "))
            if codigo_opcao in [1, 2, 3, 4, 5, 6]:
                return codigo_opcao
            else:
                print("Opção inválida. Por favor, escolha uma opção válida (1 a 6).\n")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")

def incluir_nova_aluna():
    nome = input("\nDigite o nome completo da aluna: ")
    sobrenome = input("Digite o sobrenome da aluna: ")
    turma = input("Digite a turma da aluna: ")
    
    # Coletando as notas
    quantidade_notas = int(input("Quantas notas serão inseridas? "))
    notas_aluna = []
    for i in range(quantidade_notas):
        while True:
            try:
                nota = float(input(f"Insira a nota #{i+1}: "))
                if nota < 0 or nota > 10:
                    print("Nota fora do intervalo permitido (0-10). Tente novamente.")
                else:
                    notas_aluna.append(nota)
                    break
            except ValueError:
                print("Valor inválido. Insira um número válido para a nota.")
    
    # Coletando a presença (faltas)
    quantidade_dias = int(input("Quantos dias de presença serão inseridos? "))
    presenca_aluna = []
    for i in range(quantidade_dias):
        while True:
            try:
                presenca = input(f"Informar presença no dia #{i+1} (True/False): ").strip().lower()
                if presenca not in ['true', 'false']:
                    raise ValueError("Valor inválido. Insira 'True' ou 'False'.")
                else:
                    presenca_aluna.append(presenca == 'true')
                    break
            except ValueError as e:
                print(e)
    
    # Coletando a nota de participação
    while True:
        try:
            participacao = float(input("Insira a nota de participação da aluna: "))
            if participacao < 0 or participacao > 10:
                raise ValueError("Nota de participação fora do intervalo permitido (0-10).")
            else:
                break
        except ValueError as e:
            print(e)
    
    # Calculando o status de aprovação
    media = sum(notas_aluna) / len(notas_aluna)
    percent_presenca = presenca_aluna.count(True) / len(presenca_aluna) * 100
    
    if participacao >= 6 and percent_presenca >= 80 and media >= 6:
        status = "Aprovada"
    elif 3 <= media < 6:
        status = "Recuperação"
        fez_recuperacao = input("\nA média da aluna está baixa. Ela fez prova de recuperação? ").lower()
        if fez_recuperacao == 'sim':
            while True:
                try:
                    nota_recuperacao = float(input("Insira a nota de recuperação: "))
                    if nota_recuperacao < 0 or nota_recuperacao > 10:
                        raise ValueError("Nota de recuperação fora do intervalo permitido (0-10).")
                    else:
                        break
                except ValueError as e:
                    print(e)
        else:
            nota_recuperacao = None
            print("Então essa aluna será reprovada por média.")
    else:
        status = "Reprovada"
        nota_recuperacao = None
    
    # Adicionando a aluna ao dataset
    chave = f"{nome} {sobrenome}"
    dataset[chave] = {
        "Turma": turma,
        "Notas": notas_aluna,
        "Presença": presenca_aluna,
        "Nota de Participação": participacao,
        "Status": status,
        "Média Final": round(media, 2)  # Arredonda a média final para duas casas decimais
    }
    
    # Exibindo o status de aprovação da aluna
    print(f"\nStatus de aprovação da aluna '{chave}': {status}")
    print(f"Média final: {media:.2f}")
    if status == "Recuperação":
        print(f"Nota de recuperação: {nota_recuperacao:.2f}")
    
    print(f"\nAluna '{chave}' adicionada com sucesso!")

def consultar_lista_alunas():
    if not dataset:
        print("\nNão há alunas cadastradas.")
    else:
        print("\nLista de alunas cadastradas:")
        for chave in dataset.keys():
            print(chave)

def consultar_faltas_aluna():
    nome_aluna = input("\nDigite o nome completo da aluna para consultar as faltas: ")
    if nome_aluna in dataset:
        faltas = dataset[nome_aluna]["Presença"].count(False)
        print(f"\nA aluna '{nome_aluna}' possui {faltas} falta(s).")
    else:
        print(f"\nAluna '{nome_aluna}' não encontrada.")

def consultar_notas_aluna():
    nome_aluna = input("\nDigite o nome completo da aluna para consultar as notas: ")
    if nome_aluna in dataset:
        notas = dataset[nome_aluna]["Notas"]
        print(f"\nNotas da aluna '{nome_aluna}': {notas}")
    else:
        print(f"\nAluna '{nome_aluna}' não encontrada.")

def consultar_status_aprovacao():
    nome_aluna = input("\nDigite o nome completo da aluna para consultar o status de aprovação: ")
    if nome_aluna in dataset:
        notas = dataset[nome_aluna]["Notas"]
        presenca = dataset[nome_aluna]["Presença"]
        participacao = dataset[nome_aluna]["Nota de Participação"]
        
        if len(notas) == 0:
            print("\nNão há notas registradas para esta aluna.")
            return
        
        media = sum(notas) / len(notas)
        percent_presenca = presenca.count(True) / len(presenca) * 100
        
        if participacao >= 6 and percent_presenca >= 80 and media >= 6:
            status = "Aprovada"
        elif 3 <= media < 6:
            status = "Recuperação"
        else:
            status = "Reprovada"
        
        print(f"\nStatus de aprovação da aluna '{nome_aluna}': {status}")
        print(f"Média final: {media:.2f}")
        if status == "Recuperação":
            print(f"Nota de recuperação necessária para aprovação: {media:.2f}")
    else:
        print(f"\nAluna '{nome_aluna}' não encontrada.")

if __name__ == "__main__":
    main()
