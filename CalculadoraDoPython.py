import time

while True:
    def menu():
        op = input('''Bem vindo à calculadora do Python. Selecione qual operação você deseja fazer:
        (1) Adição;
        (2) Subtração;
        (3) Multiplicação;
        (4) Divisão;
        (5) Sair da calculadora.
        ''')
        try:
            int(op)
        except:
            print('Valor inválido, tente novamente.')
            print('')
            time.sleep(1)
            return menu()
        else:
            op = int(op)
            if op < 1 or op > 5:
                print('Valor inválido, tente novamente.')
                print('')
                time.sleep(1)
                return menu()
            if op == 5:
                print('Obrigado por usar a calculadora do Python! Volte sempre!')
                print('--------------------------------------------------------')
                time.sleep(1)
                exit()
                return menu()
            else:
                return op


    x = menu()


    def soma(a, b):
        return a + b


    def subtracao(a, b):
        return a - b


    def multiplicacao(a, b):
        return a * b


    def divisao(a, b):
        if b == 0:
            return 'Não é possível dividir por 0. '
        else:
            return a / b


    def val():
        try:
            a = float(input('Insira o primeiro valor:\n'))
        except:
            print('Valor inválido, tente novamente.')
            print('')
            time.sleep(1)
            return val()
        try:
            b = float(input('Insira o segundo valor:\n'))
        except:
            print('Valor inválido, tente novamente.')
            print('')
            time.sleep(1)
            return val()
        if x == 1:
            return soma(a, b)
        if x == 2:
            return subtracao(a, b)
        if x == 3:
            return multiplicacao(a, b)
        if x == 4:
            return divisao(a, b)


    y = val()


    def operacao():
        if x == 1:
            return 'adição'
        if x == 2:
            return 'subtração'
        if x == 3:
            return 'multiplicação'
        if x == 4:
            return 'divisão'


    z = operacao()

    if y == 'Não é possível dividir por 0. ':
        print('Não é possível dividir por 0.')
    else:
        print(f'O resultado da {z} é {y}.')
    print('---------------------------------------')
    time.sleep(1)
