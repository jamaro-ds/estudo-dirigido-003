from poo import *

# ============================================================
# Dados pré-carregados
# ============================================================

produtos = [
    Produto("Mouse Gamer", 10, 59.90),
    Produto("Teclado Mecanico", 5, 199.90),
    Produto("Headset Pro", 7, 149.90)
]

usuarios = [
    Usuario("Ana Silva", "ana@mail.com", "1234"),
    Usuario("Carlos Souza", "carlos@mail.com", "abcd")
]

pedidos = []
jogadores = []
funcionarios = []
biblioteca = Biblioteca()


# ============================================================
# Menus do Sistema
# ============================================================

def menu_produtos():
    while True:
        print("\n=== PRODUTOS ===")
        print("1 - Cadastrar produto")
        print("2 - Listar produtos")
        print("3 - Atualizar estoque")
        print("0 - Voltar")
        op = input("> ")

        if op == "1":
            nome = input("Nome: ")
            qtd = ler_int("Quantidade: ")
            preco = ler_float("Preço: ")
            produtos.append(Produto(nome, qtd, preco))
            print("Produto cadastrado.")

        elif op == "2":
            for p in produtos:
                print(f"{p.nome} - Qtd: {p.quantidade} - R${p.preco}")

        elif op == "3":
            nome = input("Produto: ")
            for p in produtos:
                if p.nome == nome:
                    qtd = ler_int("Quantidade (+/-): ")
                    if qtd > 0:
                        p.adicionar(qtd)
                    else:
                        p.remover(abs(qtd))
                    break
            else:
                print("Produto não encontrado.")

        elif op == "0":
            break


def menu_usuarios():
    while True:
        print("\n=== USUARIOS ===")
        print("1 - Criar usuario")
        print("2 - Login")
        print("0 - Voltar")
        op = input("> ")

        if op == "1":
            nome = input("Nome: ")
            email = input("Email: ")
            senha = input("Senha: ")
            usuarios.append(Usuario(nome, email, senha))
            print("Usuario criado.")

        elif op == "2":
            email = input("Email: ")
            senha = input("Senha: ")

            for u in usuarios:
                if u.autenticar(email, senha):
                    print("Login realizado.")
                    break
            else:
                print("Dados incorretos.")

        elif op == "0":
            break


def menu_pedidos():
    pedido = Pedido()

    while True:
        print("\n=== PEDIDOS ===")
        print("1 - Adicionar item")
        print("2 - Listar itens")
        print("3 - Total")
        print("0 - Voltar")
        op = input("> ")

        if op == "1":
            nome = input("Item: ")
            preco = ler_float("Preço: ")
            pedido.adicionar_item(Item(nome, preco))

        elif op == "2":
            pedido.listar()

        elif op == "3":
            print("Total do pedido:", pedido.total())

        elif op == "0":
            break


def menu_jogadores():
    nome = input("Nome do jogador: ")
    j = Jogador(nome)
    jogadores.append(j)

    while True:
        print("\n=== JOGADOR ===")
        print("1 - Adicionar saldo")
        print("2 - Comprar item")
        print("3 - Ver dados")
        print("0 - Voltar")
        op = input("> ")

        if op == "1":
            j.adicionar_saldo(ler_float("Valor: "))

        elif op == "2":
            item = input("Item: ")
            preco = ler_float("Preço: ")
            j.comprar(item, preco)

        elif op == "3":
            print(j.nome, "| Saldo:", j.saldo, "| Itens:", j.inventario)

        elif op == "0":
            break


def menu_biblioteca():
    while True:
        print("\n=== BIBLIOTECA ===")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Listar disponíveis")
        print("0 - Voltar")
        op = input("> ")

        if op == "1":
            t = input("Título: ")
            a = input("Autor: ")
            biblioteca.adicionar(Livro(t, a))

        elif op == "2":
            t = input("Título: ")
            if biblioteca.emprestar(t):
                print("Livro emprestado.")
            else:
                print("Livro indisponível.")

        elif op == "3":
            biblioteca.listar_disponiveis()

        elif op == "0":
            break


def menu_funcionarios():
    while True:
        print("\n=== FUNCIONARIOS ===")
        print("1 - Cadastrar")
        print("2 - Listar")
        print("3 - Aumentar salário")
        print("0 - Voltar")
        op = input("> ")

        if op == "1":
            n = input("Nome: ")
            c = input("Cargo: ")
            s = ler_float("Salário: ")
            funcionarios.append(Funcionario(n, c, s))

        elif op == "2":
            for f in funcionarios:
                print(f"{f.nome} - {f.cargo} - R${f.salario:.2f}")

        elif op == "3":
            nome = input("Nome: ")
            for f in funcionarios:
                if f.nome == nome:
                    f.aumentar(ler_float("Percentual: "))
                    break
            else:
                print("Funcionario não encontrado.")

        elif op == "0":
            break


# ============================================================
# Menu principal
# ============================================================

def main():
    while True:
        print("\n===== SISTEMA =====")
        print("1 - Produtos")
        print("2 - Usuarios")
        print("3 - Pedidos")
        print("4 - Jogadores")
        print("5 - Biblioteca")
        print("6 - Funcionarios")
        print("0 - Sair")

        op = input("> ")

        if op == "1":
            menu_produtos()
        elif op == "2":
            menu_usuarios()
        elif op == "3":
            menu_pedidos()
        elif op == "4":
            menu_jogadores()
        elif op == "5":
            menu_biblioteca()
        elif op == "6":
            menu_funcionarios()
        elif op == "0":
            print("Encerrando sistema.")
            break


if __name__ == "__main__":
    main()
