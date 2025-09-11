'''
Criar uma classe Carro com atributos (marca, modelo, ano) e métodos (acelerar, frear).

Criar uma classe Livro com atributos (titulo, autor) e método descricao().

Criar uma classe Funcionário com subclasses Gerente e Desenvolvedor.
'''

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("Randamdam randamdam...")

    def frear(self):
        print("Reduzindo a velocidade...")



class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self, descricao):
        return f"O livro \"{self.titulo}\" fala sobre: {descricao}"
    
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def exibir_informacoes(self):
        return f"Nome: {self.nome} - Salário: R${self.salario:.2f}"
    


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def exibir_informacoes(self):
        return super().exibir_informacoes() + f" - Cargo: Gerente"
    
class Desenvolvedor(Funcionario):
    def __init__(self, nome, salario, linguagem):
        super().__init__(nome, salario)
        self.linguagem = linguagem

    def exibir_informacoes(self):
        return super().exibir_informacoes() + f" - Cargo: Dev - Linguagem: {self.linguagem}"


#book = Livro("Hobbit", "Tolkien")
#print(book.descricao("Tesouros"))

funcionario01 = Gerente("Chico", 2500)
funcionario02 = Desenvolvedor("Wilson", 7200, "Python")

print(funcionario01.exibir_informacoes())
print(funcionario02.exibir_informacoes())
