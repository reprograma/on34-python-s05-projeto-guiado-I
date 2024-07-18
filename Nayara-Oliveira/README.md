# S05 - Projeto guiado {Reprograma} 
# Tabela de conteúdos
* [O que aprendi](#o-que-aprendi)
* [Descrição - Projeto de casa - Sistema da Escola Reprograma](#projeto-de-casa---sistema-da-escola-reprograma)
* [Descrição - Projeto de sala - Automação de notas](#projeto-de-sala---automação-de-notas)
* [Como acessar os projetos](#como-acessar-os-projetos)
# O que aprendi:
Nesses projetos, apliquei conceitos relacionados a funções, condicionais, tratamento de exceções usando try e except, laços de repetições e estruturas de dados, explorando principalmente a manipulação de dicionários e listas.
# Projeto de casa - Sistema da Escola Reprograma
## Objetivo do projeto:
Criação de um sistema para uma escola. O sistema possui 5 funcionalidades:
- Inclusão de uma nova aluna na base de dados
    - O sistema permite a inclusão de uma nova aluna com os seguintes dados: nome, sobrenome, turma, notas (uma lista de números), presença (uma lista de booleanos indicando a presença em cada aula) e participação (um número representando o nota de participação da aluna).
    - Caso algum dado não seja válido (por exemplo, notas fora do intervalo, ou usuário dar letras como entrada para nota), o sistema não adiciona aluna
- Consultar a lista de alunas que estão cadastradas
    - Exibe a lista de todas as alunas cadastradas, mostrando apenas nomes.
    - Caso não haja alunas cadastradas, o sistema informa que não há registros.
- Consultar a quantidade de faltas de uma aluna
    - Sistema permite ao usuário buscar as faltas de uma aluna específica.
    - O usuário deve informar o nome completo da aluna para realizar a consulta.
    - Após a consulta, o sistema exibe a quantidade de faltas da aluna.
    - Caso o nome informado não corresponda a uma aluna cadastrada, o sistema informa que não há registro com esse nome.
- Consultar notas de uma aluna
    - O sistema permite ao usuário consultar as notas de uma aluna específica.
    - O usuário deve informar o nome completo da aluna para realizar a consulta.
    - Após a consulta, o sistema exibe as notas obtidas pela aluna em cada avaliação.
    - Caso o nome informado não corresponda a uma aluna cadastrada, o sistema informa que não há registro com esse nome.
- Consultar status de aprovação de uma aluna
    - O sistema calcula o status de aprovação de uma aluna com base nas suas notas e presença. 
    - O usuário deve informar o nome completo da aluna para realizar a consulta.
    - O sistema calcula a média simples das notas da aluna
    - Para o cálculo da aprovação, será considerado: nota de corte igual a 6, pelo menos 80% de presença e nota de participação acima de 6.
    - Após o cálculo, o sistema exibe o status de aprovação da aluna (aprovada ou reprovada) e sua média final.
    - Caso o nome informado não corresponda a uma aluna cadastrada, o sistema informa que não há registro com esse nome.
# Projeto de sala - Automação de notas
## Objetivo do projeto
Criação de um sistema para uma escola com as seguintes funcionalidades:
- Sistema permite ao usuário inserir o nome da aluna, turma, notas das avaliações, presença e nota de participação em sala.
- Sistema armazena os dados informados pelo usuário em um dicionário, cujos valores são acessados através do nome da aluna.
- Sistema calcula a média ponderada, considerando que: nota de participação tem um peso definido de 20% da média final, enquanto notas de avaliações têm um peso de 80% da média final.
- Sistema exibe o status de aprovação, com base nos seguintes critérios:
    - Se o percentual de faltas for maior que 20%, o sistema apresenta o status "Reprovada por falta", independentemente da média final
    - Se a média final for igual ou superior a 6, o sistema apresenta o status "Aprovada"
    - Se a média final estiver entre 4 e 6, o sistema apresenta o status "Em recuperação"
    - Se a média final for inferior a 4, o sistema apresenta o status "Reprovada"
- Caso a aluna estiver em recuperação:
    - Sistema pergunta ao usuário se a aluna fez a prova. 
    - Se a resposta for positiva, sistema solicita e inclui a nota da recuperação. 
    - Se a nota de recuperação for maior que a menor nota de avaliação, o sistema a substitui pela nota obtida na recuperação, e é calculada uma nova média final
# Como acessar os projetos
Caso deseje testar a atividade, siga esses passos:
1. Clone o repositório em sua máquina
2. Abra o terminal git bash no Visual Studio Code.
3. Navegue até o diretório de nome "Nayara-Oliveira"
    - Navegue até diretório de nome "exercicio-sala" para acessar o projeto de sala
    - Navegue até diretório de nome "exercicio-casa" para acessar o projeto de casa
4. Execute o arquivo no terminal 
    - utilize o comando `python Automacao_de_notas.py` para executar o projeto de sala 
    - Utilize o comando `python sistema_de_alunas.py` para executar o projeto de casa