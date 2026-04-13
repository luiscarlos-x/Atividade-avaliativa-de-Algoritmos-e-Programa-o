#questão 1. 
# a) Refaça o código utilizando a estrutura FOR 

numeros = [0, 0, 0, 0, 0]

for x in range (5):
    numeros[x] = float(input("Digite um número qualquer: "))
    x += 1
for y in range (5):
 print(f"{numeros[y]}")
y +=1