line = str(input(""))

split = line.split()

a = int(split[0])
b = int(split[1])
c = int(split[2])

resultab = ((a + b) + abs(a - b)) / 2

resultac = ((a + c) + abs(a - c)) / 2

resultado = ((resultab + resultac) + abs(resultab - resultac)) / 2


print("%d eh o maior" % resultado)
