# Dicionário que guarda as infos das estudantes
estudantes = {}

def main():
    print("Bem-vindos à Escola do Reprograma!")
    print("Aqui você pode ver se uma estudante ou aluno foi aprovada/o ou reprovada/o.\n")
    
    while True:
        nome = pegar_nome_e_dados()  # Coleta o nome e outros dados 
        media = calcular_media(nome)  # Calcula a média das notas da estudante
        situacao = verificar_status(media)
        
        print(f"A estudante {nome} da turma {estudantes[nome]['turma']} foi {situacao}. A média dela é: {media:.2f}.\n")
        
def pegar_nome_e_dados():
    print("Preencha os dados da estudante: ")
    nome = input("Nome da estudante: ")  # Pede o nome da estudante
    turma = input("Qual é a turma? ")  # Pede a turma da estudante
    
    notas = pedir_notas()  # Pede as notas da estudante
    
    guardar_dados(nome, turma, notas)
    
    return nome
    
def pedir_notas():
    quantidade = int(input("Quantas notas você vai colocar? "))  # Pergunta quantas notas serão inseridas
    lista_notas = []  # Cria uma lista para armazenar as notas
    
    for i in range(quantidade): 
        while True:  # Continua pedindo a nota até receber uma válida
            entrada = input(f"Digite a nota #{i + 1}: ")  # Pede a nota específica
            try:  # Tenta transformar a entrada em um número
                nota = float(entrada)  # Converte a entrada para número decimal
                lista_notas.append(nota)  # Adiciona a nota na lista
                break  # Sai do loop se a nota for válida
            except ValueError:  # Se a entrada não for um número
                print("Entrada inválida. Por favor, coloque um número.")
    
    return lista_notas

def guardar_dados(nome, turma, notas):
    estudantes[nome] = {  # Adiciona os dados da estudante no dicionário
        "turma": turma,
        "notas": notas,
    }
    
def calcular_media(nome):
    notas = estudantes[nome]["notas"]  # Pega as notas da estudante
    media = sum(notas) / len(notas)  # Calcula a média das notas
    return media

def verificar_status(media):
    if media >= 6:
        return "aprovada"
    else:
        return "reprovada"

main()
