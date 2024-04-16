preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0


primeiro_produto = int(input())
segundo_produto = int(input())

# desenvolva a logica condicional

if primeiro_produto == segundo_produto:
    if primeiro_produto == 54:
        valor_compra = 2*preco_codigo_0054 - 5
    elif primeiro_produto == 53:
        valor_compra = 2*preco_codigo_0053 - 5
    elif primeiro_produto == 45:
        valor_compra = 2*preco_codigo_0045 - 5

elif primeiro_produto == 54:
    if segundo_produto == 53:
        valor_compra = preco_codigo_0053 + (preco_codigo_0054*0.5)
    elif segundo_produto == 45:
        valor_compra = preco_codigo_0045 + (preco_codigo_0054*0.5)

elif segundo_produto == 54:
    if primeiro_produto == 53:
        valor_compra = preco_codigo_0053 + (preco_codigo_0054*0.5)
    elif primeiro_produto == 45:
        valor_compra = preco_codigo_0045 + (preco_codigo_0054*0.5)

else:
    valor_compra = preco_codigo_0053 + preco_codigo_0045

print(f"O valor final da compra é de R${valor_compra:.2f}!")