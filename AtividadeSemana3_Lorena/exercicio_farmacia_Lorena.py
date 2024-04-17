#Questão 2 - Desconto Farmácia - Aluna: Lorena Vieira

preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0

print("\nSeja bem-vinde à farmácia Joinha!")

primeiro_produto = input("\nInsira o código do produto 1: ")
segundo_produto = input("Insira o código do produto 2: ")

#Determinando os valores em função do input do cliente

#Primeiro produto
if primeiro_produto == "0054":
    preco_primeiro_produto = preco_codigo_0054
elif primeiro_produto == "0053":
    preco_primeiro_produto = preco_codigo_0053
elif primeiro_produto == "0045":
    preco_primeiro_produto = preco_codigo_0045

#Segundo produto
if segundo_produto == "0054":
    preco_segundo_produto = preco_codigo_0054
elif segundo_produto == "0053":
    preco_segundo_produto = preco_codigo_0053
elif segundo_produto == "0045":
    preco_segundo_produto = preco_codigo_0045

#Calculando o valor total da compra de acordo com os descontos da promoção
if primeiro_produto == segundo_produto:
    valor_total = preco_primeiro_produto + preco_segundo_produto - 5
    print ("\nOba! Você obteve um desconto de R$5,00 no valor total da sua compra!")
elif primeiro_produto == "0054" or segundo_produto == "0054":
    if primeiro_produto == "0054":
        preco_primeiro_produto = preco_primeiro_produto * 0.5
        valor_total = preco_primeiro_produto + preco_segundo_produto
        print ("\nOba! Você obteve um desconto de 50% no valor produto de código 0054!")
    else: 
        preco_segundo_produto = preco_segundo_produto * 0.5
        valor_total = preco_primeiro_produto + preco_segundo_produto
        print ("\nOba! Você obteve um desconto de 50% no produto de código 0054!")
else: 
    valor_total = preco_primeiro_produto + preco_segundo_produto
    print ("\nInfelizmente você não teve desconto nessa compra ):")

texto_valor_total = f"R${valor_total:_.2f}"
texto_valor_total = texto_valor_total.replace(".", ",").replace("_", ".")

print(f"\nO valor total é de: {texto_valor_total}.")
print("\nObrigada e espero que não precise voltar sempre rs")
