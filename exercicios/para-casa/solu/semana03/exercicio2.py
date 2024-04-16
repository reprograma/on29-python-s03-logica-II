
# dois produtos iguais = 5 reais de desconto
# produtos com o código 0054 tem 50% de desconto

def comprar():
    codigo = "0054" 
    cod_produto = input("Digite o código do primeiro produto:")
    cod_produto2 = input("Digite o código do segundo produto:")
    valor1 = float(input("Digite o valor do primeiro produto:"))
    valor2 = float(input("Digite o valor do segundo produto:"))
    valor_total = valor1 + valor2

    if cod_produto == cod_produto2 and cod_produto != codigo:
        valor_total_desconto = valor_total - 5
        print(f"Na compra de dois produtos receba 5 reais de desconto. O valor total com desconto é de {valor_total_desconto:.2f}")
        return valor_total_desconto
    elif cod_produto == cod_produto2 and cod_produto == codigo:
        valor_total_desconto2 = (valor1 * 0.5) + (valor2 * 0.5) - 5
        print(f"Produtos com o código 0054 têm 50% de desconto, levando dois e ganhando o desconto de 5 reais, o valor total é de {valor_total_desconto2:.2f}")
        return valor_total_desconto2
    elif cod_produto == codigo or cod_produto2 == codigo:
        valor_total_produto1 = valor1
        valor_total_produto2 = valor2

        if cod_produto == codigo:
            valor_total_produto1 *= 0.5 
        if cod_produto2 == codigo:
            valor_total_produto2 *= 0.5 

        valor_total_codigo = valor_total_produto1 + valor_total_produto2
        print(f"Desconto de 50% aplicado a um dos produtos. O valor total com desconto é de {valor_total_codigo:.2f}")
        return valor_total_codigo

    else:
        print("Produtos sem desconto", valor_total)
        return valor_total

comprar()