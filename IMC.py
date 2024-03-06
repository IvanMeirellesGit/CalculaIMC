def calcula_imc(p, a):
    if p <= 0 or a <= 0:
        return None # Retorna None se peso ou altura não forem válidos
    imc = (p / (a**2))
    return imc


print('Ola! Bem vindo ao programa IMC')

nome = input('Me diga seu nome: ')


try:
    altura = float(input(f'Agora {nome} me diga sua altura (em metros): '))
    peso = float(input(f'Agora {nome} me diga seu peso (em quilogramas): '))
except ValueError:
    print('Por favor, insira valores válidos para altura e peso.')
    exit()

IMC = calcula_imc(peso, altura)

if IMC is None:
    print('Valores inválidos para altura ou peso.')
else:
    print(f'Seu IMC é {IMC:.2f}')

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
