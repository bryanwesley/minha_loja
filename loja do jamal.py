class loja:
    def __init__(self, nome, funcionarios, chefe):
       self.nome = nome
       self.funcionarios = funcionarios
       self.chefe = chefe
loja_do_jamal = loja('lojadojamal', "A, B, C, D, E, F, G","bryanwsley" )
print(loja_do_jamal)
print(loja_do_jamal.nome)
print(loja_do_jamal.funcionarios)
print(loja_do_jamal.chefe)

