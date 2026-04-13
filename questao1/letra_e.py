quantidade_numeros = int(input("Digite a quantidade de números: "))

numeros = [] 

x = 0
while x < quantidade_numeros:
    numero = float(input("Digite um número qualquer: "))
    numeros.append(numero)  
    x += 1

y = 0
while y < quantidade_numeros:
    print(numeros[y])  
    y += 1