# Leia o nome de um aluno e suas três notas. 
# Calcule e exiba a média, informando se ele está aprovado (média ≥ 7) ou reprovado.
# Extra: formatar a média com duas casas decimais.

print("=== CALCULADORA DE MÉDIA ===")
estudante = input("Nome do estudante: ")
n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))

media = (n1+n2+n3)/3

if media >= 7:
    aprovado = True
else:
    aprovado = False

print(f"{estudante.upper()} - {'Média: '} {media:.2f} - {'Aprovado: '} {aprovado}")
