# Farmácia Popular está em promoção. A cada 2 produtos iguais comprados(foque somente nos clientes sempre comprando dois produtos),
# receba 5 reais de desconto, se forem diferente mas um dos produtos for o código 0054 ele tem 50% de desconto nesse produto, se não 
# valor não recebe descontoEscreva um programa para auxiliar a farmácia a calcular o valor final do produto.salvar códigos que entram pelo
# input em uma variável Fazer a logica da condiçãofazer ação de calcular desconto.retornar valor total

preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0 

primeiro_produto = int(input())
segundo_produto = int(input())

# Transformando o valor das variáves de float para int
if primeiro_produto == 54:
    primeiro_produto = preco_codigo_0054
elif primeiro_produto == 53:
    primeiro_produto = preco_codigo_0053
else:
    primeiro_produto = preco_codigo_0045

if segundo_produto == 54:
    segundo_produto = preco_codigo_0054
elif segundo_produto == 53:
    segundo_produto = preco_codigo_0053
else:
    primeiro_produto = preco_codigo_0045

# Lógica para o desconto
if primeiro_produto == segundo_produto:
    # Recebe 5 reais de desconto comprando 2 produtos iguais
    print((primeiro_produto + segundo_produto) - 5)
    # Diferente mas código 0054 ele tem 50% de desconto nesse produto
elif primeiro_produto == preco_codigo_0054 or segundo_produto == preco_codigo_0054:
    if preco_codigo_0054 == preco_codigo_0054:
        print((primeiro_produto/2) + segundo_produto)
    else:
        print((preco_codigo_0054/2) + primeiro_produto)
else:
    print(primeiro_produto + segundo_produto)






