print("#########  Sistema de calculadora #########")

login = input('Digite seu login: ')
senha = input('Digite sua senha: ')

if login != ('admin') and senha != ('admin'):
     print('Você errou a senha ! tente novamente.')
elif login == ('admin') and senha == ('admin'):
     print('Você logou com sucesso... ')

     continuar = 'sim'
     while continuar == 'sim':
        operacao = input('''Deseja realizar qual operação:     
         + para adicão   
        - para subtração
         / para divisão
         * para mutiplicação 
         '''  )

        numero1 = int(input('Insira o primeiro numero: '))
        numero2 = int(input('Insira o segundo numero: '))        
        print(numero1, operacao, numero2)
        
        if operacao == '+':
          resultado = (numero1 + numero2)
          print(resultado)
        elif operacao == '-':
          resultado = (numero1 - numero2)
          print(resultado)         
        elif operacao == '/':
          resultado = (numero1 / numero2)
          print(resultado)          
        elif operacao == '*':
          resultado = (numero1 * numero2)
          print(resultado)       

        continuar = input('Deseja fazer outra conta ? ')
print('O programa foi encerrado !')