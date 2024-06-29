resposta = {}
nome = ""

def menu():
    print("₊ ⊹🫐 ✧˚. ᵎᵎ 🪻  Bem-vinda a Escola Reprograma ₊ ⊹🪻✧˚. ᵎᵎ 🫐 \n👩‍💼 Espero que esteja gostando da experiência de EducaTec")
    print("📓 Aqui você pode calcular a aprovação de uma estudante.")
    
    while True:
        nome = obter_infos()
        desliga = input("\n🌠🪀 Deseja encerrar o programa? (s/n): ")
        if desliga.lower() == "s":
            break
    
def obter_infos():
    print("\n Solicitamos os seguintes dados ๋࣭ ⭑𐙚")

    notas = obter_notas()
    return notas

def obter_notas():
    nome = input("ᯓ★ Nome da estudante: ")
    turma = input("ᯓ★ Turma atual da estudante: ")

    quantidade_notas = int(input("꩜.ᐟ Quantidade de notas: "))
    notas = []
    for i in range(quantidade_notas): #range cria uma lista ordenada até o número passado como parâmetro
        while True: #não sabemos a quantidade de repetições
            entrada = input(f'⋆.˚ Insira a nota #{i+1}: ')
            try:
                nota = (round(float(entrada), 2))
                notas.append(nota)
                break #sai do while e segue com for
            except ValueError:
                print("❌🤖 Entrada inválida. Insira um número válido.")

    print(f'🧸ྀི  Confirmando as notas recebidas: {notas} 📂')
      
    media = sum(notas)/len(notas)
    if media >= 6:
        resultado = "aprovada ✅"
    else:
        resultado = "reprovada ❌"

    print(f'˚˖𓍢ִ໋`🌿:✧˚ A média da estudante {nome} da turma {turma} é de {media}, com isso, ela está {resultado}.')

    return notas

menu()

