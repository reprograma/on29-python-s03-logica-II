ano_nasc = int(input("Insira seu ano de nascimento: "))
idade = 2024 - ano_nasc

if idade >= 18:
  cart_moto = input("Você possui carteira de motorista no Brasil? (SIM/NÃO): ").lower()
  if cart_moto == "sim":
    print("Você pode dirigir tanto no Brasil quanto nos EUA!")
  else:
    print("Você não pode dirigir nem no Brasil nem nos EUA, mas já está autorizado a tirar sua carteira de motorista em ambos os países!")
else:
  if idade >= 16:
    print("Você ainda não pode dirigir no Brasil (nem tirar sua carteira) mas pode tirar sua carteira e dirigir nos EUA!")
  else:
    print("Você ainda não pode tirar sua carteira nem nos EUA nem no Brasil, muito menos dirigir!")