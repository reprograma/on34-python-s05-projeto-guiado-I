from dataset_alunas import dataset

def imprimir_dados():
    for aluna, info in dataset.items():
        print(f"Nome: {info['nome']}, Sobrenome: {info['Sobrenome']}")

if __name__ == "__main__":
    imprimir_dados()