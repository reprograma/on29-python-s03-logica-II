def verificar_dirigir_brasil(idade, possui_carteira):
    # Verifica se a pessoa tem idade suficiente para dirigir no Brasil (18 anos) e se possui carteira de motorista
    if idade >= 18 and possui_carteira:
        return True
    else:
        return False

def verificar_dirigir_estados_unidos(idade, possui_carteira):
    # Verifica se a pessoa tem idade suficiente para dirigir nos Estados Unidos (16 anos) e se possui carteira de motorista
    if idade >= 16 and possui_carteira:
        return True
    else:
        return False

def main():
    try:
        ano_nascimento = int(input("Digite o ano de nascimento: "))
        possui_carteira = input("Você possui carteira de motorista? (s/n): ").lower() == 's'

        # Calcula a idade da pessoa
        ano_atual = 2024  # Ano atual fictício para exemplo
        idade = ano_atual - ano_nascimento

        # Verifica se a pessoa pode dirigir no Brasil e nos Estados Unidos
        pode_dirigir_brasil = verificar_dirigir_brasil(idade, possui_carteira)
        pode_dirigir_estados_unidos = verificar_dirigir_estados_unidos(idade, possui_carteira)

        # Imprime o resultado
        if pode_dirigir_brasil:
            print("Você pode dirigir no Brasil.")
        else:
            print("Você não pode dirigir no Brasil.")

        if pode_dirigir_estados_unidos:
            print("Você pode dirigir nos Estados Unidos.")
        else:
            print("Você não pode dirigir nos Estados Unidos.")

    except ValueError:
        print("Por favor, insira um ano de nascimento válido.")
main()