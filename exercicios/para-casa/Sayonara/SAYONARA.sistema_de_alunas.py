from dataset_alunas import dataset

def main():
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        cod_opcao = obter_opcao()
        
        if cod_opcao == 1: incluir_nova_aluna()
        elif cod_opcao == 2: consultar_lista_alunas(dataset)
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
    
def incluir_nova_aluna():
    print("Informe os dados ")
    nome= input("Informe o nome e o sobrenome :")
    turma = input("informe a turma :" )
    notas = pedir_notas()
    nota_participaçao=float(input("participação da aluna: "))
    presença= chamada() 
    dataset[(nome.split()[0] , nome.split()[1])] = {
        "Turma": turma,
         "Notas": notas,
         "Presença": presença,
         "Paticipaçao": nota_participaçao
    }
    print("Aluna cadastrada com sucesso ")
    pass
    #TODO - Implentar a função
def pedir_notas():
   #quantidade_notas=input("informa a quantidade das notas:")
   notas=[]
   for i in range(3):
         nota=float(input(f"Digite a {i+1}° nota:" ))
         notas.append(nota)


   return notas 
 
def chamada(): 
    aulas=[] 
    for  i in range (5): 
     aula=int(input(f" Digite 1 se presente ou 0 se ausente, na aula :{i+1}°: presença:"))  
    aulas.append(aula)
    return aulas 

    
def consultar_lista_alunas(dataset):
     print("Lista alunas ")
     for aluna_tuple in dataset:
        nome_c = aluna_tuple[ 0 ]  + " " + aluna_tuple[1]
        nome =nome_c.strip('(').strip()
        print (nome)

     pass
    #TODO - Implentar a função
    
def consultar_faltas_aluna():
     print("informe o nome da aluna")
     nome_completo=input("Nome completo")
     nome_aluna,sobrenome_aluna=nome_completo.split()
     chave_aluna=(nome_aluna,sobrenome_aluna)

     if chave_aluna in dataset:
      presencas=dataset[chave_aluna]["Presença"]
      numero_faltas=presencas.count(False)
      print(f" Número de faltas de {nome_aluna}  {sobrenome_aluna} :{numero_faltas}")
     

            
        
     return

     pass
    #TODO - Implentar a função
    
def consultar_notas_aluna():
    print("Informe o nome da aluna")
    nome_completo=input("Nome completo: ")
    nome_aluna,sobrenome_aluna=nome_completo.split()
    chave_aluna=(nome_aluna,sobrenome_aluna)
    if chave_aluna in dataset:
      nota=dataset[chave_aluna]["Notas"]





      print(f" Notas de {nome_completo}:{nota}" )

 




   
    return
    pass
    #TODO - Implentar a função
    
def consultar_status_aprovacao():
     
     print("Informe o nome da aluna")
     nome_completo=input("Nome Completo")
     nome_aluna,sobrenome_aluna=nome_completo.split()
     chave_aluna=(nome_aluna,sobrenome_aluna)
     if chave_aluna in dataset:
      notas=dataset[chave_aluna]["Notas"]
      nota_participaçao=dataset[chave_aluna]["Participação"]
      faltas=dataset[chave_aluna]["Presença"]
      faltas_contagem=faltas.count(False)
      media=sum(notas)/len(notas)
      if media>=6 and nota_participaçao>=6 and faltas_contagem<=2:
        print(f"Aluna aprovada com a média : {media:.2f}  ")
      else:
        print(f"Aluna reprovada com média :{media:.2f}")  







     pass
    #TODO - Implentar a função
    

main()