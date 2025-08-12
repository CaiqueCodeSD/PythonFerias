# Peça um número ao usuário e exiba a tabuada de 1 a 10.
# Caso o número seja menor ou igual a zero, exiba uma mensagem
# de erro.

print('=== TABUADA INTELIGENTE ===')
maiorZero = True
while maiorZero:
    num = int(input("Insira um número: "))
    if num > 0:
        for i in range(11):
            print(f"{num} * {i} = {num * i}")
    else:
        print("O valor digitado deve ser maior que 0! ")
        maiorZero = False
