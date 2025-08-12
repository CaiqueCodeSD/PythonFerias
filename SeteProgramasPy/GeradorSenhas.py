# Peça ao usuário o tamanho da senha e gere uma senha 
# aleatória com letras minúsculas, maiúsculas e números.

import random
import string

print("=== GERADOR DE SENHAS ===")
comprimento = int(input("Insira o tamanho da senha: "))

caracEspeciais = (
    string.ascii_uppercase +
    string.ascii_lowercase + 
    string.digits 
    #string.punctuation
)

senhaAleatoria = "".join(random.choice(caracEspeciais) for _ in range(comprimento))

print(f"Senha: {senhaAleatoria}")
