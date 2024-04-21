#fazer um programa que responda se você pode dirigir no brasil e nos estados com seu ano de nascimento, levando em consideração se tem a carteira de habilitação ou não. 
#idade_habilitado_brasil = 18
#idade_habilitado_eua = 16

ano_nascimento = int(input("Infome seu ano de nascimento: "))
carteira_habilitaçao = str(input("Você tem carteira de motorista? Responda somente com 'sim' ou 'não' minúsculo. "))

ano_atual = 2024

def calculadora_idade(ano_nascimento, ano_atual):
    idade_usuario = ano_atual - ano_nascimento
    return idade_usuario

idade_usuario = calculadora_idade(ano_nascimento, ano_atual)

if idade_usuario >= 18 and carteira_habilitaçao == str("sim"):
    print("Você está habilitado no Brasil para dirigir!")
elif idade_usuario >= 18 and carteira_habilitaçao == str("não"):
    print("Você não pode dirigir no Brasil por não ter carteira de habilitação, mas você já pode tê-la.")
else:
    print("Você não pode dirigir no Brasil.")

if idade_usuario >= 16 and carteira_habilitaçao == str("sim"):
    print("Você está habilitado nos Estados Unidos para dirigir!")
elif idade_usuario >= 16 and carteira_habilitaçao == str("não"):
    print("Você não pode dirigir nos Estados Unidos por não ter carteira de habilitação, mas você já pode tê-la.")
else:
    print("Você não pode dirigir no Estados Unidos.")