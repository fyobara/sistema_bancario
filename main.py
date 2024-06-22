saldo = 0
saques_realizados = 0
operacao = []
extrato = []

while 1 == 1:

    print("""Bem-Vindo ao Banco
      
      Depósito (1) || Saque (2) || Extrato (3) || Sair (4)
      """)

    opcao = int(input("Escolha uma Opção"))
    

    if opcao == 1:
        print ("Quanto deseja depositar?")
        deposito = float(input())
        if deposito < 0:
            print("Digite uma Valor Válido")
        else:
            saldo = saldo + deposito
            operacao.append ("Depósito de: R$")
            print (f"Seu novo saldo e: {saldo}")
            extrato.append(deposito)


    elif opcao == 2:
        qtd_saques = 0
        print ("Quanto deseja sacar?")
        saque = float(input())
        if saque > saldo:
            print ("Saldo Insuficiente")
        elif saque > 500.00:
            print ("Valor Inválido")
        elif saques_realizados >= 3:
            print ("Muitos Saques por Hoje")
        else:
                saques_realizados+=1
                saldo = saldo - saque
                extrato.append(saque)
                operacao.append ("Saque de: R$")
                print (f"Seu novo saldo e: {saldo}")
            
        
    elif opcao == 3:
        print(f"Seu Saldo e: {saldo}")

        for i in range (len (extrato)):
            print(operacao[i], end="")
            print(extrato[i])


    elif opcao == 4:
        break

    else:
        print("Escolha uma Opção Válida")