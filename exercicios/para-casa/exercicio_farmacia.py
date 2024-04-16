#O código não vai entrar com os 00 (código 54, 53, 45)
primeiro_produto = int(input('Código do produto 1: '))
segundo_produto = int(input('Código do produto 2: '))

#definindo valores para produto 1 e produto 2:
preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0

#Valor produto1: alterando int('0054')
if primeiro_produto == 54:
    primeiro_produto = preco_codigo_0054
    print('Valor do produto 1: R$ 10.40.')
elif primeiro_produto == 53:
    primeiro_produto = preco_codigo_0053
    print('Valor do produto 1: R$ 4.60.')
else:
    primeiro_produto = preco_codigo_0045
    print('Valor do produto 1: R$ 50.00.')

#Valor produto2: alterando int('0054')
if segundo_produto == 54:
    segundo_produto = preco_codigo_0054
    print('Valor do produto 2: R$ 10.40.')
elif segundo_produto == 53:
    segundo_produto = preco_codigo_0053
    print('Valor  do produto 2: R$ 4.60.')
else:
    segundo_produto = preco_codigo_0045
    print('Valor do produto 2: R$ 50.00.')

#compra leva desconto?: aqui eu coloquei apenas para printar se tinha desconto ou não, tinha feito uma outra parte do código com if, elif e else para calcular o desconto;
#além disso, o segundo if FICOU BEM CONFUSO
#ERRO: COLOCAR PRIMEIRO_PRODUTO == 0054 (não à variável preco_codigo_0054)
if primeiro_produto == segundo_produto:
    print((primeiro_produto + segundo_produto) - 5)
elif primeiro_produto == preco_codigo_0054 or segundo_produto == preco_codigo_0054:
    if preco_codigo_0054 == preco_codigo_0054:
        print((primeiro_produto/2) + segundo_produto)
    else:
        print((segundo_produto/2) + primeiro_produto)
else:
    print(primeiro_produto + segundo_produto)


#MINHA VERSÃO DE RESOLUÇÃO, QUE DAVA ERRO NO PREÇO COM DESCONTO (aqui, o código não rodava mais :///)
#valor_final = primeiro_produto + segundo_produto
#print('O valor total da sua compra é de R$', valor_final)  

#valor com desconto:
#if primeiro_produto == segundo_produto:
#    print('Valor total da compra - com desconto: R$', (primeiro_produto + segundo_produto) - desconto)
#elif primeiro_produto == int('0054') or segundo_produto == int('0054'):
#    print('Valor total da compra - com desconto: R$', primeiro_produto + segundo_produto)
#else:
#    print('Valor total da compra - sem desconto: R$', primeiro_produto + segundo_produto)

