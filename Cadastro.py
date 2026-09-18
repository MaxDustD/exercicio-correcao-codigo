''' Sistema de Cadastro de Pessoas '''

def exibir_menu():
    # Exibe o menu para seleção de opções
    print("=========================")
    print(" CADASTRO DE PESSOAS")
    print("=========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Avalisar cadastro")
    print("6 - Sair")
    return int(input("Escolha uma opcao: "))
 
def cadastrar_pessoa(nomes, idades, emails):
    # Cadastro de pessoa com nome, idade e email. Também retorna se é maior de idade
    nome = input("Informe o nome: ")
    nomes.append(nome)
    idade = int(input("Informe a idade: "))
    idades.append(idade)
    email = input("Informe o email: ")
    emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(nomes, idades, emails, pos):
    # Impressão do nome, idade e email de uma pessoa a partir de uma posição
    print("Nome: " + nomes[pos])
    print("Idade: " + str(idades[pos]))
    print("E-mail: " + emails[pos])
    if idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")
 
def buscar_pessoa(nomes, nome_procurado):
    # Busca de pessoa a partir de um nome para ser procurado
    pos = 0
    while pos < len(nomes):
        if nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def consultar_pessoa(nomes, idades, emails):
    # Verifica se determinada pessoa existe. Se sim, faz exibição de seus dados
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(nomes, idades, emails, pos)

def alterar_pessoa(nomes, idades, emails):
    # Modifica todos os dados de uma pessoa a partir de um nome para procurar
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        nomes[pos] = input("Novo nome: ")
        idades[pos] = int(input("Nova idade: "))
        emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada!")
        exibir_pessoa(nomes, idades, emails, pos)

def listar_pessoas(nomes, idades, emails):
    # Mostra todas as pessoas que estiverem cadastradas
    if len(nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(nomes):
        exibir_pessoa(nomes, idades, emails, pos)
        print("-------------------------")
        pos = pos + 1
    print("Total: " + str(len(nomes)))


def analisar_faixa_etaria(idade):
    # Verifica a idade de uma pessoa, de criança até idoso
    if idade < 12:
        print("Faixa etaria: crianca")
    elif idade < 18:
        print("Faixa etaria: adolescente")
    elif idade < 60:
        print("Faixa etaria: adulto")
    else:
        print("Faixa etaria: idoso")

def analisar_contato(idade, email):
    # Verifica se uma pessoa é menor de idade e se o contato está faltando algo
    if idade >= 18 and "@" in email:
        print("Contato: completo")
    elif idade >= 18:
        print("Contato: e-mail invalido")
    else:
        print("Contato: menor de idade")

def analisar_email(email):
    # Analisa se o email é válido e o provedor
    if "@" not in email:
        print("E-mail invalido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    else:
        print("Provedor: outro")

def analisar_pessoa(nomes, idades, emails):
    # Faz a analise de idade, email e contato de uma pessoa 
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = idades[pos]
        email = emails[pos]

        analisar_faixa_etaria(idade)
        analisar_email(email)
        analisar_contato(idade, email)

nomes = []
idades = []
emails = []
 
quantidade = 0
opcao = 0
 
while opcao != 6:

    opcao = exibir_menu()
 
    if opcao == 1:
        cadastrar_pessoa(nomes, idades, emails)
    elif opcao == 2:
        consultar_pessoa(nomes, idades, emails)
    elif opcao == 3:
        alterar_pessoa(nomes, idades, emails)            
    elif opcao == 4:
        listar_pessoas(nomes, idades, emails)
    elif opcao == 5:
        analisar_pessoa(nomes, idades, emails)
    elif opcao == 6:
        print("Saindo...") 
    else:
        print("Opcao invalida")
 
print("Fim do programa")
