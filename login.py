class login:

    def __init__(self):
       pass

    def nao_tem_conta(self):
        if not self.conta:
            print('Conta Vamos fazer uma nova conta ? ')
            login = input('Digite seu novo numero de conta: ')
            senha = input('Digite sua nova senha: ')
            print('Conta ', login, ' cadastrada e senha', senha, 'cadastrada')
            print('Entre com sua conta: ')
            return login + senha



