## Maior idade (desafio extra)
# - Explicação do exercício: 
# desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados unidos 
# a partir da informação do ano de nascimento.
# Leve em consideração se a pessoa tem carteira de motorista.

ano_atual= 2024
try:
    habilitacao= input("Você tem habilitação? ")

    if habilitacao == "sim" or habilitacao == "Sim":
        ano_nasc= int(input("Informe seu ano de nascimento: "))
        if ano_atual - ano_nasc >= 18:
            print("Você tem habilitação e pode dirigir no brasil e no USA!!!")
        elif ano_atual - ano_nasc >= 16:
            print("Você tem habilitação e pode dirigir nos estados unidos!!!")
        else:
            print("Você não tem idade para dirigir no Brasil e tampouco nos USA")        
    else:
        if habilitacao == "não" or habilitacao == "Não" or habilitacao == "nao" or habilitacao == "Nao":
            print("Você não tem habilitação! Não pode dirigir :D")
        else:
            print("Você digitou alguma coisa errada. Escreva 'sim' ou 'não, please")
except:
    print("Você digitou um caractere incorreto, tente novamente.")