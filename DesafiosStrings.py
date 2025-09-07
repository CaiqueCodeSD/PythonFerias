# 01 exibir cada caractere de "Camus"
palavra = "Camus"

for i in palavra:
    print(i)

# 02 coletar duas strings, inserir em uma existente e exibir em uma nova
resposta_um = str(input("Insira a string 1: "))
resposta_dois = str(input("Insira a string 2: "))

st_01 = f"Yesterday I wrote a {resposta_um}."
st_02 = f" I sent it to {resposta_dois}!"
st_nova = st_01 + st_02

# 03 capitalizar string
def capitalizar():
    frase = "aldous Huxley was born in 1894"
    return frase.capitalize()

# 04 pegar uma String  e retornar separada em uma lista
def strLista():
    texto = "Where now? Who now? When now?"
    lista = texto.split("?")
    lista = [p.strip() + "?" for p in lista if p.strip()]
    return lista

# 05 pegarr uma lista e transformar em uma string
def listaStr():
    lista = ["The",
             "fox",
             "jumped",
             "over",
             "the",
             "fence",
             "."]
    texto = " ".join(lista)
    texto = texto.replace(" .",".")
    return texto

# 06 trocar s por $
def trocar_s():
    texto = "A screaming comes across the sky".lower()
    texto = texto.replace("s","$").capitalize()
    return texto

# 07 encontrar primeiro índice de um caractere fornecido na função em uma string fornecida
def indice_palavra(caractere, palavra):
    if caractere in palavra:
        print(f"Caractere \"{caractere}\" no índice {palavra.index(caractere)}")
    else:
        print(f"Caractere \"{caractere}\" não está presente na String \"{palavra}\"")

# 08 citação de livro com aspas
def aspas():
    print(
        "\"Há dois tipos de injustiça: a primeira se encontra naqueles "
        "que prejudicam os outros, a segunda, naqueles que falham em proteger "
        "outra pessoa do prejuízo quando podem.\""
    )
# 09 concatenar e multiplicar String
def concatenar_e_multiplicar(palavra):
    print(f"Concatenação: {palavra + palavra + palavra}")
    print(f"Multiplicação: {palavra * 3}")

# 10 fatiar string para que só inclua os caracteres existentes antes da vírgula
def antes_virgula():
    frase = "It was a bright cold day in April, and the clocks were striking thirteen."
    frase = frase.split(",")[0]
    return frase

print(st_nova)
print(capitalizar())
print(strLista())
print(listaStr())
print(trocar_s())
indice_palavra('x',"Men Evolution")
aspas()
concatenar_e_multiplicar("three")
print(antes_virgula())
