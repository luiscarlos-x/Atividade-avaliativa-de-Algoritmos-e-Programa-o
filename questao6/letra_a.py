L = []
while True:
    n = int(input("Digite um número ou 0 para sair: "))
    if n == 0:
        break
    L.append(n)

for elemento in L:
    print(elemento)