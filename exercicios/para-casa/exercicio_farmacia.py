# Criando uma lista de Produtos Promocionais 
codigo_0054 = "Shampoo"
codigo_0053 = "Sabonete"
codigo_0045 = "Creme de Tratamento"

# Armazenando o valor de cada item
preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0

# Apresentando produtos promocionais e perguntando quais produtos deseja comprar
print(f"Produtos em promoção:\nCódigo 54 - {codigo_0054}\nCódigo 53 - {codigo_0053}\nCódigo 45 - {codigo_0045}")
primeiro_produto = float(input("Digite o código do primeiro produto: "))
segundo_produto = float(input("Digite o código do segundo produto: "))

# desenvolva a logica condicional
# Atibuindo o valor ao produto informado 
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
    
# Lógica para desconto 
if primeiro_produto == segundo_produto:
    print(f"Você acaba de ganhar um desconto de R${5}, o valor total da sua compra é R${(primeiro_produto + segundo_produto) - 5}")
elif primeiro_produto == preco_codigo_0054 or segundo_produto == preco_codigo_0054:
    if preco_codigo_0054 == preco_codigo_0054:
        print(f"Você acaba de ganhar um desconto de 50% sobre o produto {codigo_0054} e o valor total da sua compra é R${(primeiro_produto / 2) + segundo_produto}")
    else:
        print(f"Você acaba de ganhar um desconto de 50% sobre o produto {codigo_0054} e o valor total da sua compra é R${(segundo_produto / 2) + primeiro_produto}")
        
else:
    print(f"Esses produtos não entram na promoção e o valor da sua compra é de R${primeiro_produto + segundo_produto}")


# Prof, eu estava desenvolvendo essa outra lógica aqui antes da aula de ontem, mas me embananei no último caso. Ficou muito mais complicado...
"""
# # se ps produtos são iguais 
if primeiro_produto == segundo_produto == 54:
    primeiro_produto = preco_codigo_0054
    segundo_produto = preco_codigo_0054
    print(f"O valor unitário do produto é R${preco_codigo_0054}")
    desconto = 5
    valor_final = (primeiro_produto + segundo_produto) - desconto
    print(f"Você acaba de ganhar R${desconto} de desconto por comprar duas unidades de {codigo_0054}!\nO valor total da sua compra é de R${valor_final:.2f}")
elif primeiro_produto == segundo_produto == 53:
    primeiro_produto = preco_codigo_0053
    segundo_produto = preco_codigo_0053
    print(f"O valor unitário do produto é R${preco_codigo_0053}")
    desconto = 5
    valor_final = (primeiro_produto + segundo_produto) - desconto
    print(f"Você acaba de ganhar R${desconto} de desconto por comprar duas unidades de {codigo_0053}!\nO valor total da sua compra é de R${valor_final:.2f}")
    if primeiro_produto == segundo_produto == 45:
        primeiro_produto = preco_codigo_0045
        segundo_produto = preco_codigo_0045
        print(f"O valor unitário do {codigo_0045} é R${preco_codigo_0045}")
        desconto = 5
        valor_final = (primeiro_produto + segundo_produto) - desconto
        print(f"Você acaba de ganhar R${desconto} de desconto por comprar duas unidades de {codigo_0045}!\nO valor total da sua compra é de R${valor_final}")
# se diferentes mas um dos dois o 0054
elif primeiro_produto or segundo_produto == 54:
        if primeiro_produto == 54:
            primeiro_produto = preco_codigo_0054
            if segundo_produto == 53:
                segundo_produto = preco_codigo_0053
                if segundo_produto == 45:
                    segundo_produto = preco_codigo_0045
                    desconto = primeiro_produto / 2
                    valor_final = desconto + segundo_produto
            print(desconto, valor_final)
            
        elif segundo_produto == 54:
            segundo_produto = preco_codigo_0054
            if primeiro_produto == 53:
                primeiro_produto = preco_codigo_0053
                if primeiro_produto == 45:
                    primeiro_produto = preco_codigo_0045
                    desconto = segundo_produto / 2
                    valor_final = desconto + primeiro_produto
                    print(desconto, valor_final)
# se diferentes e nenhum o 0054
else:
    primeiro_produo = # aqui eu não conseguia mais pensar 
    valor_final = primeiro_produto + segundo_produto
    print(valor_final)


"""