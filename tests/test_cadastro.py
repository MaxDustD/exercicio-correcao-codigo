import copy

import pytest

from cadastro import CadastroPessoas
from pessoa import Pessoa
from repositorio_pessoas_memoria import (
    RepositorioPessoasMemoria,
)

class RepositorioDeCopias(RepositorioPessoasMemoria):

    def buscar(self, nome):
        pessoa = super().buscar(nome)
        if pessoa is None:
            return None

        return copy.copy(pessoa)

@pytest.mark.parametrize(
    "fabrica",
    [RepositorioPessoasMemoria, RepositorioDeCopias]
)
def test_alterar_persiste(fabrica):
    repositorio = fabrica()
    repositorio.cadastrar(
        Pessoa("Ana Souza", 30, "ana@example.com")
    )

    cadastro = CadastroPessoas(repositorio)
    cadastro.alterar(
        "Ana Souza",
        "Ana Souza",
        31,
        "ana.s@example.com"
    )

    pessoa = repositorio.buscar("Ana Souza")

    assert pessoa is not None
    assert pessoa.getIdade() == 31
    assert pessoa.getEmail() == "ana.s@example.com"

def test_cadastrar_pessoa():
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ronaldo", 20, "ronaldo@gmail.com")

    pessoas = cadastro.listar()

    assert len(pessoas) == 1
    assert pessoas[0].getNome() == "Ronaldo"
    assert pessoas[0].getIdade() == 20
    assert pessoas[0].getEmail() == "ronaldo@gmail.com"

def test_buscar_por_nome():
    cadastro = CadastroPessoas()
    cadastro.cadastrar("Ronaldo", 20, "ronaldo@gmail.com")

    encontrada = cadastro.buscarPorNome("Ronaldo")

    assert encontrada is not None
    assert encontrada.getNome() == "Ronaldo"
    assert encontrada.getIdade() == 20
    assert encontrada.getEmail() == "ronaldo@gmail.com"
