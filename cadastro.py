""" Sistema de Cadastro de Pessoas """
import os

def exibir_menu():
    """ Exibe o menu para seleção de opções """
    print("===========================")
    print("   CADASTRO DE PESSOAS")
    print("===========================")
    print("1 - Cadastrar pessoa")
    print("2 - Consultar pessoa")
    print("3 - Alterar pessoa")
    print("4 - Listar pessoas")
    print("5 - Analisar cadastro")
    print("6 - Sair")
    return int(input("\nEscolha uma opcao: "))

def cadastrar_pessoa(lista_nomes, lista_idades, lista_emails):
    """ Cadastro de pessoa com nome, idade e email. 
        Também retorna se é maior de idade """
    nome = input("Informe o nome: ")
    lista_nomes.append(nome)
    idade = int(input("Informe a idade: "))
    lista_idades.append(idade)
    email = input("Informe o email: ")
    lista_emails.append(email)
    if idade >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos):
    """ Impressão do nome, idade e email de uma pessoa 
        a partir de uma posição """
    print("Nome: " + lista_nomes[pos])
    print("Idade: " + str(lista_idades[pos]))
    print("E-mail: " + lista_emails[pos])
    if lista_idades[pos] >= 18:
        print("Situacao: Maior de idade")
    else:
        print("Situacao: Menor de idade")

def buscar_pessoa(lista_nomes, nome_procurado):
    """ Busca de pessoa a partir de um nome para ser procurado """
    pos = 0
    while pos < len(lista_nomes):
        if lista_nomes[pos] == nome_procurado:
            return pos
        pos = pos + 1
    return -1

def consultar_pessoa(lista_nomes, lista_idades, lista_emails):
    """ Verifica se determinada pessoa existe.
        Se sim, faz exibição de seus dados """
    procurado = input("Nome para consultar: ")
    pos = buscar_pessoa(lista_nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)

def alterar_pessoa(lista_nomes, lista_idades, lista_emails):
    """ Modifica todos os dados de uma pessoa a partir
        de um nome para procurar """
    procurado = input("Nome para alterar: ")
    pos = buscar_pessoa(lista_nomes, procurado)
    if pos == -1:
        print("Nao encontrado")
    else:
        lista_nomes[pos] = input("\nNovo nome: ")
        lista_idades[pos] = int(input("Nova idade: "))
        lista_emails[pos] = input("Novo e-mail: ")
        print("Pessoa alterada!")
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)

def listar_pessoas(lista_nomes, lista_idades, lista_emails):
    """ Mostra todas as pessoas que estiverem cadastradas """
    if len(lista_nomes) == 0:
        print("Nenhuma pessoa cadastrada")
    pos = 0
    while pos < len(lista_nomes):
        exibir_pessoa(lista_nomes, lista_idades, lista_emails, pos)
        print("===============================")
        pos = pos + 1
    print("Total: " + str(len(lista_nomes)))

def analisar_faixa_etaria(idade):
    """ Verifica a idade de uma pessoa, de criança até idoso """
    if idade < 12:
        print("Faixa etaria: crianca")
    elif idade < 18:
        print("Faixa etaria: adolescente")
    elif idade < 60:
        print("Faixa etaria: adulto")
    else:
        print("Faixa etaria: idoso")

def analisar_contato(idade, email):
    """ Verifica se uma pessoa é menor de idade 
        e se o contato está faltando algo """
    if idade >= 18 and "@" in email:
        print("Contato: completo")
    elif idade >= 18:
        print("Contato: e-mail invalido")
    else:
        print("Contato: menor de idade")

def analisar_email(email):
    """ Analisa se o email é válido e o provedor """
    if "@" not in email:
        print("E-mail invalido")
    elif email.endswith("@gmail.com"):
        print("Provedor: Gmail")
    elif email.endswith("@outlook.com"):
        print("Provedor: Outlook")
    else:
        print("Provedor: outro")

def analisar_pessoa(lista_nomes, lista_idades, lista_emails):
    """ Faz a análise de idade, email e contato de uma pessoa """ 
    procurado = input("Nome para analisar: ")
    pos = buscar_pessoa(lista_nomes, procurado)

    if pos == -1:
        print("Pessoa nao encontrada")
    else:
        idade = lista_idades[pos]
        email = lista_emails[pos]

        analisar_faixa_etaria(idade)
        analisar_email(email)
        analisar_contato(idade, email)

nomes = []
idades = []
emails = []

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

    if opcao != 6:
        input("\nPressione Enter para voltar ao menu...")
        os.system("cls")

print("Fim do programa")
