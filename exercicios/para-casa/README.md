# Exercício de Casa 🏠 

## Sistema da Escola Reprograma!

Nós somos da escola Reprograma, e queremos poder utilizar um sistema que nos auxilie no controle de algumas questões dentro do nosso dia-a-dia. Todas os nossos cálculos acabam sendo manuais, o que demanda muito tempo de nossos professores. Quero pedir uma ajuda a você para que nos auxilie nesta difícil missão. Como usuária, quero que este sistema tenha 5 funcionalidades importantes:
- Inclusão de uma nova aluna na minha base de dados
  - O sistema deve permitir a inclusão de uma nova aluna com os seguintes dados: nome, sobrenome, turma, notas (uma lista de números), presença (uma lista de booleanos indicando a presença em cada aula) e participação (um número representando o nota de participação da aluna).
  - Após a inclusão, o sistema deve exibir uma confirmação de que a aluna foi adicionada com sucesso.
  - Caso algum dado não seja válido (por exemplo, notas fora do intervalo permitido), o sistema deve informar o usuário sobre o erro e não adicionar a aluna. (opcional)

- Consultar a lista de alunas que estão cadastradas
  - O sistema deve exibir a lista de todas as alunas cadastradas, mostrando apenas os nomes.
  - A lista deve estar formatada de forma legível para o usuário.
  - Caso não haja alunas cadastradas, o sistema deve informar que não há registros. (opcional)

- Consultar a quantidade de faltas de uma aluna
  - O sistema deve permitir ao usuário buscar as faltas de uma aluna específica.
  - O usuário deve informar o nome completo da aluna para realizar a consulta.
  - Após a consulta, o sistema deve exibir a quantidade de faltas da aluna

- Consultar notas de uma aluna
  - O sistema deve permitir ao usuário consultar as notas de uma aluna específica.
  - O usuário deve informar o nome completo da aluna para realizar a consulta.
  - Após a consulta, o sistema deve exibir as notas obtidas pela aluna em cada avaliação.

- Consultar status de aprovação de uma aluna
  - O sistema deve calcular o status de aprovação de uma aluna com base nas suas notas.
  - O usuário deve informar o nome completo da aluna para realizar a consulta.
  - O sistema deve calcular a média simples das notas da aluna
  - Para o cálculo da aprovação, será considerado: nota de corte, a aluna deve ter pelo menos 80% de presença e nota de participação acima de 6
  - Após o cálculo, o sistema deve exibir o status de aprovação da aluna (aprovada ou reprovada) e sua média final
  - A nota de corte na escola é 6.

Nós contratamos uma pessoa que começou o sistema previamente, sua tarefa é implementar as funções que farão com que o sistema funcione. Aqui na escola, para cada funcionalidade implementada, recomendamos um commit, pois se caso algum dê errado, nós temos como reverter.

Obrigada pela ajuda! :)

--

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
- [ ] Criei um Pull Request seguindo as orientaçoes que estao nesse [documento](https://github.com/mflilian/repo-example/blob/main/exercicios/para-casa/instrucoes-pull-request.md).
