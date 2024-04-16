
anoAtual = 2024
anoNascimento = int(input("Qual seu ano de nascimento? "))
nacionalidade = input("Você nasceu no BR ou USA?")
idadeAtual = anoAtual - anoNascimento


if idadeAtual >= 18 and nacionalidade == "BR":
        print(f"Você tem {idadeAtual} e no seu país {nacionalidade} é permitido dirigir a partir de 18 anos. Já pode tirar habilitação!")
elif idadeAtual >= 16 and nacionalidade == "USA":
        print(f"Você tem {idadeAtual} e no seu país {nacionalidade} é permitido dirigir a partir de 16 anos. Já pode tirar habilitação!")
else:
    print("Você ainda não tem idade para dirigir!")