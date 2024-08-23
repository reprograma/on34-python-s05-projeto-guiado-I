class Aluno:
    def __init__(self, nome, sobrenome, turma, notas, presencas, participacao):
        self.nome = nome
        self.sobrenome = sobrenome
        self.turma = turma
        self.notas = notas
        self.presencas = presencas
        self.participacao = participacao
    
    def calcular_faltas(self):
        
        return len([presenca for presenca in self.presencas if not presenca])
    
    def calcular_media(self):
        
        return sum(self.notas) / len(self.notas) if self.notas else 0

    def verificar_aprovacao(self):
        
        media = self.calcular_media()
        porcentagem_presencas = sum(self.presencas) / len(self.presencas) if self.presencas else 0
        if media >= 6 and porcentagem_presencas >= 0.8 and self.participacao > 6:
            return True, media
        return False, media

class Escola:
    def __init__(self):
        
        self.alunas = []

    def carregar_dataset_inicial(self, dataset):
        
        for (nome, sobrenome), dados in dataset.items():
            self.adicionar_aluna(nome, sobrenome, dados['Turma'], dados['Notas'], dados['Presença'], dados['Participação'])

    def adicionar_aluna(self, nome, sobrenome, turma, notas, presencas, participacao):
        
        nova_aluna = Aluno(nome, sobrenome, turma, notas, presencas, participacao)
        self.alunas.append(nova_aluna)
        print(f'Aluna {nome} {sobrenome} adicionada com sucesso!')

    def listar_alunas(self):
        
        if not self.alunas:
            print('Nenhuma aluna cadastrada.')
            return
        for aluna in self.alunas:
            print(f'{aluna.nome} {aluna.sobrenome}')
    
    def consultar_faltas(self, nome_completo):
       
        for aluna in self.alunas:
            if f'{aluna.nome} {aluna.sobrenome}' == nome_completo:
                faltas = aluna.calcular_faltas()
                print(f'Aluna {nome_completo} tem {faltas} faltas.')
                return
        print(f'Aluna {nome_completo} não encontrada.')

    def consultar_notas(self, nome_completo):
        
        for aluna in self.alunas:
            if f'{aluna.nome} {aluna.sobrenome}' == nome_completo:
                print(f'Notas da aluna {nome_completo}: {aluna.notas}')
                return
        print(f'Aluna {nome_completo} não encontrada.')

    def consultar_aprovacao(self, nome_completo):
        
        for aluna in self.alunas:
            if f'{aluna.nome} {aluna.sobrenome}' == nome_completo:
                aprovada, media = aluna.verificar_aprovacao()
                status = 'aprovada' if aprovada else 'reprovada'
                print(f'Aluna {nome_completo} está {status} com média {media:.2f}.')
                return
        print(f'Aluna {nome_completo} não encontrada.')

# Exemplo de uso do sistema
escola = Escola()

#
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
escola.carregar_dataset_inicial(dataset)

escola.listar_alunas()

escola.consultar_faltas('Ana Silva')

escola.consultar_notas('Maria Silva')

escola.consultar_aprovacao('Juliana Ferreira')
