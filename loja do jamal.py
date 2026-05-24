# aqui temos um codigo representando uma loja, de uma forma orientada a objetos.
class loja:
# abaixo temos uma função para reconhecer cada parâmetro dela mesma.
    def __init__(self, nome, funcionarios, produtos, clientes, chefe):
       self.nome = nome
       self.funcionarios = funcionarios
       self.produtos = produtos
       self.clientes = clientes
       self.chefe = chefe
# abaixo temos uma função para cada vez que chamada somar +1 ao parâmetro NUMERICO clientes.
    def clientela(self, quantidade=1):
        self.clientes += quantidade
# aqui atribuio que loja_do_jamal é o objeto loja que tem seus parâmetros personalizados.
loja_do_jamal = loja('lojadojamal', "A, B, C, D, E, F, G", "calças, blusas", 1200, "bryanwesley" )
# temos abaixo uma serie de 'prints' para cada parâmetro.
print(loja_do_jamal)
print(loja_do_jamal.nome)
print(loja_do_jamal.funcionarios)
print(loja_do_jamal.chefe)
print(loja_do_jamal.produtos)
# também temos uma pequena cadeia de 'prints' para executar a função 'clientela'.
print(f"clientes na loja: {loja_do_jamal.clientes}")
loja_do_jamal.clientela()
print(f"clientes na loja: {loja_do_jamal.clientes}")
# aqui termina o codigo.
