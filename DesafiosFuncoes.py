#DESAFIO 4
def by_two():

    """
    sem parâmetros obrigatórios
    recebe uma entrada do usuário e divide por dois
    o valor é retornado e guardado na variável x
    na segunda função n recebe o valor contido em x
    em seguida, multiplica por quatro
    """
    
    try:
        n = int(input("Insira um número: "))
        if n <= 0:
            raise ZeroDivisionError
        resultado = n / 2
        print(f"{n} / 2 = {n/2}")
        return resultado
    except ZeroDivisionError:
        print("Insira um valor maior que 0")
        return None
    except ValueError:
        print("Erro: insira apenas números inteiros.")
        return None

def by_four(n):
    try:
        if n is None:
            return
        if n <= 0:
            raise ZeroDivisionError
        resultado = n * 4
        print(f"{n} * 4 = {resultado}")
        return resultado
    except ValueError:
        print("Erro: insira apenas números inteiros.")

x = by_two()
by_four(x)

# DESAFIO 5

"""
Recebe o número em formato de String
substitui possíveis ',' por '.'
na sequência, converte em float
"""

def stri_to_floa(numero_String):
    try:
        numero_String = numero_String.replace(",",".")
        print(float(numero_String))
    except ValueError:
        print("Erro: Não é uma entrada válida")

stri_to_floa("954,3")
