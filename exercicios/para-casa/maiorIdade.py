# maiorIdade.py

# Maior idade (desafio extra)Explicação do exercício: 
# desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou 
# no estados unidos a partir da informação do ano de nascimento. 
# Leve em consideração se a pessoa tem carteira de motorista.


ano_atual = 2024
ano_de_nascimento = int(input())

idade = ano_atual - ano_de_nascimento

possui_carteira = input("Possui carteira de motorista? (S/N): ").upper() == "S"

if idade > 18:
    if possui_carteira:
        print("pode dirigir nos EUA e no Brasil")
    
    else:
        print("Pode dirigir no Brasil, mas precisa de uma carteira de motorista.")

else:
    print("Você ainda não tem idade para dirigir")
