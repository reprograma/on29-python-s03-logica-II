# - Explicação do exercício: desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados unidos a partir da informação do ano de nascimento. Leve em consideração se a pessoa tem carteira de motorista.

idade = int(input("Digite sua idade: "))
carteira = input("Você tem carteira de motorista? (s/n): ")

if idade >= 18 and carteira == "s":
    print("Você pode dirigir no Brasil e nos Estados Unidos.")
elif idade >= 18 and carteira == "n":
    print("Você pode dirigir no Brasil, mas não nos Estados Unidos.")
else:
    print("Você não pode dirigir.")
    