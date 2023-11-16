from ctypes import pythonapi


pythonapi

def withdrawal(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_limite = valor > limite
    excedeu_saldo = valor > saldo
    excedeu_saques = numero_saques > limite_saques


    if excedeu_limite:
        print('Operação falhou! O valor do saque excede o limite diário.')
        
    elif excedeu_saldo:
        print('Operação falhou! Você não tem saldo suficiente.')
    
    elif excedeu_saques:
        print('Operação falhou! Você excedeu o limite de saques.')


    elif valor > 0:
        numero_saques += 1
        saldo = saldo - valor
        extrato.append(f'Saque de R$ {valor:.2f}')
        print('Saque realizado com sucesso!')
        print(numero_saques)
        print(limite_saques)


    else:
        print('Operação falhou! O valor informado é inválido.')


    return saldo, extrato