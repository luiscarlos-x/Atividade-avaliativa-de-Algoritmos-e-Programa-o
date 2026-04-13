#b) O que acontece se colocarmos while <= 4: ? Justifique.

numeros =[0, 0, 0, 0, 0]
x = 0
while x <=4:
    numeros[x] = float(input("Digite um número qualquer: "))
    x += 1
y = 0
while y <=4:
    print(f"{numeros[y]}")
    y +=1

# O código irá repetir 5 vezes a mensagem "Digite um número qualquer: "
# e o código imprimirá os números recebidos 5 vezes. Ou seja, o código mudou os valores, mas não se alterou a lógica, uma vez que, em lista o índice é contado do 0, e nessa condição o sinal de = inclue o 4 também, diferentemente de <5 que exclui o 5. 