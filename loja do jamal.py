class loja:
    def __init__(self, nome, funcionarios, produtos, clientes, chefe):
       self.nome = nome
       self.funcionarios = funcionarios
       self.produtos = produtos
       self.clientes = clientes
       self.chefe = chefe
loja_do_jamal = loja('lojadojamal', "A, B, C, D, E, F, G", "calças, blusas", 1200, "bryanwesley" )
print(loja_do_jamal)
print(loja_do_jamal.nome)
print(loja_do_jamal.funcionarios)
print(loja_do_jamal.chefe)
print(loja_do_jamal.produtos)
print(loja_do_jamal.clientes)