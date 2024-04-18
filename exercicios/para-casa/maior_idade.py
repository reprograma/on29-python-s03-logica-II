'''
Explicação do exercício: desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados unidos a
 partir da informação do ano de nascimento. Leve em consideração se a pessoa tem carteira de motorista.
---
'''


print("Aluga-se Carros\n\nResponda o questionario a seguir:")

nome = input("NOME: ")
ano = input("Ano de Nascimento: ")
idade =  2024 - int(ano)
habilitado = input("Possui Carteira motorista: [S] ou [N]?")
pais = input("Em qual pais você mora:\n Selecione: [B] para Brasil\n [E] para Estados Unidos\n")


print("Termos e condições para conseguir alugar um carro em nossas lojas:\n\n") 
if idade >=18 and (habilitado == "s" or habilitado == "S") and (pais == "b" or pais == "B"):
    print("O contratante é maior de 18 anos e possui habilitação\n Potanto o senhor" , nome, "está apto para alugar nossos carros em qualquer  uma de nossas loja no BRASIL")
elif idade >=16  and (habilitado == "s" or habilitado == "S") and (pais == "e" or pais == "E"):
    print("O contratante é maior de 16 anos e possui habilitação\n Potanto o senhor" , nome, "está apto para alugar nossos carros em qualquer umas de nossas loja no ESTADOS UNINDOS")
else: 
    print("O senhor", nome, "não pode solicitar nossos serviços, pois não atende nossos temos e condições para ambos paises")   
     
     


