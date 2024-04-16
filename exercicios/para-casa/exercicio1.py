print("~" * 20)
print("RETIRANDO O LIXO")
print("~" * 20)

print("\nVá até a cozinha, abra a tampa do lixo.\nAgora verifique se...")


lixo = int(input("1. Contém Lixo\n2. Lixo Cheio\n3. Sem Lixo.\nDigite o número correspondente ao estado do Lixo da sua cozinha:\n"))


if lixo == 1:
    print("Você precisa colocar o lixo da sua cozinha dentro do lixo maior na área de Serviço.")
elif lixo == 2:
    print("Seu lixo está transbordando, você precisa tirar o saco e levar para a lixeira do condomínio para evitar mau cheiro.\nNa volta lave o cesto e coloque um saco limpo.")
elif lixo == 3:
    print("O seu lixo está vazio e você não precisa se preocupar com isso nesse momento, vá beber uma água (: ")
else:
    print("Opção inválida")
    