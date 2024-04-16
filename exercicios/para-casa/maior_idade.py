print('Autoescola - Poneicar')
habilitacao = input('Você já tem carteira de habilitação? Responda S ou N. ')

if habilitacao == ('S'):
    print('O cliente já é habilitado.')
elif habilitacao == ('N'):
    print('O cliente deve preencher as informações abaixo para conferir se pode dar seguimento ao processo de habilitação.') 
    dia = int(input('Digite o dia do seu nascimento: '))
    mes = int(input('Digite o mês do seu nascimento: '))
    ano = int(input('Digite seu ano do seu nascimento: '))

    if mes <= int(4) and ano <= int(2006):
        print('Pode tirar a carteira de habilitação no Brasil e nos EUA.')
    elif mes <= int(4) and ano <= int(2008):
        print('Pode tirar a carteira de habilitação apenas nos EUA.')
    else:
        print('Não pode tirar a carteira de habilitação.')