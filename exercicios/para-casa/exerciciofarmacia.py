# farmacia
def calcular_desconto(cod1, cod2):
    # Se os códigos forem iguais, aplica o desconto de 5 reais
    if cod1 == cod2:
        return 5
    # Se um dos produtos for o código 0054, aplica 50% de desconto
    elif cod1 == "0054" or cod2 == "0054":
        return 0.5
    else:
        return 0  # Sem desconto

def calcular_valor_final(preco1, preco2, desconto):
    valor_total = preco1 + preco2
    if desconto:
        valor_final = valor_total - desconto
    else:
        valor_final = valor_total
    return valor_final

def main():
    try:
        cod1 = input("Digite o código do primeiro produto: ")
        preco1 = float(input("Digite o preço do primeiro produto: R$ "))
        cod2 = input("Digite o código do segundo produto: ")
        preco2 = float(input("Digite o preço do segundo produto: R$ "))

        desconto = calcular_desconto(cod1, cod2)
        valor_final = calcular_valor_final(preco1, preco2, desconto)

        print(f"Valor final do produto: R$ {valor_final:.2f}")
    except ValueError:
        print("Por favor, insira um valor numérico para o preço.")

main()