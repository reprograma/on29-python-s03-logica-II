# Receita Brigadeiro de Colher

# Ingredientes
# 1 lata de leite condensado
# 1 lata de creme de leite
# 3 colheres de sopa de chocolate em pó

def preparar():
    condensado = int(input("Informe a quantidade de latas de leite condensado que você vai usar na receita: "))
    creme_leite = int(input("Informe a quantidade de latas de creme de leite que você vai usar na receita: "))
    chocolate = int(input("Informe a quantidade de colheres de chocolate em pó que você vai usar na receita: "))
    colher_chocolate = 2 * chocolate
    print(f"Para a quantidade de {condensado} de leite condensado informada, será preciso usar {creme_leite} de creme de leite e {colher_chocolate} de chocolate em pó.")
    print("Passo 1: Ainda em fogo apagado, em uma panela, coloque as latas de leite condensado e o chocolate em pó e mexa até ficar homogêneo.")
    print("Passo 2: Após isso, acrescente o creme de leite. Este passo é importante, pois o creme de leite e o pó não se misturam facilmente.")
    print("Passo 3: Leve ao fogo baixo, mexendo sempre, até que a mistura desgrude do fundo da panela.")
    print("Passo 4: Desligue o fogo e deixe o brigadeiro esfriar um pouco.")
    print("Passo 5: Está pronto :)")

preparar()
