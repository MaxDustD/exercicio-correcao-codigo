# Cadastro de Pessoas

Projeto evolutivo de cadastro de pessoas em Python, utilizado na disciplina Gestão da Qualidade de Software para práticas de modularização, qualidade de código e versionamento com Git.

Desenvolvido para a disciplina **Gestão da Qualidade de Software**, o programa oferece um menu de terminal para cadastrar, consultar, alterar e listar pessoas, além de analisar faixa etária e e-mail.

## Objetivo e organização dos arquivos

O projeto serve como base para praticar modularização, qualidade de código, testes e versionamento. Os principais arquivos são:

- `src/main.py`: menu e interação com a pessoa usuária.
- `src/pessoa.py`: modelo de pessoa (nome, idade e e-mail).
- `src/cadastro.py`: operações de cadastro.
- `src/repositorio_pessoas.py`: contrato do repositório.
- `src/repositorio_pessoas_memoria.py`: implementação em memória.
- `tests/`: testes automatizados.
- `infra/compose.yaml`: serviços MySQL para atividades de infraestrutura.

## Requisitos e ambiente python

- Python 3.14 ou superior (versão indicada nas convenções de contribuição).
- Para usar os serviços de banco, Docker com Docker Compose.

Crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No macOS/Linux:

```bash
source .venv/bin/activate
```

Depois, em qualquer plataforma:

```bash
python -m pip install -r requirements.txt
```

## Docker, contêineres

O arquivo `infra/compose.yaml` define dois serviços MySQL (`principal` e `replica`), disponíveis na máquina local nas portas `3307` e `3308`, respectivamente. Para iniciá-los e encerrá-los:

```bash
docker compose -f infra/compose.yaml up -d
docker compose -f infra/compose.yaml down
```

O Compose configura a variável `MYSQL_ROOT_PASSWORD` para os contêineres. O valor definido no arquivo é destinado ao ambiente de estudo; altere-o antes de usar em outro contexto.

## Tabela pessoa e variáveis de ambiente

O modelo `Pessoa` contém os campos nome, idade e e-mail. Atualmente, não há tabela SQL implementada nem variáveis de ambiente para conexão: os serviços MySQL são infraestrutura disponível para a evolução do exercício, mas ainda não são usados pelo programa.

## Executar e escolher a persistência

Na raiz do projeto, execute o programa e os testes com:

```bash
python src/main.py
pytest
```

Por padrão, o cadastro usa o repositório em sql, configurado em `src/main.py` na variável `USAR_MYSQL`. Para usar o repositório em memória, basta definir como `FALSE`. O repositório usa persistência local. 
