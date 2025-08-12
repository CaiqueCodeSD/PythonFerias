# Escreva um programa que conte quantas vogais existem em 
# uma frase digitada pelo usuário.

from collections import Counter

print("=== CONTADOR DE VOGAIS ===")
texto = input("Digite qualquer palavra: ").upper()

contar = Counter(texto)

vogais = "AEIOU"
total = sum(contar[i] for i in vogais)

print(f"Quantidade de vogais: {total}")
for i in vogais:
    print(f"{i}: {contar[i]}")
