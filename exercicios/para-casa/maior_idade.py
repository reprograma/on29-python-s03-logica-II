# Maior idade (desafio extra)
# Desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados unidos a partir da informação do ano de nascimento.
# Leve em consideração se a pessoa tem carteira de motorista.

ano = int(input("Digite seu ano de nascimento "))
cnh = int(input("Você possui CNH? Responda 1 para sim ou 2 para não: "))
idade = 2024 - ano


if idade >= 16 and idade < 18:
    print("Possui idade para dirigir nos EUA")
elif idade > 18:
    print("Grandinho o suficiente para dirigir em qualquer lugar 🌎")
else:
    print("Ainda um baby, não pode dirigir em canto nenhum.")
# considerando a CNH
if cnh == 1:
    print("Vai dirigir na legalidade")
else:
    print("Ta na ilegaildade, se liga em 👮🚓")
