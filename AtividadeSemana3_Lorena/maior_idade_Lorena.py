#Questão 3 - Maior idade (desafio extra) - Aluna: Lorena Vieira

import datetime
from datetime import date, datetime

print("\nOlá, seja bem-vindo!\n")

nascimento_usuario = input("Qual sua data de nascimento (DD/MM/AAAA)? ")
habilitacao = input("Você possui habilitação para dirigir (sim/não)? ")

nascimento_usuario = datetime.strptime(nascimento_usuario, "%d/%m/%Y")
hoje = datetime.today()

idade_usuario = hoje - nascimento_usuario
idade_usuario_em_anos = idade_usuario.days / 365.25

maior_idade_BR = 18
maior_idade_EUA = 16

if idade_usuario_em_anos >= maior_idade_BR and habilitacao == "sim":
    print("\nVocê está apto e habilitado para dirigir no Brasil e nos Estados Unidos.")
elif idade_usuario_em_anos >= maior_idade_BR and habilitacao == "não":
    print("\nVocê está apto para dirigir no Brasil e nos Estados Unidos, porém precisa ser habilitado.")
elif idade_usuario_em_anos >= maior_idade_EUA and idade_usuario_em_anos < maior_idade_BR and habilitacao == "não":
    print("\nVocê está inapto para dirigir no Brasil e apto para dirigir nos Estados Unidos, porém ainda precisa ser habilitado.")
elif idade_usuario_em_anos >= maior_idade_EUA and idade_usuario_em_anos < maior_idade_BR and habilitacao == "sim":
    print("\nVocê está apto e habilitado para dirigir somente nos Estados Unidos.")
elif idade_usuario_em_anos >= maior_idade_EUA and idade_usuario_em_anos < maior_idade_BR and habilitacao == "não":
    print("\nVocê está apto para dirigir somente nos Estados Unidos, porém precisa ser habilitado.")
else:
    print("Você está inapto para dirigir no Brasil e nos Estados unidos.")




