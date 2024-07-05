dataset = {
    ("Ana", "Silva"): {
        "Turma": "Turma A",
        "Notas": [7.5, 8.0, 9.0],
        "Presença": [True, True, False, True, True],
        "Participação": 8.5
    },
    ("Mariana", "Santos"): {
        "Turma": "Turma B",
        "Notas": [6.0, 7.5, 8.5],
        "Presença": [True, True, True, False, True],
        "Participação": 7.2
    },
    ("Carla", "Oliveira"): {
        "Turma": "Turma A",
        "Notas": [8.0, 7.5, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.2
    },
    ("Juliana", "Ferreira"): {
        "Turma": "Turma C",
        "Notas": [9.0, 8.5, 7.0],
        "Presença": [True, True, True, True, True],
        "Participação": 8.7
    },
    ("Patrícia", "Souza"): {
        "Turma": "Turma B",
        "Notas": [7.0, 7.0, 7.5],
        "Presença": [True, False, True, True, True],
        "Participação": 7.2
    },
    ("Aline", "Martins"): {
        "Turma": "Turma A",
        "Notas": [8.5, 8.0, 9.0],
        "Presença": [True, True, True, True, True],
        "Participação": 8.5
    },
    ("Fernanda", "Costa"): {
        "Turma": "Turma C",
        "Notas": [6.5, 7.0, 8.0],
        "Presença": [True, True, True, False, True],
        "Participação": 7.2
    },
    ("Camila", "Pereira"): {
        "Turma": "Turma B",
        "Notas": [7.5, 8.0, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.0
    },
    ("Luana", "Rodrigues"): {
        "Turma": "Turma A",
        "Notas": [9.0, 9.0, 8.5],
        "Presença": [True, True, True, True, True],
        "Participação": 8.8
    },
    ("Beatriz", "Lima"): {
        "Turma": "Turma C",
        "Notas": [8.0, 7.5, 7.0],
        "Presença": [True, True, True, False, True],
        "Participação": 7.5
    }
}



def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    
    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1: incluir_nova_aluna()
        elif cod_opcao == 2: consultar_lista_alunas()
        elif cod_opcao == 3: consultar_faltas_aluna()
        elif cod_opcao == 4: consultar_notas_aluna()
        #elif cod_opcao == 5: consultar_status_aprovacao()
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
    
    return nome
  
  
def consultar_lista_alunas():
    print(dataset.keys())
    
    
def consultar_faltas_aluna():
  try:
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    lista_de_presenca = dataset[(nome,sobrenome)]["Presença"]
    print(f"A aluna {nome} {sobrenome} está com {lista_de_presenca}")
    
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
 

  
main()