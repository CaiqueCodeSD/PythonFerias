class Tarefa:
    def __init__(self, id, descricao):
        self.id = id
        self.descricao = descricao
        self.concluida = False

    def __str__(self):
        status = "OK" if self.concluida else "X"
        return f"ID: {self.id} | {self.descricao} | Concluída: {status}"
    
tarefas = []
proximo_id = 1

def criar_tarefa():
    global proximo_id
    descricao = input("O que você irá fazer nessa tarefa? ")
    tarefa = Tarefa(proximo_id, descricao)
    tarefas.append(tarefa)
    proximo_id += 1
    print("Tarefa adicionada!")

def listar_tarefas():
    if not tarefas:
        print("\nNenhuma tarefa registrada")
        return
    print("\n===== LISTA DE TAREFAS =====")
    for t in tarefas:
        print(t)


def atualizar_tarefa():
    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja atualizar: "))
        for t in tarefas:
            if t.id == id_tarefa:
                nova_desc = input("Nova descrição: ")
                t.descricao = nova_desc
                concluida = input("Marcar como concluída? (s/n): ").lower()
                t.concluida = concluida == "s"
                print("Tarefa atualizada!")
                return
        print("Tarefa não encontrada")
    except ValueError:
        print("ID inválido!")


def remover_tarefa():
    try:
        id_tarefa = int(input("Digite o ID da tarefa que deseja remover: "))
        global tarefas
        tarefas = [t for t in tarefas if t.id != id_tarefa]
        print("Tarefa removida")
    except ValueError:
        print("ID inválido!")


def menu():
    while True:
        print("\n===== MENU =====")
        print("1. Criar tarefa")
        print("2. Listar tarefas")
        print("3. Atualizar tarefa")
        print("4. Remover tarefa")
        print("0. Sair")
        opcao = input("Escolha: ")

        if opcao == "1":
            criar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            atualizar_tarefa()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    menu()