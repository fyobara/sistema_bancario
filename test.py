class Usuarios():

    def __init__(self, nome, cpf, senha):
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.usuarios = usuarios = []


    def registrar_usuarios(self, nome, cpf, senha):
        self.usuarios.append (nome)
        self.usuarios.append (cpf)
        self.usuarios.append (senha)
    


class Conta():

    def __init__(self, saldo):
        self.saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def set_saldo(self, novo_valor):
        self._saldo += novo_valor
        return self._saldo




def main():
    while True:


        print(f"""
             
                         Bem-Vindo ao Banco



        Depósito (1) || Saque (2) || Extrato (3) || Sair (4)
                           
        """)


        opcao = input("Escolha uma Opção ")


        if opcao == "1":
            print ("Quanto deseja depositar?")
            valor_deposito = float(input())
           




        elif opcao == "2":
            print ("Quanto deseja sacar?")
            saque = float(input())




        elif opcao == "3":
            pass




        elif opcao == "4":
            break
           
        else:
            print("Escolha uma Opção Válida")






def entrar():




    print("""
             
                Bem-Vindo ao Banco

                    Cadastro (C)
    """)




    opcao = input("Escolha uma Opção ")


    if opcao == "c" or opcao == "C":
        nome = input("Insira seu Nome ")
        cpf = input("Insira seu CPF ")
        senha = input("Insira uma Senha ")
        user = Usuarios(nome, cpf, senha)           #Criar Instância
        user.registrar_usuarios(nome, cpf, senha)   #Listar Instância
        print("Usuário Cadastrado com Sucesso ")
        main()


entrar()



