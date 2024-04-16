preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0


primeiro_produto = int(input("COLOQUE O VALOR PARA O PRIMEIRO PRODUTO:"))
segundo_produto = int(input("COLOQUE O VALOR PARA O SEGUNDO PRODUTO:"))

# desenvolva a logica condicional

#como identificar o valor do codigo com o preço

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
    segundo_produto = preco_codigo_0045

#logica para desconto

if primeiro_produto == segundo_produto:
    print((primeiro_produto + segundo_produto)- 5 )
elif primeiro_produto == preco_codigo_0054 or segundo_produto == preco_codigo_0054:
    if primeiro_produto == preco_codigo_0054:
        print ((preco_codigo_0054/3) + segundo_produto)
    else:
        print((preco_codigo_0054/2) + primeiro_produto)
else:
    print(primeiro_produto + segundo_produto)