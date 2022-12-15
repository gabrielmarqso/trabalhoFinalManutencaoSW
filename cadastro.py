import datetime
import os

def menu():
    print("Menu Principal ")
    print()
    print ("[1] - Cadastrar registro")
    print ("[2] - Pesquisar registro por nome")
    print ("[3] - Pesquisa registro por data de nascimento")
    print ("[4] - Remover registro")
    print ("[5] - Alterar registro")
    print ("[0] - Sair")
    opcao = int(input("Entre a opção desejada:"))
    return opcao

def cadastrar():
    #Lê o nome do registro
    nome = input("Entre com o nome: ")
    nascimento = input("Entre com a data de nascimento (DD/MM/AAAA): ")

    #Cria ou abre o arquivo "banco.dbc"
    with open("banco.dbc", "a") as arquivo:
        #Escreve os dados da pessoa no arquivo
        arquivo.write(nome + "," + nascimento + "\n")
    #Mostra uma mensagem de sucesso
    print("Concluido com sucesso. Pressione <Enter> para continuar... ")


def pesquisar_por_nome():
    #Lê o nome a ser pesquisado no arquivo
    nome  = input("Entre com o nome: ")

    #Cria ou abre o arquivo "banco.dbc"
    with open("banco.dbc", "r") as arquivo:
        linhas = arquivo.readlines()

        #flag que indica se o nome foi encontrado
        encontrado = False

        #Percorre todas as linhas do arquivo
        for linha in linhas:
            #Divide a linha em campos (nome e data de nascimento)
            campos = linha.split(",")

            #Verifica se o nome no arquivo é igual ao nome pesquisado
            if campos[0] == nome:
                #O nome foi encontrado
                encontrado = True

                #Obtém a data de nascimento e a data atual
                nascimento = datetime.datetime.strptime(campos[1].replace("\n", ""),"%d/%m/%Y")
                atual = datetime.datetime.now()

                #Calcula a idade do registro
                idade = atual.year - nascimento.year
                if atual.month < nascimento.month or (atual.month == nascimento.month and atual.day < nascimento.day):
                    idade -= 1

                #Exibe os dados do registro
                print("Nome: ", nome)
                print("Data de nascimento: ", nascimento.strftime("%d/%m/%Y"))
                print("Data Atual: ", atual.strftime("%d/%m/%Y"))
                print("Idade: ", idade)
                print()
        if not encontrado:
            print("Nenhum registro encontrado com o nome '" + nome + "'.")

def pesquisar_por_data():
    nascimento = input("Entre com a data de nascimento (DD/MM/AAAA): ")

    with open("banco.dbc", "r") as arquivo:
        #Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

        #Flag q indica se a data de nascimento foi encontrada
        encontrado = False

        #Percorre todas linhas do arquivo
        for linha in linhas:
            #Divide a linha em campos (nome e data de nascimento)
            campos = linha.replace("\n", "").split(",")

            #Verifica se a data de nascimento no arquivo orignal é igual a data pesquisada
            if campos[1] == nascimento:
                print("foi ")
                #A data de nascimento foi encontrada
                encontrado = True

                #Obtém o nome a data atual
                nome = campos[0]
                atual = datetime.datetime.now()

                #Converte a data de nascimento em um objeto datetime
                nascimento = datetime.datetime.strptime(campos[1], "%d/%m/%Y")

                #Calcula a idade da pessoa
                idade = atual.year - nascimento.year
                if atual.month < nascimento.month or (atual.month == nascimento.month and atual.day < nascimento.day):
                    idade -= 1

                #Exibe os dados do registro
                print("Nome: ", nome)
                print("Data de nascimento: ", nascimento.strftime("%d/%m/%Y"))
                print("Data Atual: ", atual.strftime("%d/%m/%Y"))
                print("Idade: ", idade)
                print()

            if not encontrado:
                print("Nenhum registro encontrado com a data de nascimento: '" + nascimento + "'.")

def remover():
    nome = input("Entre com o nome: ")
    with open("banco.dbc", "r") as arquivo:
        #Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

        #Flag q indica se o nome foi encontrado
        encontrado = False

        for linha in linhas:
            #Divide a linha em campos (nome e data de nascimento)
            campos = linha.split(",")

            #Verifica se o nome no arquivo é igual ao nome pesquisado
            if campos[0] == nome:
                #O nome foi encontrado
                encontrado = True

                #Remove a linha do arquivo
                linhas.remove(linha)
        #Se o nome foi encontrado, reescreve o arquivo sem a linha removida
        if encontrado:
            with open("banco.dbc", "w") as arquivo:
                for linha in linhas:
                    arquivo.write(linha)

                #Exibe uma mensagem de sucesso
                print("Registro removido com sucesso!")
        else:
            #Se o nome não foi encontrado, exibe uma mensagem
            print("Nenhum registro encontrado com o nome '" + nome + "'.")


def alterar():
    #Lê o nome a ser alterado
    nome = input("Entre com o nome: ")

    #Cria ou abre o arquivo "banco.dbc"
    with open("banco.dbc", "r") as arquivo:
        #Lê todas as linhas do arquivo
        linhas = arquivo.readlines()

        #Flag q indica se o nome foi encontrado
        encontrado = False

        #Percorre todas as linhas do arquivo
        for linha in linhas:
            #Divide a linha em campos (nome e data de nascimento)
            campos = linha.split(",")

            #Verifica se o nome no arquivo é igual ao nome pesquisado
            if campos[0] == nome:
                #O nome foi encontrado
                encontrado = True

                #Lê os novos dados da pessoa
                novo_nome = input("Insira o novo nome: ")
                nova_data = input("Insira a nova daa de nascimento (DD/MM/AAAA): ")

                #Substitui a linha antiga pela nova
                linhas[linhas.index(linha)] = novo_nome + "," + nova_data + "\n"


        #Se o nome foi encontrado, reescreve o arquivo com a linha alterada
        if encontrado:
            with open("banco.dbc", "w") as arquivo:
                for linha in linhas:
                    arquivo.write(linha)

            #Exibe uma mensagem de sucesso
            print("Registro alterado com sucesso...")
        else:
            #Se o nome não foi encontrado, exibe uma mensagem
            print("Nenhum registro encontrado com o nome '" + nome + "'.")
