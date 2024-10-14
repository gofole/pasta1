produto = 'biscoito'
preco = 1.99
qntd = int(input('digite a quantidade de pacotes'))

total = preco * qntd

# Voce comprou [produtoe] e total é [total]
mensagem = F'Voce comprou {qntd} {produto} e o total é $ {total}'
print(mensagem)