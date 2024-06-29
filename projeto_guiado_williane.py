def media_notas ():
    while True:
        try:
            print("**Calculadora para média de notas** \nPara realizar o cálculo, digite o nome da aluna e as três notas que deseja calcular a média. \n Não são permitidos: \n⇨ Valores que não sejam números para as notas\n⇨ Inserir número negativo")
            nome = input("Nome da aluna: ")
            nota1 = float(input("Insira a primeira nota: "))
            nota2 = float(input("Insira a segunda nota: "))
            nota3 = float(input("Insira a terceira nota: "))

            media = (nota1 + nota2 + nota3)/3

            if media < 6:
                print("A aluna", nome, "foi reprovada com média igual a:", round(media, 2))
            
            else:
                print("A aluna", nome, "foi aprovada com média igual a:", round(media, 2))

            continuar_programa = input("Digite 1 se deseja calcular uma nova média ou 2 caso deseje parar: ")

            if continuar_programa == '1':
                continue
            else:
                break
                
        except:
            print("Entrada inválida.")

media_notas()