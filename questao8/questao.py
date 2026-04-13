numeros = []
palavras = []

while True:
    pedido = input("Digite um número ou palavras ou x para sair: ")
    if pedido == 'x':
      break
    elif pedido.isnumeric():
       numeros.append(int(pedido))
    else:
       palavras.append(pedido)

tudo = len(numeros) + len(palavras)

print(f"Palavras digitadas: {palavras}")
print(f"Números digitados: {numeros}")
print(f"A quantidade total: {tudo}")