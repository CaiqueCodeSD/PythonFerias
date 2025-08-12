# Leia 4 números e ao final exiba:
# Quantos são pares
# Quantos são ímpares
# A soma dos pares e a soma dos ímpares

par = 0
impar = 0
somaPar = 0
somaImpar = 0

print("=== SOMAR PARES E ÍMPARES ===")

for i in range(1,5):
    num = int(input(f"Insira o {i}º número: "))

    if num % 2 == 0:
        par += 1
        somaPar += num
    else:
        impar += 1
        somaImpar += num

print(f"\nPares: {par}")
print(f"Soma dos Pares: {somaPar}")
print(f"Ímpares: {impar}")
print(f"Soma dos Ímpares: {somaImpar}")
