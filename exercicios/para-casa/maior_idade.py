'''Explicação do exercício: desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados unidos a partir da informação do ano de nascimento. Leve em consideração se a pessoa tem carteira de motorista.'''

ano_nascimento = int(input("Qual seu ano de nascimento?"))
nacionalidade = input("Qual a sua nacionalidade?")

if nacionalidade == "Estados Unidos":
    if (2024 - ano_nascimento) >= 16:
        print("Pode dirigir")
    else:
        print("Não pode dirigir")
else:
    if (2024 - ano_nascimento) >= 18:
        print("Pode dirigir")
    else:
        print("Não pode dirigir") 