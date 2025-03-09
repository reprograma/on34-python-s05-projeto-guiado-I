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
            print("Entrada inválida. Por favor, digite um número inteiro de 1 a 6.\n")
            
        return codigo_opcao
      
def lista_de_presenca():
    qntdd_de_aulas = input("Quantas aulas a aluna teve? ") 
    aulas = [] 
    for contador in range(int(qntdd_de_aulas)): 
        while True:    
            entrada = input(f"Insira a presença da aula. Considere True=presença e False=falta, #{contador + 1}: ")
            try: 
                presenca = eval(entrada)
                aulas.append(presenca) 
                break 
            except NameError: 
                print("Entrada inválida. Por favor, insira True ou False.")
    return presenca
  
def lista_de_notas():
    qntdd_de_notas = (input("Quantas notas quer inserir? "))
    notas = []
    
    for contador in range(int(qntdd_de_notas)): 
        while True:  
            entrada = input(f"Insira a nota {contador + 1}: ")
            try: 
                nota = float(entrada) 
                notas.append(nota)
                break
            except:
                print("Entrada inválida. Insira uma nota de 0 a 10. ")
    return notas
    
def incluir_nova_aluna():
    print("Insira  os seguintes dados: ")
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome: ")
    turma = input("Turma: ")
    notas = lista_de_notas()
    lista_presenca = lista_de_presenca()
           
    while True:  
          nota_participacao = (input("Qual foi a nota de participação da aluna? "))
          try: 
                nota_participacao = float(nota_participacao) 
                break
          except:
                print("Entrada inválida. Insira uma nota de 0 a 10. ")  
            
    print(f"A aluna {nome} {sobrenome} foi cadastrada com sucesso: ")
     
    salvar_dados_aluna(nome, sobrenome, turma, notas, lista_presenca, nota_participacao)
    return nome

def salvar_dados_aluna(nome, sobrenome, turma, notas, lista_presenca, nota_participacao):
    chave = (nome, sobrenome)
    dataset[chave] = { 
        "Turma": turma,
        "Notas": notas,
        "Presença": lista_presenca,
        "Participação": nota_participacao
    } 
  
def consultar_lista_alunas():
    print(dataset.keys())
    for nome, sobrenome in dataset.keys():
        print(f'- {nome} {sobrenome}')
    
def consultar_faltas_aluna():
  try:
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    quantidade_faltas = dataset[(nome,sobrenome)]["Presença"].count(False)
    print(f"A aluna {nome} {sobrenome} está com {quantidade_faltas} falta(s).")
    
  except:
    print("Aluna não encontrada. ")
    
def consultar_notas_aluna():
  try:
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    lista_de_notas = dataset[(nome,sobrenome)]["Notas"]
    print(f"A aluna {nome} {sobrenome} está com {lista_de_notas}")
    
  except:
    print("Aluna não encontrada. ")
 
def consultar_status_aprovacao():
  nome = input("Qual nome da aluna gostaria de consultar o status de aprovação? : ")
  sobrenome = input("Qual sobrenome da aluna gostaria de consultar o status de aprovação? : ")
  try:
        notas = dataset[(nome, sobrenome)]["Notas"]
        participacao = dataset[(nome, sobrenome)]["Participação"]
        media = sum(notas) / len(notas)
        presenca = dataset[(nome, sobrenome)]["Presença"]
        percentual_presenca = (presenca.count(True) / len(presenca)) * 100
        
        if percentual_presenca < 80:
          print("A aluna está reprovada por falta. ")
        elif media < 6:
          print("A aluna está reprovada por nota. ")
        elif participacao < 6:
            print("A aluna está reprovada por nota de participação. ")
        else:
           print("A aluna está aprovada. ")
            
        print(f"A aluna {nome} {sobrenome} está  com média final de {media}")
        
  except KeyError:
        print("Não foi possível consultar o status de aprovação, a aula não conta no sistema. ")
  
main()