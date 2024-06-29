# Exercício de sala 
#O sistema deve permitir ao usuário inserir o nome da aluna, turma e as notas obtidas.
# Cálculo de Média:

#- O sistema deve calcular a média das notas inseridas.
#- Se a média for igual ou superior a 6, o sistema deve apresentar o status "Aprovada".
#- Se a média for inferior a 6, o sistema deve apresentar o status "Reprovada".

#Saída de Resultado:

#- Após calcular o status da aluna, o sistema deve apresentar a mensagem correspondente de forma clara e compreensível para o usuário.

nome_da_aluna = input("Por favor, insira seu nome: ")
turma_da_aluna = input("Agora informe sua turma: ")
notas_da_aluna = float[input("Informe suas notas: ")]
soma_das_notas = 0
for nota in notas_da_aluna:
    soma_das_notas += nota
    qtd_de_notas = (len(notas_da_aluna))
    media_das_notas = soma_das_notas / qtd_de_notas 

    if media_das_notas < 6:
       print("Olá", nome_da_aluna, "da", turma_da_aluna,".", "Sua nota final foi", media_das_notas, "logo você foi reprovada. \nNão desanime! Você pode tentar novamente.")

else:
    print("Olá", nome_da_aluna, "da", turma_da_aluna,".", "Sua nota final foi", media_das_notas, "Parabén! Você foi aprovada!")


