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


#Inserindo tupla com nome e sobrenome que será a chave principal no dicionário nova aluna   
def incluir_nova_aluna():
    inserir_nome_aluna = str (input ("Insira o primeiro nome da aluna: "))
    inserir_sobrenome_aluna = str (input ("Insira o sobrenome da aluna: "))
    nova_aluna = (inserir_nome_aluna, inserir_sobrenome_aluna)
    dataset [nova_aluna] = {}

   

    turma = incluir_turma (nova_aluna)
    notas = lista_notas (nova_aluna)
    presenca = lista_presenca(nova_aluna)
    nota_particpacao = particpacao (nova_aluna)
  

    salva_dados (nova_aluna,turma, notas, presenca, nota_particpacao)


    return nova_aluna


def incluir_turma (nova_aluna):
    print (f"A nova aluna {nova_aluna} foi incluída com sucesso \n")

    turma = str (input ("Insira a turma da aluna: "))
    dataset [(nova_aluna)] = [turma]

    

    print (f"A {turma} foi incluída no cadastro da aluna {nova_aluna}")

    return turma

def lista_notas (nova_aluna):

    print ("Insira uma nota de 1 a 10 cada matéria: \n")
    
    lista_notas = []

    for i in range (1,4):
        valor = float (input (f"Insira uma nota de 1 a 10 para a matéria {i}: \n"))
        lista_notas. append (valor)

    dataset [(nova_aluna)] = [lista_notas]

    print (f"As notas {lista_notas} foram incluídas no sistema! \n")

    return lista_notas


def lista_presenca (nova_aluna):

    lista_presenca_2 =[] 

    for i in range (1,6):
        valor = input(f"A aluna esteve presnete na aula {i}? Insira 'True' para presença e 'False' para ausência em cada aula:  \n")
        lista_presenca_2.append (valor)

    dataset [(nova_aluna)] = [lista_presenca_2] 

    print (f"A {lista_presenca_2} foi incluída no sistema com sucesso: ")

    return lista_presenca_2


def particpacao (nova_aluna):

    nota_participacao = float (input ("Insira a nota de participação de 1 a 10: "))

    dataset [(nova_aluna)]  = [nota_participacao]

    print (f"A nota de participação {nota_participacao} foi incluída com sucesso: ")

    return nota_participacao

def salva_dados (nova_aluna,incluir_turma, lista_notas,lista_presenca, participacao):
    
    dataset [nova_aluna] = {
        "Turma": incluir_turma,
        "Notas": lista_notas,
        "Presença": lista_presenca,
        "Participação": participacao

    }
    print ("Dados da aluna salvos com sucesso!")

#-------------------------------------------------------------------------------------------------------  
   
  
def consultar_lista_alunas():
    for nome,sobrenome in (dataset.keys()):
        print ((nome,sobrenome))
    

def consultar_faltas_aluna():
    busca_nome = input ("Digite o nome da aluna que deseja buscar: ")
    busca_sobrenome = input ("Digite o sobrenome da aluna que deseja buscar: ")
    if (busca_nome, busca_sobrenome) in dataset:
        consulta_faltas = dataset [(busca_nome, busca_sobrenome)] ["Presença"].count (False)
        print (f"A quantidade de faltas da aluna {busca_nome} {busca_sobrenome} é {consulta_faltas}")
 
    else:
        print ("Aluna não encontrada")
    return (busca_nome , busca_sobrenome)
    
    
def consultar_notas_aluna():
    busca_notas_nome = input ("Digite o nome da aluna que deseja buscar: ")
    busca_notas_sobrenome = input ("Digite o sobrenome da aluna que deseja buscar: ")
    if (busca_notas_nome, busca_notas_sobrenome) in dataset:
        consulta_notas = dataset [(busca_notas_nome,busca_notas_sobrenome)] ["Notas"]
        print (f"As notas da {busca_notas_nome} {busca_notas_sobrenome} são {consulta_notas}")

    else:
        print ("A aluna não foi encontrada")
        return (busca_notas_nome, busca_notas_sobrenome)    
    
    
def consultar_status_aprovacao():
    presenca3 = consultar_faltas_aluna
    nota_participacao = particpacao
    notas_aprovacao = consultar_notas_aluna

    busca_aprovacao_nome = input ("Digite o nome da aluna que deseja buscar: ")
    busca_aprovacao_sobrenome = input ("Digite o sobrenome da aluna que deseja buscar:")

    print ("_____________________________________________________________________________________\n")

    if (busca_aprovacao_nome, busca_aprovacao_sobrenome) in dataset:
        consulta_aprovacao_nota = dataset [(busca_aprovacao_nome, busca_aprovacao_sobrenome)] ["Notas"]
        media_notas = sum (consulta_aprovacao_nota)/ len (consulta_aprovacao_nota)
        media_notas_round = round (media_notas, 1)
        print (f"A média da aluna {busca_aprovacao_nome} {busca_aprovacao_sobrenome} é {media_notas_round}\n")

    if (busca_aprovacao_nome, busca_aprovacao_sobrenome) in dataset:
        consulta_aprovacao_falta = dataset [(busca_aprovacao_nome, busca_aprovacao_sobrenome)] ["Presença"].count (False)
        print  (f"O número de faltas da aluna {busca_aprovacao_nome} {busca_aprovacao_sobrenome} é {consulta_aprovacao_falta}\n")

    if (busca_aprovacao_nome, busca_aprovacao_sobrenome) in dataset:
        consulta_aprovacao_participacao = dataset [(busca_aprovacao_nome, busca_aprovacao_sobrenome)]["Participação"]
        print (f"A nota de participação da aluna {busca_aprovacao_nome} {busca_aprovacao_sobrenome} é {consulta_aprovacao_participacao}\n")

    print ("_____________________________________________________________________________________\n")    

    nota_de_corte = 6
    aprovada_nota = media_notas_round >= nota_de_corte and consulta_aprovacao_participacao >= nota_de_corte
    aprovada_falta = consulta_aprovacao_falta <= 1

    if aprovada_nota and aprovada_falta:
        print(f"A aluna {busca_aprovacao_nome} {busca_aprovacao_sobrenome} está APROVADA!")
    else:
        print(f"A aluna {busca_aprovacao_nome} {busca_aprovacao_sobrenome} está REPROVADA.")
 
    print ("_____________________________________________________________________________________\n")        

main()