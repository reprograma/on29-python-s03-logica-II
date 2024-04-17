#EXERCICIO 1

# LAVANDO ROUPAS  
print('-' * 30)
print('hoje é dia de lavar roupas querida! Pegue as roupas sujas e coloque na maquina.')
print('-' * 30)

lavar_roupas = True

comando_lavar_estender = int(input('Após o primeiro ciclo de lavagem confira a roupa, se ainda estiver suja digite 1, se tiver apenas manchinhas digite 2 e se limpa digite 3:'))


if lavar_roupas == True:
    print(comando_lavar_estender)
    if comando_lavar_estender == 1:
        print('Volte para a maquina e lave novamente')
    elif comando_lavar_estender == 2:
        print('Querida já que temos apenas manchas será necessário lavar manualmente com a escova. Após isso estenda.')
    else:
      print('Mulher a lavagem de roupas foi um sucesso!!!! Agora só estender.') 