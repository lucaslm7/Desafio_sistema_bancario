menu = '''


[d] Deposito
[s] Saque
[e] Extrato
[q] Sair

'''

saldo = 0 
limite = 500
extrato = ''
numeros_saque = 0
LIMITES_SAQUE = 3

while True:

    opcao = input(menu)
    
    if opcao == 'd':
        valor = float(input('Informe o valor do seu depósito:\n==> '))
        
    
        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor: .2f}\n'
            print('DEPÓSITO FOI REALIZADO COM SUCESSO.')
            print(f'\nVALOR DO DEPÓSITO: R$ {valor: .2f}')
            print(f'VALOR NA CONTA CORRENTE: {saldo}')
            
        else:
            print('A operação falhou, o valor informado é invalido.')
    
    elif opcao == 's':
        valor = float(input('Informe o valor desejado:' ))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numeros_saque >= LIMITES_SAQUE

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')
        
        elif excedeu_limite:
            print('Operação falhou! O valor de saque excede o limite.')

        elif excedeu_saques:
            print('Operação falhou! Você excedeu o limite de saques diário.')

        if valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor: .2f}\n'
            numeros_saque += 1

        else:
            print('Operação falhou! o valor informado é inválido.')

    elif opcao == 'e':
        print('\n ====================== EXTRATO =======================')
        print('Não foram realizadas movimentações') if not extrato else extrato
        print(f'\n Saldo: R$ {saldo: .2f}')
        print('=======================================')

    elif opcao == 'q':
        break
    else:
        print('Operação inválida, por favor selecione novamente a operação desejada.')



           




