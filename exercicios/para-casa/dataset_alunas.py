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



print ("-------------------------hello world!!---------------------------------")
print ("-------------------Esse é o sistema reprograma-------------------------")
print ("-----------------------seja bem vinde ;) ------------------------------")
print ("----------Para ter acesso a lista de alunas (digite 1)-----------------")
print ("----------------------Para inserir aluna nova (digite 2)--------------")
print ("-------------------Para consultar presença (digite 3)-----------------")
print ("----------------Para consultar notas  (digite 4)------------------------")
print ("----------------Para calcular média (digite 5)------------------------")
print ("-----------------Para sair do sistema (digite 6)----------------------")

 

 

     
    
def inclusao_novas_alunas ():
    while True:
     nome = str(input("Insira o nome: "))
     sobrenome = input("Insira o seu sobrenome: ")
     turma = input(" Insira a sua turma: ")
   
     notas = []
     for i in range (3):
       nota = int(input (f"Insira as suas {i+1} notas: "))
       notas.append(nota)
       
     presenca = []
     for i in range (5):
       aulas = bool(input(f"insira presença {i+1} com 'True' e falta com 'False' são 5 aulas: ")) # returnar, criar função bool
       presenca.append(presenca)
    
     participacao = int(input("Insira sua nota de participação de 0 á 10: "))
   
     salvamento_dos_dados_aluna = (nome,sobrenome,turma,notas,presenca,participacao)

     print (f"olá, {nome} seja bem vinde a rede reprograma! ")
     break



def salvamento_dos_dados_aluna (nome,sobrenome,turma,notas,presenca,participacao):
    chave = (nome)
    dataset = [chave] = { 
        "Turma": turma,
        "Notas": notas,
        "Presença": presenca,
        "Participação": participacao
    }

    print (f"a aluna {nome} foi adicionada com sucesso!!")
    return qual_numero

def consultar_dados_alunas ():
 nome_aluna_cadastrada = input("insira o nome da aluna que deseja ver os dados :")

 sobrenome_aluna_cadastrada = input("insira o sobrenome da aluna que deseja ver os dados :")


 if (nome_aluna_cadastrada, sobrenome_aluna_cadastrada) not in dataset:
    print ("esse nome não está no sistema!!")
 
 else:
    print (f"o seu nome  é {nome_aluna_cadastrada} e sobrenome {sobrenome_aluna_cadastrada}")
    
    return nome_aluna_cadastrada,sobrenome_aluna_cadastrada
    
 
 
 
     
def consulta_presenca():
   while True:
    nome, sobrenome = consultar_dados_alunas()
    qtd_faltas = dataset[(nome, sobrenome)]["Presença"].count(False)
    qtd_presente = dataset [((nome, sobrenome))]["Presença"].count (True)
    print (f"essa aluna tem {qtd_faltas} faltas e {qtd_presente} presentes. ")
    break

def consulta_notas():
   nome, sobrenome = consultar_dados_alunas()
   mostrar_notas = dataset[(nome, sobrenome)]["Notas"]
   print (f"essa aluna tem essas notas {mostrar_notas} ")
    


def calcular_aprovacao ():
   
    nome, sobrenome = consultar_dados_alunas()
    notas = dataset[(nome, sobrenome)]["Notas"]
    soma = (sum(notas))
    participacao = dataset[(nome, sobrenome)]["Participação"]
    qtd_presente = dataset [((nome, sobrenome))]["Presença"].count (True) 
    percentual_presenca = qtd_presente / len(dataset [((nome, sobrenome))]["Presença"])
    nota_media = float(soma/ len(notas))
    
    print(f"sua nota é {nota_media}")
    
    if nota_media >= 6 and percentual_presenca >= 80 and participacao >= 6 :
     print("aprovada")
     
    else:
      print("reprovada ou por nota ou por falta!")
    
    
    


while True:
    qual_numero = int(input("insira o número: "))
    if qual_numero == (1):
       print (dataset)
    elif qual_numero == (2):
        inclusao_novas_alunas()
    elif qual_numero == (3):
        consulta_presenca()
    elif qual_numero == (4):
        consulta_notas() 
    elif qual_numero == (5):
        calcular_aprovacao() 
    elif qual_numero == (6):
        print ("o sistema desligou")
