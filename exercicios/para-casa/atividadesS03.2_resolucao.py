###2- Desconto farmácia
# Explicação do exercício: Farmácia Popular está em promoção.
# A cada 2 produtos iguais comprados(foque somente nos clientes sempre comprando dois produtos), 
# receba 5 reais de desconto, se forem diferente mas um dos produtos for o código 0054 ele tem 50% de desconto nesse produto, 
# se não valor não recebe desconto.
# Escreva um programa para auxiliar a farmácia a calcular o valor final do produto.
# salvar códigos que entram pelo input em uma variável
# Fazer a logica da condição
# fazer ação de calcular desconto.
# retornar valor total

p0= "0050"
p1= "0051"
p2= "0052"
p3= "0053"
p4= "0054"

v0= 10
v1= 20
v2= 30
v3= 40
v4= 50
promo= 5

desct_especial= v4 * 0.50 


produto1_cliente= input("Informe o primeiro código do produto: ")
produto2_cliente= input("Informe o segundo código do produto: ")


if produto1_cliente == p0 and produto2_cliente == p0:
    valor_total= (v0*2) - promo
    print("Esse é o valor p0", valor_total)
elif produto1_cliente == p1 and produto2_cliente == p1:
    valor_total= (v1*2) - promo
    print("Esse é o valor p1", valor_total)
elif produto1_cliente == p2 and produto2_cliente == p2:
    valor_total= (v2*2) - promo
    print("Esse é o valor p2", valor_total)
elif produto1_cliente == p3 and produto2_cliente == p3:
    valor_total= (v3*2) - promo
    print("Esse é o valor p0", valor_total)
elif produto1_cliente == p4 and produto2_cliente == p4:
    valor_total= desct_especial
    print("Esse é o valor p4", valor_total)
    
elif produto1_cliente and produto2_cliente == p0 and produto1_cliente and produto2_cliente == p4:
        valor_total= v0 + desct_especial
        print("V0 com 0054:", valor_total)
elif produto1_cliente and produto2_cliente == p1 and produto1_cliente and produto2_cliente == p4:
        valor_total= v1 + desct_especial
        print("V1 com 0054:", valor_total)
elif produto1_cliente and produto2_cliente == p2 and produto1_cliente and produto2_cliente == p4:
        valor_total= v2 + desct_especial
        print("V1 com 0054:", valor_total)
elif produto1_cliente and produto2_cliente == p3 and produto1_cliente and produto2_cliente == p4:
        valor_total= v3 + desct_especial
        print("V1 com 0054:", valor_total)
else:
    print("Não tem desconto")