

### "Sistema da Escola Reprograma"

Esta é uma aplicação desenvolvida para auxiliar a escola no gerenciamento eficiente de informações sobre suas alunas. Atualmente, a escola enfrenta desafios com cálculos manuais que consomem muito tempo dos professores, portanto, o sistema foi projetado para automatizar diversas tarefas do dia-a-dia.

*A média simples das notas é calculada e comparada com a nota de corte da escola (6).*
*Além das notas, a aluna deve ter pelo menos 80% de presença e uma nota de participação acima de 6 para ser considerada aprovada.*

## Funcionalidades Implementadas:

* Inclusão de uma nova aluna na base de dados:

- Permite a adição de uma nova aluna com dados como nome, sobrenome, turma, notas em avaliações, presença em aulas e nota de participação. (Usa operadores booleanos).
- Após a inclusão bem-sucedida, o sistema confirma a adição.
- Validações são aplicadas para garantir que os dados inseridos sejam válidos. (Usando Try e Except).

* Consulta da lista de alunas cadastradas:

- Exibe a lista de todas as alunas cadastradas, mostrando apenas os nomes.
- Consulta da quantidade de faltas de alunas.
- Permite buscar o número de faltas de uma aluna específica.
- Permite a consulta das notas de uma aluna específica.
- Permite a consulta do status de aprovação de uma aluna específica.
- Após o cálculo, o sistema exibe o status de aprovação da aluna (aprovada ou reprovada) e sua média final.


## Metodologia:

O sistema foi desenvolvido seguindo uma abordagem modular, onde cada funcionalidade foi implementada separadamente, usando commits individuais para cada etapa, facilitando o controle de versões e a possibilidade de reverter mudanças se necessário. Há também comentários ao longo do código para facilitar o entendimento do sistema.

# Técnicas usadas

- Para evitar erros: Try e except
- Para conversões - listas: split, append
- Para conversões - tuplas: split
- Operadores Booleanos: True e False
- Para condições: If, elif e else.
- Para percorrer listas: For.


