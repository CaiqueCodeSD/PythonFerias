"""
Função raiz(n) que calcula a raiz quadrada.
Se o número for negativo, dispare uma exceção com mensagem: 
"Não é possível calcular raiz de número negativo".
"""

import math

def raiz(n):
    try:
        if n < 0:
            raise ValueError("Não é possível calcular raiz de um número negativo")
        
        valor = math.sqrt(n)
        print(f"A raiz de {n} é -> {valor:.2f}")
        return valor
    
    except ValueError as e:
        print(f"Erro: {e}")
        return None
    
raiz(365)
