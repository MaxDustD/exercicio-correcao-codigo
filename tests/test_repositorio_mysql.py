import os
import uuid

import pytest

from pessoa import Pessoa
from repositorio_pessoas_mysql import (
    RepositorioPessoasMySQL,
)

pytestmark = pytest.mark.skipif(
    "TESTE_DB_NAME" not in os.environ,
    reason="Sem banco de testes",
)

@pytest.fixture
def repo():
    banco = os.environ["TESTE_DB_NAME"]
    assert banco != "cadastro", "use banco de testes"
    return RepositorioPessoasMySQL(
        host=os.environ["TESTE_DB_HOST"],
        port=int(os.environ["TESTE_DB_PORT"]),
        usuario=os.environ["TESTE_DB_USER"],
        senha=os.environ["TESTE_DB_PASSWORD"],
        banco=banco,
    )

def test_cadastrar_e_buscar(repo):
    nome = f"Teste-{uuid.uuid4().hex[:8]}"
    email = f"{nome.lower()}@t.example"
    repo.cadastrar(Pessoa(nome, 20, email))
    pessoa = repo.buscar(nome)
    assert pessoa is not None
    assert pessoa.getEmail() == email

def test_alterar_inexistente(repo):
    nova = Pessoa("Sem Nome", 1, "sn@t.example")
    inexistente = f"Inexistente-{uuid.uuid4().hex[:8]}"
    assert repo.alterar(inexistente, nova) is False