def calcula_imc(p, a):
    imc = (p / (a**2))
    print(f'Seu IMC é {imc:.2f}')
    return IMC


print('Ola! Bem vindo ao programa IMC')
nome = input('Me diga seu nome: ')

altura = float(input(f'Agora {nome} me diga sua altura :'))
peso = float(input(f'Agora {nome} me diga seu peso :'))

IMC = calcula_imc(peso, altura)

if IMC < 17:
    print(f'{nome}, seu IMC está MUITO ABAIXO do peso.')
elif IMC < 18.5:
    print(f'{nome}, seu IMC está ABAIXO do peso.')
elif IMC < 25:
    print(f'{nome}, seu IMC está NORMAL para o peso.')
elif IMC < 30:
    print(f'{nome}, seu IMC esta ACIMA do peso.')
elif IMC < 35:
    print(f'{nome}, seu IMC esta OBESIDADE GRAU I.')
elif IMC < 40:
    print(f'{nome}, seu IMC esta MOBESIDADE GRAU II.')
else:
    print(f'Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.')
