preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0


primeiro_produto = int(input("Digite o primeiro produto: "))
segundo_produto = int(input("Digite o segundo produto: "))

# desenvolva a logica condicional

# como identificar o valor do cod com o preço
# vinculando ao primeiro produto
if primeiro_produto == 54:
    primeiro_produto = preco_codigo_0054
elif primeiro_produto == 53:
    primeiro_produto = preco_codigo_0053
else:
    primeiro_produto = preco_codigo_0045
# vinculando ao segundo produto.
if segundo_produto == 54:
    segundo_produto = preco_codigo_0054
elif segundo_produto == 53:
    segundo_produto = preco_codigo_0053
else:
    segundo_produto = preco_codigo_0045

# logica para desconto

# a compra foi feita com dois produtos iguais e recebe R$5,00 de desconto.
if primeiro_produto == segundo_produto:
    print((primeiro_produto + segundo_produto) - 5)
# verificando se um dos produtos é o produto código 0054
elif primeiro_produto == preco_codigo_0054 or segundo_produto == preco_codigo_0054:
    # desconto refernte a 50% do produto código 0054
    if preco_codigo_0054 == preco_codigo_0054:
        print(primeiro_produto / 2 + segundo_produto)
    else:
        print(segundo_produto / 2 + primeiro_produto)
# nenhum desconto aplicado:
else:
    print(primeiro_produto + segundo_produto)
