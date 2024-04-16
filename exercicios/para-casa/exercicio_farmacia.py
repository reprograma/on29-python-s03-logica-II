preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0


primeiro_produto = int(input())
segundo_produto = int(input())

'''- Explicação do exercício: 
Farmacia Popular está em promoção. A cada 2 produtos iguais comprados(foque somente nos clientes sempre comprando dois produtos), receba 5 reais de desconto, se forem diferente mas um dos produtos for o codigo 0054 ele tem 50% de desconto nesse produto, se não valor não recebe desconto.Escreva um programa para auxiliar a farmacia a calcular o valor final do produto.'''

# desenvolva a logica condicional
if primeiro_produto == segundo_produto:
    print("Desconto de 5 reais")
    if primeiro_produto == 53 and segundo_produto == 53:
        print("Total de 4.6+4.6-5= 4.4 reais")
    elif primeiro_produto == 45 and segundo_produto == 45:
        print("Total de 50+50-5= 95 reais")
else:
    if primeiro_produto == 54 or segundo_produto == 54:
        print("Desconto de 50%")
        if primeiro_produto == 54 and segundo_produto == 54:
            print("Total de (10.4+10.4)*50/100 = 10.4 reais")
        elif primeiro_produto == 54 and segundo_produto == 53:
            print("Total de (10.4+4.6)*50/100 = 7.5 reais")
        elif primeiro_produto == 54 and segundo_produto == 45:
            print("Total de (10.4+50)*50/100 = 30.2 reais")
    else:
        print("Não recebe nenhum desconto")
