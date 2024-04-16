"""
- Explicação do exercício: desenvolva um sistema em que verifique se a pessoa pode dirigir no Brasil ou no estados unidos a partir da informação do ano de nascimento. Leve em consideração se a pessoa tem carteira de motorista.
"""

# Importando o datetime para obter a data atual

import datetime

def verificar_dirigir(nascimento, tem_carteira=False, pais="Brasil"):
    # Obtendo a data atual
    data_atual = datetime.datetime.now()
    
    # Calculando a idade da pessoa
    idade = data_atual.year - nascimento.year - ((data_atual.month, data_atual.day) < (nascimento.month, nascimento.day))
    
    # Verificando se a pessoa tem idade suficiente para dirigir
    idade_minima_brasil = 18
    idade_minima_eua = 16
    
    if pais.lower() == "brasil":
        if idade >= idade_minima_brasil:
            if tem_carteira:
                return "Você pode dirigir no Brasil!"
            else:
                return "Você precisa ter uma carteira de motorista para dirigir no Brasil."
        else:
            return f"Você ainda não tem idade suficiente para dirigir no Brasil. Idade mínima: {idade_minima_brasil} anos."
    elif pais.lower() == "estados unidos" or pais.lower() == "eua":
        if idade >= idade_minima_eua:
            if tem_carteira:
                return "Você pode dirigir nos Estados Unidos!"
            else:
                return "Você precisa ter uma carteira de motorista para dirigir nos Estados Unidos."
        else:
            return f"Você ainda não tem idade suficiente para dirigir nos Estados Unidos. Idade mínima: {idade_minima_eua} anos."
    else:
        return "Por favor, especifique 'Brasil' ou 'Estados Unidos' como país."

# Obter dados do usuário
ano_nascimento_str = input("Digite o ano de nascimento (no formato YYYY): ")
ano_nascimento = datetime.datetime.strptime(ano_nascimento_str, "%Y")
tem_carteira_str = input("Você possui carteira de motorista? (sim/não): ").lower()
tem_carteira = tem_carteira_str == "sim"
pais = input("Digite o país onde deseja dirigir (Brasil/Estados Unidos): ")

# Verificar se pode dirigir no país especificado
print(verificar_dirigir(ano_nascimento, tem_carteira, pais))