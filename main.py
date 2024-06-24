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


def fun_cadastro(cpf, cadastros):
    usuario = fun_filtrar_usuarios(cpf, cadastros)
    if usuario:
        print("CPF Já Cadastrado, Tente Novamente")
    else:
        nome = input("Digite seu Nome")
        data_nascimento = input("Digite sua Data de Nascimento (dd-mm-aaaa)")
        endereco = input("Digite seu Endereco (Logradouro-Número-Bairro-Cidade-Estado)")
        cadastros.append({"cpf": cpf, "nome": nome, "data_nascimento": data_nascimento, "endereco": endereco,})
        print("Cadastro Realizado")
        print(cadastros[-1])
    return cpf, cadastros


def fun_filtrar_usuarios (cpf, cadastros):
    usuarios_filtrados = [usuario for usuario in cadastros if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def fun_criar_conta(cpf, cadastros, contas):
    usuario = fun_filtrar_usuarios(cpf, cadastros)
    if usuario:
        conta = len(contas) + 1
        contas.append({"usuario": usuario, "agencia": "0001", "conta": conta,})
        print("Conta Criada com Sucesso")
        print(contas[-1])
    else:
        print("Faça seu Cadastro")
    return cpf, cadastros, contas


def main():

    saldo = 0
    saques_realizados = 0
    operacao = []
    extrato = []
    cadastros = []
    contas = []


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
            cpf = input("Digite seu CPF")
            cpf, cadastros = fun_cadastro(cpf, cadastros)

        elif opcao == 5:
            cpf = input("Digite seu CPF")
            cpf, cadastros, contas = fun_criar_conta(cpf, cadastros, contas)

        elif opcao == 6:
            break
        else:
            print("Escolha uma Opção Válida")

main()