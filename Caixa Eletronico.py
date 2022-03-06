from login import login

nao_tem_conta = login.nao_tem_conta()

print('=' * 80)
print('****************************** Caixa eletronico*********************************')
print('*****************************Roubando seu dinheiro******************************')
print('=' * 80)
print('Bem vindo ao seu caixa eletronico !!')


continuar = 'sim'
while continuar == ('sim'):
    conta = input('Você ja tem conta ? ')
    conta == ('sim')
    if conta == ('sim'):
        login = input('Digite sua conta: ')
        senha = input('Digite sua senha: ')
    elif conta != ('sim'):
        print(nao_tem_conta)

    if login == ('0000' or login) and senha == ('admin' or senha):
        operacao = int(input('''Qual operação você deseja realizar: 
        1: Para saque
        2: Para transferencia
        3: Para emprestimo  
        4: Para sair
        : '''))
        match operacao:
            case 1: 
                saque = int(input('Digite o valor do saque: '))
                cedula = 50
                totalCedulas = 0
                while True:
                    if saque >= cedula:
                       saque -= cedula
                       totalCedulas += 1
                    else:
                        print('O total de', totalCedulas, 'cedulas de R$:', cedula)
                        if cedula == 50:
                            cedula = 20
                        elif cedula == 20:
                            cedula = 10
                        elif cedula == 10:
                             cedula = 1   
                        totalCedulas = 0
                        if saque == 0:                             
                           break                        
            case 2:
                transferencia = input('Digite o valor do transferencia: ')
                contaTrasnferida = input('Digite a conta a ser transferida: ')
                print('Foi transferido: ', transferencia, 'Para a conta: ', contaTrasnferida)
            case 3:
                emprestimo = input('Digite o valor do emprestimo: ')
                vezes = input('Em quantas vezes você deseja pagar: ')
                print('Foi emprestado a voce: ', emprestimo, 'com pagamento em : ', vezes, 'x')
            case 4:
                sair = input('Você deseja sair da operação ? ')
                if sair == ('sim'): 
                    continuar = ('nao')                    

continuar = input('Você deseja sair ? ')    
continuar = ('nao')
print('Programa encerrado até a proxima !!!!')