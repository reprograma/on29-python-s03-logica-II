#EXERCICIO 2

#DESCONTO FARMACIA

 


print('-' * 60)
print('FARMACIA DA BLANCA')
print('-' * 60)
print('produtos disponiveis e seu código')
print('-' * 60)

print('0054 - Creme hidratante')
print('0053 - Shampoo')
print('0052 - Dramin')


preco_0054 = int(10)
preco_0053 = int(8)
preco_0052 = int(3)

compra1 = int(input('insira o código do primeiro produto que irá comprar: '))
compra2 = int(input('insira o código do segundo produto que irá comprar: '))

#Definições de preço
if compra1 == 54:
    compra1 == preco_0054
elif compra1 == 53:
    compra1 == preco_0053
else:
    compra1 == preco_0052

if compra2 == 54:
    compra2 == preco_0054
elif compra2 == 53:
    compra2 == preco_0053
else:
    compra2 == preco_0052


#Desconto dois produtos iguais

if compra1 == compra2:
    print((compra1 + compra2) -5)



#observação: atividade está sendo entregue de forma imcompleta, não obtive sucesso na criação do código total a tempo. 