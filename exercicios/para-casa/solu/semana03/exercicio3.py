from datetime import date

def idade_dirigir():
    ano_nascimento = int(input("Informe o ano de nascimento: "))
    tem_carteira = input("Você possui carteira de motorista? (S/N): ").upper()
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    dirigir_brasil = idade >= 18 and tem_carteira == "S"
    dirigir_eua = idade >= 16 and tem_carteira == "S"

    if dirigir_brasil:
        print("Se você tem 18 anos ou mais e possui carteira de motorista, vc pode dirigir no Brasil.")
    else:
        print("Você não pode dirigir no Brasil, ou vc é menor de idade ou vc não possui carteira de motorista")

    if dirigir_eua:
        print("Se vc tem mais de 16 anos e possui carteira de motorista, vc pode dirigir nos EUA.")
    else:
        print("Você não pode dirigir nos Estados Unidos, ou vc não tem 16 anos ou mais ou vc não possui carteira de motorista")

idade_dirigir()

