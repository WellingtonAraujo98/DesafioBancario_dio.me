

saldo = 0
extrato = str(' ')
opcao = ' '
numero_saque = 0
LIMITE_SAQUES = 3

while opcao != '4':
    print("-*"*20)
    menu = print(
        '''
        MENU
    [1] depositar
    [2] sacar
    [3] extrato
    [4] sair
        '''
    )
    opcao = input("Selecione uma opção: ")
    if opcao == "1":
        valor = float(input("Quantos deseja depositar: "))

        if valor > 0:
            if saldo ==0:
                extrato += (f"\n")
            saldo += valor
            extrato += (f"   Deposito: R$ {valor:.2f}")
            extrato += (f"\n")
        
        else: 
            print("Valor invalido")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        # tem que ter saldo 
        # saque n pode exceder o limite de 500
        # tem o limite de 3 saques por dia
        if valor <= 0:
            print("Valor invalido")
        elif valor > 500:
            print(
                '''
                    Saque invalido!!
                O limite de saque é de R$500,00.
                ''')
        elif valor > saldo:
            print(
                '''
            Saque invalido!!
            Saldo insuficiente. 
                '''
            )
        elif numero_saque == 3:
            print("Excedeu os saques diarios ")
        
        elif valor > 0 and valor <=500:
            saldo -= valor
            extrato += (f"   Saque: R$ {valor:.2f}") 
            extrato +=(f"\n")
            numero_saque += 1

    elif opcao == "3":
        print("========= EXTRATO =========")
        if extrato == ' ':
            print("Não foram realizados movimentações.")
            print(f"   Saldo: R$ {saldo:.2f}")
            extrato += (f"\n")
        else: 
            print(extrato)
            print(f"   Saldo: R$ {saldo:.2f}")
            
        print("===========================")
    elif opcao == "4":
        print("Obrigado por utilizar esse sistema")
        
