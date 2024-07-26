from dataset_alunas import dataset

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

def obtem_nome(pergunta):
  while True:
    entrada_usuário = str(input(pergunta)).lstrip().rstrip()
    if entrada_usuário.replace(" ", "").isalpha() and entrada_usuário != "":
      break
    else:
      print("Digite um nome válido")
  return entrada_usuário

def obtem_nota(numero_nota, tipo):
  status = 0
  while status == 0:
    try:
        if tipo == 'n':
            nota = float(input(f"Digite a nota {numero_nota} da aluna) (0 a 10): "))
        else:
            nota = float(input(f"Digite a nota de participação da aluna) (0 a 10): "))
        if nota >= 0 and nota <= 10:
            status = 1
        else:
            print("Digite uma nota válida entre 0 e 10")
    except:
      print(" Entrada inválida. Digite um número inteiro entre 0 e 10")
  return nota

def obtem_presenca(num_presenca):
  contador = 0
  while contador == 0:
    presenca = input(f"Digite a presença {num_presenca} da aluna apenas com (True ou False): ").strip()
    if presenca.lower() in ['true', 'false']:
      presenca = presenca.lower() == 'true'
      contador = 1
    else:
      print("Entrada inválida, informe a presença apenas com (True ou False)")
  return presenca


def incluir_nova_aluna():
    print('Iniciando cadastro de nova aluna ')
    notas = []
    presencas = []

    nome = obtem_nome(" Informe o nome da aluna para cadastro: ").title()
    sobrenome = obtem_nome (" Informe o sobrenome da aluna para cadastro: ").title()
    nome_sobrenome = (nome, sobrenome)

    while True:
        turma = (input ('Informe a turma da aluna com A / B ou C: ')).strip().upper()
        if turma == "A" or turma == "B" or  turma == 'C':
            break
        else:
            print('Entrada inválida. Informe uma turma com ( A / B ou C )')


    for i in range (1, 4):
        nota = obtem_nota(i, 'n')
        notas.append(nota) 

    for i in range (1, 6 ):
        presenca = obtem_presenca(i)
        presencas.append(presenca) 

    participacao = obtem_nota(0,'p')

    dataset[nome_sobrenome] = {
        "Turma": turma ,
        "Notas": notas,
        "Presença": presencas ,
        "Participação": participacao
    }
    print("Aluna cadastrada com sucesso ")


def consultar_lista_alunas():
    print(' Segue a lista de alunas cadastradas ')
    if len(dataset) != 0:
        for nome in dataset.keys(): 
            print(nome[0])
    else:
        print("Não existem alunas cadastradas")

def consultar_faltas_aluna():
    try:
        nome_completo = tuple(obtem_nome('Informe o nome completo da aluna: ').title().split())

        faltas_alunas = dataset[nome_completo]["Presença"]

        numero_faltas = faltas_alunas.count(False)
        print(f' A aluna {nome_completo[0]} , tem {numero_faltas} faltas')
    except KeyError:
        print(" Não localizado. Por favor informe o nome completo de uma aluna: ")


def consultar_notas_aluna():
    try:
        nome_completo = tuple(obtem_nome('Informe o nome completo da aluna: ').title().split())

        notas_aluna = dataset[nome_completo]['Notas']

        conte_nota = 0
        for nota in notas_aluna:
            conte_nota += 1
            print(f' A nota {conte_nota} da aluna {nome_completo[0]} é: {nota}')

    except KeyError:
        print("Não localizado. Por favor informe o nome completo de uma aluna: ")


def consultar_status_aprovacao():
    try:
        nome_completo = tuple(obtem_nome('Informe o nome completo da aluna: ').title().split())

        notas_aluna = dataset[nome_completo]['Notas']
        media_aluna = round(sum(notas_aluna)/len(notas_aluna),1)


        presença_aluna = dataset[nome_completo]['Presença']
        numero_presenca = presença_aluna.count(True)
        porcentagem_presenca = round((numero_presenca/len(presença_aluna)) *100)

        nota_participação = dataset[nome_completo]['Participação']

        if media_aluna >=6 and porcentagem_presenca >= 80 and nota_participação >=6:
            print(f' Aluna aprovada. \n Média Final: {media_aluna}')
        elif media_aluna <6:
            print(f' Aluna Reprovada por média inferior a 6.0 \n Média Final Obtida: {media_aluna}')
        elif nota_participação < 6:
            print(f' Aluna Reprovada por nota de participação inferior a 6.0 \n Nota de participação obtida: {nota_participação}. \n Média Final: {media_aluna} ')
        else:
            print(f' Aluna Reprovada por presença inferior a 80%.\n A presença da aluna foi de {porcentagem_presenca}% \n Média Final: {media_aluna}')
    except KeyError:
        print("Não localizado. Por favor informe o nome completo de uma aluna")

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
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
            print("Encerrando o programa...");
            break

main()