def programa ():
     
    
    print("\nFÁRMACIA POPULAR\n\nNa compra de dois produtos iguais, receba 5,00 reais de desconto!\n ")

    print("Escolha os produto, selecionando um número de 1 a 4:")

    print ("[1] Sabonete Líquido Nívea (1l) = 12,59\n[2] Pasta de Dente SENDODYNE (250g) = 15,78\n[3] Escova de dente Colgate (2un.) = 23,89\n[4] Mascara de Tratamento = 59,99\n")
    
    primeiro_produto = int(input())
    segundo_produto = int(input())

    if (primeiro_produto < 1 or primeiro_produto > 4) or (segundo_produto < 1 or segundo_produto > 4):
        print("Valor Inválido!\nVocê será redirecionado(a) para o menu de seleção novamente.")
       
        programa()
        return

    preco1 = 12.59
    preco2 = 15.78
    preco3 = 23.89
    preco4 = 59.99

    if primeiro_produto == 1:
        primeiro_produto = preco1
    elif primeiro_produto == 2:
        primeiro_produto = preco2
    elif primeiro_produto == 3:
        primeiro_produto = preco3
    elif primeiro_produto == 4:
        primeiro_produto = preco4
    
  
    if segundo_produto == 1:
        segundo_produto = preco1
    elif segundo_produto == 2:
        segundo_produto = preco2
    elif segundo_produto == 3:
        segundo_produto = preco3
    elif segundo_produto == 4:
        segundo_produto = preco4

    if primeiro_produto == segundo_produto:
        print("O valor da sua compra, com desconto foi:",(primeiro_produto + segundo_produto)-5,"reais\nObrigada, volte sempre!")
    elif primeiro_produto != segundo_produto:
        print("O valor da sua compra foi:",primeiro_produto + segundo_produto,"reais\nObrigada, volte sempre!")

programa()

