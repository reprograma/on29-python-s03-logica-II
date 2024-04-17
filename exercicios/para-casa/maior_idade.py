# Explicação do exercício: desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados
# unidos a partir da informação do ano de nascimento. Leve em consideração se a pessoa tem carteira de motorista.


# 2006 ou maior que 2006
motorista_brasil = 18
# 2008 ou meior que 2008
motorista_eua = 16

ano2024 = 2024

com_cnh = "sim"
sem_cnh = "nao"

permissao = (input("Você tem CNH? Responda 'sim' ou 'nao': ") == com_cnh or sem_cnh)
nascimento = int(input("Digite sua data de nascimento: "))

# Profs, tá dando ruim em alguma coisa aqui mas eu tentei :(

if permissao == sem_cnh:
    print("Você não tem permissão para dirigir!")
elif permissao == com_cnh:
    nascimento - ano2024 >= motorista_brasil
    print("Você pode dirigir no Brasil!")
else: 
    nascimento - ano2024 >= motorista_eua
print("Você pode dirigir nos Estados Unidos!")





