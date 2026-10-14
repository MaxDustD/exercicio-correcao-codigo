from cadastro import CadastroPessoas

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
