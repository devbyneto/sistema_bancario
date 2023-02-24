saldo = 0
saques_no_dia = 0
extrato = []

while True:

    menu = input('''
======== MENU ========
[S] SACAR
[D] DEPOSITAR
[E] EXTRATO
[0] SAIR
======================
''')
    
    while menu.upper() != 'S' and menu.upper() != 'D' and menu.upper() != 'E' and menu != '0':
        print('Digite uma opção válida!')
        menu = input('''
======== MENU ========
[S] SACAR
[D] DEPOSITAR
[E] EXTRATO
[0] SAIR
======================
''')

    if menu.upper() == 'S':
               
        verificacao_saques_no_dia = saques_no_dia < 3

        if verificacao_saques_no_dia == False:          
            print('Você pode fazer apenas três saques por dia.')

        else:
            
            valor_saque = float(input('Digite o valor a ser sacado: '))
            verificacao_saldo = saldo > valor_saque
            verificacao_limite = valor_saque <= 500

            if verificacao_saldo == False:
                print('Não há saldo disponível!')
                if verificacao_limite == False:
                    print('E seu limite só permite sacar 500.')
            
            else:
                if verificacao_limite == False:
                    print('Seu limite de saque é 500.')

                else:
                    print('Saque realizado!')
                    saldo = saldo - valor_saque
                    saques_no_dia = saques_no_dia + 1
                    extrato.append(f'Saque: R$ {valor_saque}')

    if menu.upper() == 'E':

        if len(extrato) == 0:
            print('Não foram realizdas movimentações.')

        else:
            for i in extrato:
                print(i)
            print(f'Saldo atual: {saldo}')

    if menu.upper() == '0':
        print('Vejo você na próxima!')
        break

    if menu.upper() == 'D':
        
        valor_deposito = float(input('Digite o valor a ser depositado: '))
        
        while valor_deposito <= 0:
            valor_deposito = float(input('O valor precisa ser maior que zero: '))

        saldo = saldo + valor_deposito
        print('Depósito realizado!')
        extrato.append(f'Depósito: R$ {valor_deposito}')