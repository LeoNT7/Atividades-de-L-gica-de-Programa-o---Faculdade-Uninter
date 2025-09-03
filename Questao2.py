# inicio  
print("Olá Leonardo Bento, seja bem vindo(a)!")  
  
# entrada de dados  
valor_pedido = float(input("Digite o valor do pedido: "))  
quantidade_parcelas = int(input("Digite a quantidade de parcelas: "))  
  
# condicional que define o percentual de juros  
if quantidade_parcelas < 4:  
    juros = 0 / 100  
elif (quantidade_parcelas >= 4) and (quantidade_parcelas < 6):  
    juros = 4 / 100  
elif (quantidade_parcelas >= 6) and (quantidade_parcelas < 9):  
    juros = 8 / 100  
elif (quantidade_parcelas >= 9) and (quantidade_parcelas < 13):  
    juros = 16 / 100  
else:  
    juros = 32 / 100  
  
# calcula valor total parcelado e valor da parcela, ambos com juros já inclusos  
valor_total_parcelado = valor_pedido * (1 + juros)  
valor_parcela = valor_total_parcelado / quantidade_parcelas  
  
# imprimindo os resultados com f string  
print(f"O valor das parcelas é de: R${valor_parcela}")  
print(f"O valor total parcelado é de: R${valor_total_parcelado}")  
# fim  