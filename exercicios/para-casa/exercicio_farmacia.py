#preco_codigo_0054 = 10.4
#preco_codigo_0053 = 4.6
#preco_codigo_0045 = 50.0

primeiro_produto = float(input("insira o valor do primeiro produto: "))
segundo_produto = float(input("Insira o valor do segundo produto: "))


if primeiro_produto == segundo_produto:
    print("Valor a ser pago: ",primeiro_produto + segundo_produto - 5)
elif primeiro_produto == 10.4:
    print("Valor a ser pago: ",(primeiro_produto/2) + segundo_produto)
elif segundo_produto == 10.4:
    print("Valor a ser pago: ",primeiro_produto + (segundo_produto/2))
else:
    print("Valor a ser pago: ",primeiro_produto + segundo_produto)

