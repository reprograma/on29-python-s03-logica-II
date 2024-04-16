habilitacao = input("Voce tem habilitacao? responda 's' para 'SIM' e 'n' para 'NAO': ")
data_de_nascimento = int(input("Insira  aqui seu ano de nascimento: "))
idade = 2024 - data_de_nascimento

if habilitacao == "s" and idade >= 18:
    print("Voce tem permissao para dirigir no Brasil e nos EUA")
elif habilitacao == "s" and idade >= 16:
    print("Voce tem permissao para dirigir apenas nos EUA")
else:
    print("Voce nao tem permissao para dirigir!")