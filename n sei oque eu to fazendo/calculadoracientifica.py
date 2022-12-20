"calculadora cientifica"

"numeros"

numero1 = 0
numero2 = 0
num = 0
resultado = ''

"escolha"

print('raiz')
print('elevação')
print('porcentagem')

operacao = input('escolha qual conta deseja fazer:')

"raiz"

if operacao == 'raiz':

    print('quadrada')
    print('cubo')
    operacao2 = input('Qual a raiz:')
    if operacao2 == 'quadrada':
        num = int(input('Digite o numero da raiz:'))
        raizq =num ** (1/2)
        resultado = print(f'\nA raiz quadrada de {num} é {raizq}\n')
    elif operacao2 == 'cubo':
        num = int(input('Digite o numero da raiz:'))
        raizc = num ** (1/3)
        resultado = print(f'\nA raiz cubica de {num} é {raizc}\n')
else:
    resultado = 'Resposta invalida'

"elevação"

if operacao == 'elevação':

    numE = int(input('Digite o numero a ser elevado:'))
    numD = int(input('Digite o numero da elevação:'))
    resultado = print('A elevação resultou em', numE ** numD)

"porcentagem"

if operacao == 'porcentagem':
    
    numero1 = int(input('Digite o valor:'))
    numero2 = int(input('Digite a porcentagem:'))
    final = (numero2 / 100) * numero1
    resultado = print('O resultado foi', final)

resultado = ''