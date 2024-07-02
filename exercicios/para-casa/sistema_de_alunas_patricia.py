#from dataset_alunas import dataset
dataset = []

def main():
    # Exibe a mensagem de boas-vindas a loop principal
    print("\n---  Seja bem vinda a Escola do Reprograma!  ---")
    print("Sistema de informações de alunas")
    
    while True:
        # Obtém a opção selecionada pelo usuario
        cod_opcao = obter_opcao()

        #EXECUTA A FUNÇÃO CORREPONDENTE Á OPÇÃO SELECIONADA
        
        if cod_opcao == 1: incluir_nova_aluna()
        elif cod_opcao == 2: consultar_lista_alunas()
        elif cod_opcao == 3: consultar_faltas_aluna()
        elif cod_opcao == 4: consultar_notas_aluna()
        elif cod_opcao == 5: consultar_status_aprovacao()
        elif cod_opcao == 6: print("Encerrando o programa..."); break

def obter_opcao():
    #função para obter a opção do usuario
    codigo_opcao = 0

    while codigo_opcao not in [1, 2, 3, 4, 5, 6]:
        try:

            #EXIBE O MENU DE OPÇÕES E SOLICITA UMA ESCOLHA DO USUARIO

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
    #FUNÇÃO PARA INCLUIR NOVA ALUNA NO DATASET

    nome = input ("Nome da nova aluna:")
    sobrenome = input ("Sobrenome nova aluna:")
    turma = input ("Turma:")
    notas = list(map(float,input("Notas (separadas por espaço):").split()))
    presencas = list(map(bool,map(int,input("Presenças (1 para presente,0 para ausente, separada por espaço):").split())))
    participaçao = float(input("Nota de participação:"))    
    
    #valida os dados da entrada
    if not all(0 <= nota <= 10 for nota in notas):
        print("Erro:Presenças devem ser 1 (prensente)ou 0(ausente).")
        return
    if not all(presenca in [True,False] for presenca in presencas):
        return
    if not 0 <= participaçao <= 10:
        print("Erro: Nota de participação deve estar no intervalo de 0 a 10. ")
        return
    
# CRIA UM DICIONÁRIO COM DADOS DA NOVA ALUNA
    nova_aluna ={
        "nome": nome,
        "sobrenome":sobrenome,
        "turma": turma,
        "notas": notas,
        "presencas": presencas,
        "participacao": participaçao

    }

    #adiciona a nova aluna ao dataset
    dataset.append(nova_aluna)
    print(f"Aluna{nome}{sobrenome}incluida com sucesso!")
    



def consultar_lista_alunas():
    #função para consultar a lista de alunas cadastradas
    if not dataset:
        print("Não há alunas cadastrada")
        return
    print("\nLista de Alunas:")
    #exibe o nome completo de cada aluna cadastrada
    for aluna in dataset:
         print(f"{aluna["nome"]} {aluna["sobrenome"]}")
         


    
def consultar_faltas_aluna():
     #função para consultar a quantidade de faltas de uma aluna especifica
     nome_completo = input ("Nome completo da aluna: ") 
     aluna = next((a for a in dataset if f"{a['nome']} {a["sobrenome"]}"  == nome_completo), None)   
     if aluna:
         faltas = aluna["presencas"].count(False)
         print(f"Faltas da aluna {nome_completo}:{faltas}")
     else:
         print(f"Aluna {nome_completo} não encontrado.")    
    


def consultar_notas_aluna():
    #função para consultar as notas de uma aluna especifica
    nome_completo = input ("Nome completo da aluna:")
    aluna = next((a for a in dataset if f"{a["nome"]}  {a["sobrenome"]}"== nome_completo), None)
    if aluna:
        print(f"Notas da aluna {nome_completo}: {aluna["notas"]}")
    else:
        print(f"Aluna {nome_completo} não encontrado")    

    
def consultar_status_aprovacao():
    #função para consultar o status de aprocação
    nome_completo = input ("Nome completo da aluna:")
    aluna = next ((a for a in dataset if f"{a ["nome"]}  {a["sobrenome"]}" == nome_completo), None)
    if aluna:
        media_notas = sum(aluna['notas']) / len(aluna["notas"])
        percentual_presenca = aluna["presencas"].count (True) / len(aluna["presencas"])
        status ="APROVADA" if media_notas >= 6  and percentual_presenca >=0.8 and aluna ["participacao"] > 6 else "REPROVADA"
        print(F"Status de aprovação da aluna {nome_completo}:{status}")
        print(f"Aluna {nome_completo} NÃO ENCONTRADO")
    
    
    

main()