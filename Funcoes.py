# ✅ Funções Simples (iniciante)

# Saudação personalizada (saudacao(nome))
def cumprimento(nome):
    print(f"\nSeja bem vindo(a), {nome}!")

# Dobro de um número (dobro(n))
def dobrar(num):
    print(f"2 * {num} = {2 * num}")

# Verificar se um número é par (eh_par(n))
def verificar_par(valor):
    if (valor % 2 == 0):
        print(f"{valor} é par")
    else:
        print(f"{valor} é ímpar")

# 🔄 Funções com listas e strings (intermediário)

# Somar todos os números de uma lista (soma_lista(lista))
def somar_lista(numeros):
    print(sum(numeros))

# Contar vogais em uma palavra (contar_vogais(palavra))
def contar_vogais(palavra):
    palavra = palavra.upper()
    print(sum(palavra.count(vogais) for vogais in "AEIOU"))

# Inverter uma string (inverter_string(texto))
def inverter_palavra(texto):
    print(texto[::-1])

# 🧠 Funções com lógica mais elaborada (avançado)

# Verificar se uma palavra é palíndromo (eh_palindromo(palavra))
def palindromo(palavra_palindromo):
    palavra_palindromo = palavra_palindromo.upper()
    palindromo_teste = palavra_palindromo[::-1]

    if palavra_palindromo == palindromo_teste:
        print(f"A palavra {palavra_palindromo} é um palíndromo")
    else:
        print(f"A palavra {palavra_palindromo} não é um palíndromo")

# Calcular fatorial de um número com recursão (fatorial(n))
def fatorial(n):
    import math
    print(math.factorial(n))

# Gerar senha aleatória (gerar_senha(tamanho=8))
def gerar_senha(tamanho):
    import random
    import string

    senha = "".join(random.choice(string.ascii_letters) for _ in range(tamanho))
    print(senha)

cumprimento("Abigail")
dobrar(93)
verificar_par(5)
somar_lista([10,29,38,47,56])
contar_vogais("Wayne")
inverter_palavra("Hobbit")
palindromo("jornada")
fatorial(7)
gerar_senha(8)
