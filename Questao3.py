print("Olá Leonardo Bento, bem vindo ao Uniformes Xeres LTDA") 
 
def escolha_modelo(): 
    while True: 
        modelo = input("Entre com o modelo desejado\n" 
                       "MCS - Manga Curta Simples\n" 
                       "MLS - Manga Longa Simples\n" 
                       "MCE - Manga Curta Com Estampa\n" 
                       "MLE - Manga Longa Com Estampa\n" 
                       ">>") 
        if modelo == "MCS": 
            return 1.80 
        elif modelo == "MLS": 
            return 2.10 
        elif modelo == "MCE": 
            return 2.90 
        elif modelo == "MLE": 
            return 3.20 
        else: 
            print("Escolha inválida, entre com o modelo novamente") 
            continue 
 
def num_camisetas(): 
    while True: 
        try: 
            qnt = int(input("Entre com o número de camisetas: ")) 
            if qnt >= 2000 and qnt <= 20000: 
                desconto = 0.12 
                return qnt, desconto 
            elif qnt >= 200 and qnt < 2000: 
                desconto = 0.07 
                return qnt, desconto 
            elif qnt >= 20 and qnt < 200: 
                desconto = 0.05 
                return qnt, desconto 
            elif qnt < 20: 
                desconto = 0 
                return qnt, desconto 
            else: 
                print("Não aceitamos tantas camisetas de uma vez.") 
                continue 
        except ValueError: 
            print("Por favor, entre com o número de camiseta novamente.") 
 
def frete(): 
    while True: 
        escolha = int(input("Escolha o tipo de frete: \n" 
                      "1 - Frete por transportadora - R$ 100.00\n" 
                      "2 - Frete por Sedex - R$ 200.00\n" 
                      "0 - Retirar pedido na fábrica - R$ 0.00\n" 
                      ">>")) 
        if escolha == 1: 
            return 100 
        elif escolha == 2: 
            return 200 
        elif escolha == 0: 
            return 0 
        else: 
            print("Opção inválida, tente novamente.") 
    #Retorna (use return) o valor de apenas uma das opções de frete 
    #Repetir a pergunta item D.a se digitar uma opção diferente de: 1/2/0; 
valor_modelo = escolha_modelo() 
qnt, desconto = num_camisetas() 
valor_frete = frete() 
 
total = (valor_modelo * qnt) * (1 - desconto) + valor_frete 
print(f"Total a pagar: R$ {total:.2f}") 
 