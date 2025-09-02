menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def deposito():
    global saldo
    global extrato
    dep = float(input("Insira o valor para ser depositado: "))
    if dep > 0:
        saldo += dep
        extrato += f"Depósito: R$ {dep:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def sacar():
    global saldo
    global extrato
    global numero_saques
    saq = float(input("Informe o valor de saque: "))

    excedeu_saldo = saq > saldo
    excedeu_limite = saq > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques diários excedido.")
    elif saq > 0:
        saldo -= saq
        extrato += f"Saque: R$ {saq:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")

def exibir_extrato():
    global saldo
    global extrato
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)
    if opcao == "d":
        deposito()
    elif opcao == "s":
        sacar()
    elif opcao == "e":
        exibir_extrato()
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
