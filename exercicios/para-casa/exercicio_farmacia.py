preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0

# PEDIR OS DADOS PARA O CLIENTE
primeiro_produto = int(input("INSIRA O CODIGO DO PRIMEIRO PRODUTO"))
segundo_produto = int(input("INSIRA O CODIGO DO SEGUNDO PRODUTO"))

#TRANSFORMAR O INPUT EM UM VALOR VALIDO
if primeiro_produto == 54:
  primeiro_produto = preco_codigo_0054
elif primeiro_produto == 53:
  primeiro_produto == preco_codigo_0053
elif primeiro_produto == 45:
  primeiro_produto = preco_codigo_0045

if segundo_produto == 54:
  segundo_produto = preco_codigo_0054
elif segundo_produto == 53:
  segundo_produto == preco_codigo_0053
elif segundo_produto == 45:
  segundo_produto = preco_codigo_0045

#CALCULAR PRIMEIRO CENARIO (PRODUTOS DE PRECOS IGUAIS)
if primeiro_produto == segundo_produto:
  print("O VALOR TOTAL E : ",(primeiro_produto + segundo_produto) - 5)
#CALULCAR SEGUNDO CENARIO (PRODUTOS 0054)
elif primeiro_produto == 54 or segundo_produto == 54:
  if primeiro_produto == 54:
    print("O VALOR TOTAL E : ",(primeiro_produto/2) + segundo_produto)
  else:
    print((segundo_produto/2) + primeiro_produto)
# CALCULAR TERCEIRO CENARIO (SEM DESCONTO)
else:
  print("O VALOR TOTAL E : ",primeiro_produto + segundo_produto)

