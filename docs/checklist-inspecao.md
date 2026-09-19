# CHECKLIST DE INSPECAO

**A. Clareza e legibilidade**
( X ) A1 – Os nomes das variáveis deixam claro o seu significado?
( X ) A2 – É possível compreender o que cada trecho faz sem executar o programa?
( X ) A3 – Textos e valores literais aparecem repetidos ao longo do código?

**B. Duplicação**
( X ) B1 – Existe código repetido em pontos diferentes do programa?
( X ) B2 – A mesma regra está implementada em mais de um lugar?
( X ) B3 – A busca de uma pessoa aparece repetida?
( X ) B4 – A impressão dos dados de uma pessoa aparece repetida?

**C. Estrutura e complexidade**
( X ) C1 – Há blocos muito extensos ou difíceis de acompanhar?
( X ) C2 – É possível identificar rapidamente onde começa e termina cada responsabilidade?
( X ) C3 – Menu, leitura de dados, regras e exibição estão misturados no mesmo trecho?

**D. Entrada e validação de dados**
( X ) D1 – Entradas inválidas podem causar comportamento inesperado?
( X ) D2 – Existe verificação de faixa ou de plausibilidade para a idade?
( X ) D3 – Campos obrigatórios podem ser gravados vazios?

**E. Consistência dos dados**
( X ) E1 – Os dados de uma mesma pessoa estão espalhados em variáveis que podem se desencontrar?
( X ) E2 – Existe regra clara para identificar unicamente uma pessoa?
( X ) E3 – Há política definida para nomes duplicados?

**F. Manutenibilidade e evolução**
( X ) F1 – Acrescentar um novo atributo à pessoa exigiria alterar muitos pontos do código?
( X ) F2 – Uma nova operação faria o bloco principal crescer significativamente?
( X ) F3 – Alterar a interface com o usuário exigiria alterar a lógica do sistema?

**G. Comportamento e possíveis defeitos**
( X ) G1 – O comportamento para uma pessoa inexistente é adequado e informativo?
( X ) G2 – Operações equivalentes tratam os mesmos dados de maneira coerente entre si?


---------------------------------------------------------------------------------------------------

### ID 01

| Campo | Descrição |
|---|---|
| **ID** | 01 |
| **Local** | Linhas 14, 15 e outras |
| **Categoria** | A1 |
| **Achado** | Variáveis que não apresentam significado claro no programa, prejudicando o entendimento de todos que forem analisá-lo. |
| **Evidência** | Variáveis como `qtd` e `op`. |
| **Consequência/risco** | Dificuldade de entendimento do programador, desperdiçando tempo para leitura do código. |
| **Sugestão** | Adotar convenções de nomes adequados e explícitos. |

### ID 02

| Campo | Descrição |
|---|---|
| **ID** | 02 |
| **Local** | Linha 17 |
| **Categoria** | C1 |
| **Achado** | Um bloco extenso que poderia ser reduzido. |
| **Evidência** | O uso do `while` com muitas funções dentro que poderiam ser apenas chamadas de métodos e procedimentos. |
| **Consequência/risco** | Dificuldade de manutenção caso o software cresça, com possibilidade de erros ficarem escondidos. |
| **Sugestão** | Criar métodos e procedimentos separados para cada opção. |

### ID 03

| Campo | Descrição |
|---|---|
| **ID** | **03** |
| **Local** | Linhas 4 a 12 |
| **Categoria** | F1 |
| **Achado** | Uso muito simplório de declaração de variáveis para cada pessoa. |
| **Evidência** | Declaração de nome, idade e e-mail seguida de um número para cada pessoa cadastrada. |
| **Consequência/risco** | O programa precisa de várias alterações para se adequar à quantidade atual de pessoas, além de declarar variáveis para cada pessoa nova. |
| **Sugestão** | Adotar vetores de structs ou listas. |
 
### ID 04

| Campo | Descrição |
|---|---|
| **ID** | **04** |
| **Local** | Linhas 29, 58, 68, 73... |
| **Categoria** | A3 |
| **Achado** | Valores estáticos que fazem parte de condições lógicas, atrelados às opções. |
| **Evidência** | `qtd == 3`, `qtd >= 1`, `qtd >= 2`, `qtd >= 3`. |
| **Consequência/risco** | Escalonamento empírico, forçado e limitado do programa. |
| **Sugestão** | Usar valores adequados à condição, como `n` para representar o tamanho do vetor. |