def fun_deposito(deposito, saldo):
    if deposito <= 0.0:
        print("Digite uma Valor Válido")
    else:
        saldo = saldo + deposito
        print (f"Seu novo saldo e: {saldo}")
    return deposito, saldo


def fun_saque(saque, saldo, saques_realizados):
    if saque > saldo:
        print ("Saldo Insuficiente")
    elif saque > 500.00:
        print ("Limite de R$500.00")
    elif saques_realizados >= 3:
        print ("Limite de 3 Saques")
    else:
        saques_realizados+=1
        saldo = saldo - saque
        print (f"Seu novo saldo e: {saldo}")
    return saque, saldo, saques_realizados


def fun_extrato(saldo, operacao, extrato):
    print(f"Seu Saldo e: {saldo}")
    for i in range (len (extrato)):
        print(operacao[i], end="")
        print(extrato[i])


def main():

    saldo = 0
    saques_realizados = 0
    operacao = []
    extrato = []

    while True:


        print("""
              
                                        Bem-Vindo ao Banco
     
        Depósito (1) || Saque (2) || Extrato (3) || Cadastro (4) || Conta (5) || Sair (6)
        """)


        opcao = int(input("Escolha uma Opção "))

        if opcao == 1:
            print ("Quanto deseja depositar?")
            deposito = float(input())
            deposito, saldo = fun_deposito(deposito, saldo)
            operacao.append ("Depósito de: R$")
            extrato.append(deposito)

        elif opcao == 2:
            print ("Quanto deseja sacar?")
            saque = float(input())
            saque, saldo, saques_realizados = fun_saque(saque, saldo, saques_realizados)
            operacao.append ("Saque de: R$")
            extrato.append(saque) 

        elif opcao == 3:
            fun_extrato(saldo, operacao, extrato)

        elif opcao == 4:
            break
        else:
            print("Escolha uma Opção Válida")

main()