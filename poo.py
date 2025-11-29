# ============================================================
# Funções auxiliares
# ============================================================

def ler_float(msg):
    return float(input(msg).replace(",", "."))

def ler_int(msg):
    return int(input(msg))


# ============================================================
# Produtos e Estoque
# ============================================================

class Produto:
    def __init__(self, nome, quantidade, preco):
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def adicionar(self, qtd):
        self.quantidade += qtd

    def remover(self, qtd):
        if self.quantidade >= qtd:
            self.quantidade -= qtd
        else:
            print("Estoque insuficiente.")

    def valor_total(self):
        return self.quantidade * self.preco


# ============================================================
# Usuários
# ============================================================

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def autenticar(self, email, senha):
        return self.email == email and self.senha == senha


# ============================================================
# Pedidos
# ============================================================

class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def listar(self):
        for i in self.itens:
            print(f"{i.nome} - R${i.preco}")

    def total(self):
        return sum(i.preco for i in self.itens)


# ============================================================
# Sistema de Jogo
# ============================================================

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.saldo = 0
        self.inventario = []

    def adicionar_saldo(self, valor):
        self.saldo += valor

    def comprar(self, item, preco):
        if self.saldo >= preco:
            self.saldo -= preco
            self.inventario.append(item)
        else:
            print("Saldo insuficiente.")


# ============================================================
# Pagamentos
# ============================================================

class Pagamento:
    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor
        self.status = "PENDENTE"

    def processar(self):
        self.usuario.saldo += self.valor
        self.status = "CONCLUIDO"


# ============================================================
# Biblioteca
# ============================================================

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True


class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def emprestar(self, titulo):
        for l in self.livros:
            if l.titulo == titulo and l.disponivel:
                l.disponivel = False
                return True
        return False

    def listar_disponiveis(self):
        for l in self.livros:
            if l.disponivel:
                print(f"{l.titulo} - {l.autor}")


# ============================================================
# Funcionários
# ============================================================

class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar(self, percentual):
        self.salario *= (1 + percentual / 100)
