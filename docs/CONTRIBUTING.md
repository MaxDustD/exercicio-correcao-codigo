# Contribuição e padronização do projeto

## Boas-vindas

Seja bem-vindo ao projeto. Este repositório é um exercício de correção e melhoria de código, então o foco principal é manter o código organizado, legível e consistente.

Aqui, qualquer contribuição deve respeitar as convenções do projeto e ajudar a deixar a solução mais clara, sem complicar a lógica por regras excessivas. O objetivo não é “deixar tudo perfeito” do ponto de vista do Pylint, mas manter um padrão útil para o exercício.

## Padrões do projeto

- Python mínimo: 3.14
- Módulos: snake_case
- Classes: PascalCase
- Funções: snake_case
- Variáveis: snake_case
- Constantes: UPPER_CASE
- Métodos: snake_case
- Máximo de argumentos por função: 5

## Organização de Commits
Foi adotado o padrão de commits convencional para o histórico do Git. Os prefixos mais comuns utilizados neste projeto são:
* `chore`: Mudanças no processo de desenvolvimento, ferramentas de build ou configurações que não modificam o código de produção.
* `refactor`: Alterações no código que não corrigem bugs nem adicionam funcionalidades, mas melhoram sua estrutura/legibilidade.
* `feat`: Introdução de uma nova funcionalidade.
* `fix`: Correção de um bug.

## Pylint

O comando abaixo pode ser usado para verificar o código localmente, mas não é necessário por haver configuração de pre-commit e validação automática:

```bash
pylint cadastro.py
```

## Antes de concluir

- Use nomes claros
- Mantenha o código organizado
- Teste a alteração
- Rode o Pylint localmente se quiser revisar antes do commit
- Verifique se a mudança não deixou o código mais confuso
