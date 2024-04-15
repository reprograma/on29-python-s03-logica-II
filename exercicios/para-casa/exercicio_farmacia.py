"""
- Explicação do exercício: 
Farmacia Popular está em promoção. A cada 2 produtos iguais comprados(foque somente nos clientes sempre comprando dois produtos), receba 5 reais de desconto, se forem diferente mas um dos produtos for o codigo 0054 ele tem 50% de desconto nesse produto, se não valor não recebe desconto.Escreva um programa para auxiliar a farmacia a calcular o valor final do produto.

1. Salvar códigos que entram pelo input em uma variável;
2. Fazer a logica da condição;
3. Fazer ação de calcular desconto;
4. Retornar valor total.
"""

# Definindo os preços dos produtos
preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0

# Solicitando os códigos dos produtos ao usuário
menu = "+-----------------------------------------------------------+"
menu += "\n+              Bem vindo a farmácia popular!                +"
menu += "\n+-----------------------------------------------------------+"
menu += "\n+ No nosso programa constam os seguintes medicamentos:      +"
menu += "\n+ Código: 54                                                +"
menu += "\n+ Código: 53                                                +"
menu += "\n+ Código: 45                                                +"
menu += "\n+-----------------------------------------------------------+"
menu += "\n+ Para comprar, insira os códigos que deseja abaixo:        +"
menu += "\n+-----------------------------------------------------------+"

print(menu)

primeiro_produto = int(input("+ Qual é o primeiro produto que deseja comprar? "))
segundo_produto = int(input("+ Qual é o segundo produto que deseja comprar? "))

# Lógica condicional

# Verificando se os produtos são iguais
if primeiro_produto == segundo_produto:
    # Se forem iguais, aplicamos o desconto de 5 reais
    if primeiro_produto == 54:
        valor_total = (preco_codigo_0054 * 2) - 5
    elif primeiro_produto == 53:
        valor_total = (preco_codigo_0053 * 2) - 5
    else:
        valor_total = (preco_codigo_0045 * 2) - 5
else:
    # Se forem diferentes, verificamos se um deles é o código 0054 para aplicar o desconto de 50%
    if (primeiro_produto == 54) or (segundo_produto == 54):
        if (primeiro_produto == 53) or (segundo_produto == 53):
            valor_total = preco_codigo_0054 * 0.5 + preco_codigo_0053
        else:
            valor_total = preco_codigo_0054 * 0.5 + preco_codigo_0045

# Exibindo o valor total para o usuário
print("+-----------------------------------------------------------+")
print(f"+ O valor total da compra é: R${valor_total: .2f}                       +")
print("+-----------------------------------------------------------+")