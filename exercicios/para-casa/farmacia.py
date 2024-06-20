preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0


# desenvolva a logica condicional

# Definir preços dos produtos

precos = {
    54: 10.4,  # Código 0054
    53: 4.6,   # Código 0053
    45: 50.0   # Código 0045
}

# Obter códigos dos produtos 

primeiro_produto = int(input("Digite o código do primeiro produto: "))
segundo_produto = int(input("Digite o código do segundo produto: "))

# Inicializar variáveis para os preços dos produtos

preco1 = precos.get(primeiro_produto, 0)
preco2 = precos.get(segundo_produto, 0)

# Inicializar desconto

desconto = 0

# Calcular desconto

if primeiro_produto == segundo_produto:
    # Desconto de 5 reais para dois produtos iguais
    desconto = 5.0
elif primeiro_produto == 54 or segundo_produto == 54:
    # Desconto de 50% no produto com código 0054
    desconto = min(preco1, preco2) * 0.50

# Calcular valor total com desconto
valor_total = (preco1 + preco2) - desconto

# Exibir valor total
print(f"Valor total a pagar: R$ {valor_total:.2f}")
