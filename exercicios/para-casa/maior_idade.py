# Desenvolvendo código para maior idade podendo ou não dirigir 

# VARIÁVEL

ano_nascimento = input(("INSERIR ANO DE NASCIMENTO: "))
ano_atual = 2024
idade_atual = ano_atual - int(ano_nascimento)
# IDADE POR PAÍS PARA PODER DIRIGIR

maior_idade_br = 18
maior_idade_eua = 16
if idade_atual >= maior_idade_br:
    print("Já pode dirigir sim no Brasil!")
elif idade_atual < maior_idade_br:
    print("Não vai tá podendo dirigir no Brasil não!")

if idade_atual >= maior_idade_eua:
    print("Já pode dirigir sim no EUA!")
elif idade_atual < maior_idade_eua:
    print("Não vai tá podendo dirigir no EUA não!")


print("FIM DO PROGRAMA!")
      