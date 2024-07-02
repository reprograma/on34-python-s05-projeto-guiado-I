# Passo 1: Obter a entrada do usuário como uma string
entrada = input("Digite uma sequência de True e False separados por espaço: ")

# Passo 2: Dividir a string em uma lista de substrings
entradas_list = entrada.split()

# Passo 3: Converter cada substring para um valor booleano
booleanos = [entrada == "True" for entrada in entradas_list]

# Passo 4: Contar os valores booleanos na lista resultante
num_true = booleanos.count(True)
num_false = booleanos.count(False)

print(f"Número de True: {num_true}")
print(f"Número de False: {num_false}")