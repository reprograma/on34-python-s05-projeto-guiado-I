# Exercício de Sala 🏫  

## Automação de notas!

Nós somos da escola Reprograma, e estamos muito felizes em poder contar com você. Com o crescente número de alunas, nós queremos automatizar o processo de cálculo de notas. Para isso, queremos definir entregáveis para que possamos 

### MVP 1: Coleta de Dados Básicos

Critérios de Aceite:

Entrada de Dados:

- O sistema deve permitir ao usuário inserir o nome da aluna, turma e as notas obtidas.

Cálculo de Média:

- O sistema deve calcular a média das notas inseridas.
- Se a média for igual ou superior a 6, o sistema deve apresentar o status "Aprovada".
- Se a média for inferior a 6, o sistema deve apresentar o status "Reprovada".

Saída de Resultado:

- Após calcular o status da aluna, o sistema deve apresentar a mensagem correspondente de forma clara e compreensível para o usuário.

### MVP 2: Coleta de Dados com Presença e Participação

Critérios de Aceite:

Novos Dados:

- Além dos dados do MVP 1, o sistema deve permitir ao usuário inserir dados de presença como uma lista booleana (por exemplo, [True, True, False]) e a nota de participação da aluna.

Cálculo com Participação:

- O sistema deve incorporar a nota de participação no cálculo da média final da aluna.
- Após calcular a média ponderada, o sistema deve verificar se a aluna está em situação de recuperação.
- A participação deve ter um peso definido de 20% da média final.

Validação de Dados:

- Todos os dados inseridos pelo usuário devem ser validados para garantir que estejam corretos antes de calcular o resultado final.

### MVP 3: Adição do Status "Em Recuperação"

Critérios de Aceite:

Inclusão da Recuperação:

- Após calcular o status de aprovação/reprovação, o sistema deve permitir ao usuário informar se a aluna fez prova de recuperação.
- Se a aluna fez prova de recuperação, o sistema deve solicitar e incluir a nota da recuperação.

Verificação de Recuperação:

- Após calcular a média ponderada, o sistema deve verificar se a aluna está em situação de recuperação.
- Uma aluna estará em recuperação se sua média ponderada for inferior a um valor de corte definido (por exemplo, 6).

### MVP 4: Implementação de Recuperação com Substituição Automática

Critérios de Aceite:

Substituição de Nota:

- O sistema deve permitir substituir a menor nota pela nota de recuperação, se essa ainda não tiver sido inserida.
- A substituição deve ocorrer automaticamente após a inserção da nota de recuperação, sem a necessidade de intervenção adicional do usuário.

Restrição de Substituição:

- A substituição automática só pode ocorrer se a aluna tiver feito a prova de recuperação e essa nota for superior à menor nota originalmente inserida.

### MVP 5: Adição do Status "Reprovada por Falta"

Critérios de Aceite:

Cálculo de Faltas:

- O sistema deve calcular a porcentagem de faltas com base nos dados de presença fornecidos pelo usuário.
- Uma aluna será considerada "Reprovada por falta" se a porcentagem de faltas for superior a um limite predefinido de 20%.

Novo Status de Resultado:

- Além dos status anteriores ("Aprovada", "Reprovada" e "Em recuperação"), o sistema deve apresentar o status "Reprovada por falta" quando aplicável.


Considerações Finais

Feedback ao Usuário:

- Após cada cálculo, o sistema deve apresentar claramente o status da aluna, garantindo que o usuário compreenda completamente os resultados.

Terminou o exercício? Dá uma olhada nessa checklist e confere se tá tudo certinho, combinado?!

- [ ] Fiz o fork do repositório.
- [ ] Clonei o fork na minha máquina (`git clone url-do-meu-fork`).
- [ ] Resolvi o exercício.
- [ ] Adicionei as mudanças. (`git add .` para adicionar todos os arquivos, ou `git add nome_do_arquivo` para adicionar um arquivo específico)
- [ ] Commitei a cada mudança significativa ou na finalização do exercício (`git commit -m "Mensagem do commit"`)
- [ ] Pushei os commits na minha branch (`git push origin nome-da-branch`)
