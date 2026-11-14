# Como contribuir

Este repositório é um exercício de correção e melhoria de código. Contribuições devem manter a solução organizada, legível e consistente, sem complexidade desnecessária.

O projeto usa Python 3.14 ou superior. Siga as convenções: módulos, funções, métodos e variáveis em `snake_case`; classes em `PascalCase`; constantes em `UPPER_CASE`; e prefira funções com no máximo cinco argumentos. Não inclua dados reais de pessoas no repositório.

## Verificar o estado do repositório

Antes de começar, atualize a branch principal e confirme que não há alterações locais que possam ser sobrescritas:

```bash
git status
git switch main
git pull --ff-only origin main
git status
```

Se houver alterações locais, salve-as ou faça o commit antes de trocar de branch.

## Branch, commits e hooks do pre-commit

Crie uma branch para a tarefa, com um nome curto que indique o objetivo:

```bash
git switch -c tipo/descricao-curta
```

Instale as dependências e o hook do Git:

```bash
python -m pip install -r requirements.txt
pre-commit install
```

O hook executa o Pylint nos arquivos Python preparados para commit e os testes do projeto. Corrija eventuais falhas antes de tentar o commit novamente.

Use commits pequenos, cada um representando uma alteração verificável, com mensagens objetivas no padrão convencional. Prefixos comuns neste projeto:

- `feat`: nova funcionalidade.
- `fix`: correção de bug.
- `refactor`: melhoria estrutural sem alterar o comportamento esperado.
- `docs`: documentação.
- `chore`: ferramentas e configurações de desenvolvimento.

Exemplo: `docs: atualiza instruções de contribuição`.

## Testes e Pylint

Execute os testes antes de publicar a branch:

```bash
python -m pytest -q
```

Para executar manualmente as verificações configuradas no pre-commit em todos os arquivos:

```bash
pre-commit run --all-files
```

## Publicar a branch e abrir o Pull Request

Envie a branch para o repositório remoto:

```bash
git push -u origin tipo/descricao-curta
```

Abra um Pull Request com destino à branch `main`. Descreva o problema e a solução, informe os testes executados e destaque qualquer mudança que exija atenção de quem revisa.

## Revisar e integrar à branch principal

Revise o diff e os resultados das verificações. A pessoa autora deve responder aos comentários e atualizar a branch quando necessário; depois, execute novamente os testes e o pre-commit.

Integre o Pull Request à `main` somente depois das revisões e verificações exigidas pelo projeto. Evite integrar mudanças com conflitos ou verificações pendentes.
