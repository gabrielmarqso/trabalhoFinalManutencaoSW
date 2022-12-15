from cadastro import menu, cadastrar, pesquisar_por_nome, pesquisar_por_data, remover, alterar

#Loop principal
while True:
    #Exibe o menu e lê a opção escolhida pelo usuário
    opcao = menu()

    #Verifica a opção escolhida
    if opcao == 1:
        #Cadastrar registro
        cadastrar()
    elif opcao == 2:
        #Pesquisar registro por nome
        pesquisar_por_nome()
    elif opcao == 3:
        #Pesquisar registro por data de nascimento
        pesquisar_por_data()
    elif opcao == 4:
        #Remover registro
        remover()
    elif opcao == 5:
        #Alterar registro
        alterar()
    elif opcao == 0:
        #Sair do programa
        break


