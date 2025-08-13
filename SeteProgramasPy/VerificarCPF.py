# Leia um CPF no formato xxx.xxx.xxx-xx e verifique se está 
# no padrão correto (não precisa validar dígitos, só o formato).
# Extra: usar expressões regulares para a validação.
# Conceitos envolvidos: re (regex), validação de strings.

import re

print("=== VERIFICAR CPF ===")
print("000.000.000-00")
cpf = input("Insira o CPF respeitando o padrão: ")

estruturaCPF = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"
# ^ → início da string
# \d{3} → exatamente 3 dígitos
# \. → ponto literal (precisa de barra invertida para escapar)
# - → hífen literal
# $ → final da string

if re.match(estruturaCPF, cpf):
    print("O CPF está correto!")
else:
    print("O CPF não está de acordo com o padrão")
