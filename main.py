saldo = 0
saques_realizados = 0
extrato = []

while 1 == 1:

    print("""Bem-Vindo ao Banco
      
      Depósito (1) || Saque (2) || Extrato (3) || Sair (4)
      """)

    opcao = int(input("Escolha uma Opção"))
    

    if opcao == 1:
        print ("Quanto deseja depositar?")
        deposito = int(input())
        if deposito < 0:
            print("Digite uma Valor Válido")
        else:
            saldo = saldo + deposito
            extrato.append(deposito)
            print (f"Seu novo saldo e: {saldo}")


    elif opcao == 2:
        qtd_saques = 0
        print ("Quanto deseja sacar?")
        saque = int(input())
        if saque > saldo:
            print ("Saldo Insuficiente")
        elif saque > 500:
            print ("Valor Inválido")
        elif saques_realizados >= 3:
            print ("Muitos Saques por Hoje")
        else:
                saques_realizados+=1
                saldo = saldo - saque
                extrato.append(-saque)
                print (f"Seu novo saldo e: {saldo}")
            
        
    elif opcao == 3:
        print(f"Seu Saldo e: {saldo}")
        print(extrato[::])


    elif opcao == 4:
        break

    else:
        print("Escolha uma Opção Válida")