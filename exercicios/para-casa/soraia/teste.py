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
  
lista_de_presenca()

def consultar_notas_aluna():
  try:
    nome = input("Nome da aluna: ")
    sobrenome = input("Sobrenome da aluna: ")
    lista_de_notas = dataset[(nome,sobrenome)]["Notas"]
    print(f"A aluna {nome} {sobrenome} está com {lista_de_notas}")
    
  except:
    print("Aluna não encontrada. ")
    
    qtd_faltas = dataset[(nome)]["Presença"].count(False)
    qtd_aulas = len(dataset[(nome)]["Presença"])
    percentual_de_faltas = (qtd_faltas / qtd_aulas) * 80
    
    #nome = dataset[(nome)]
  #sobrenome = dataset[(sobrenome)]
  lista_de_notas = dataset[(nome)]["Notas"]
  media = float(sum(notas)/len(notas))
  nota_participacao = dataset[(nome, sobrenome)]["Participação"]
  presenca = dataset[(nome, sobrenome)]["Presença"]
  faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
  
  if media <  6:
    print ("Aluna está reporvada. ")
  elif nota_participacao < 6:
    print ("Aluna está reporvada. ")
  elif faltas > 2:
    print("Aluna está reporvada. ")
  else: 
    print("Aluna aprovada. ")