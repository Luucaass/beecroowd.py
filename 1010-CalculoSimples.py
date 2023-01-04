entry = input().split()
cod1 = int(entry[0])
num1 = int(entry[1])
valor1 = float(entry[2])

entry = input().split()
cod2 = int(entry[0])
num2 = int(entry[1])
valor2 = float(entry[2])

pag = (num1 * valor1) + (num2 * valor2)

print('VALOR A PAGAR: R$ %0.2lf' %pag)
