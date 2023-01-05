entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

triangulo = a * c / 2
circulo = 3.14159 * c * c
trapezio = 1 / 2 * c * (a + b)
quadrado = b**2
retangulo = a * b

print('TRIANGULO = %0.3lf' %triangulo)
print('CIRCULO = %0.3lf' %circulo)
print('TRAPEZIO = %0.3lf' %trapezio)
print('QUADRADO = %0.3lf' %quadrado)
print('RETANGULO = %0.3lf' %retangulo)
