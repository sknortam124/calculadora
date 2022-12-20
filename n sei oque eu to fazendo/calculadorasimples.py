"calculadorasimples"

"numeros"

numero1 = 0
numero2 = 0
resultado = 0
operacao = ''

"resolução"

numero1 = int(input('Digite o numero: '))
operacao = input('Digite a operação: ')
numero2 = int(input('Digite o numero: '))

if operacao == '+':
    resultado = numero1 + numero2
elif operacao == '-':
    resultado = numero1 - numero2
elif operacao == '/':
    resultado = numero1 / numero2
elif operacao == '*':
    resultado = numero1 * numero2
else: 
    resultado = 'operação inválida'

print(str(numero1) + '' + str(operacao) + '' + str(numero2) + ' = ' + str(resultado))