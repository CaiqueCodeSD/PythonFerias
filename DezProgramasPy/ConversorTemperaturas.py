#Escreva um programa que leia uma temperatura em Celsius e exiba o valor convertido para Fahrenheit e Kelvin.

print("=== Conversor de Temperatura ===")
temperatura = int(input("Insira a temperatura em Celsius: "))
print("=========")
print(f"Temperatura em F: {(temperatura * 1.8)+32}")
print(f"Temperatura em K: {(temperatura + 273)}")
