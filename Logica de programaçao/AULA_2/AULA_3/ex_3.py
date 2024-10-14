# #idade = int(input('digite sua idade'))

# if idade >=18:
#  print("voce e maior de 18 pode votar")
# else:
#     print("voce menor que 18  anos nao pode votar") 
    
    
    
    #1 PEDIR A IDADE 
    #2 TESTAR 
    
# idade = int(input("digite a idade" ))
# print(idade)
# idade = input('Digite a idade por extenso. Ex: um '))
# print(idade)
# if idade <= "um" or idade == 'dois' or idade == 'tres':
#     print('criança')
# elif idade <= 17:
#     print('Adolescente')
# elif idade <= 59:
#     print('adulto') 
# else:
#     print('idoso')   

# turno = (input('digite o seu turno Usando Apenas ( m ) para manha (v) para Tarde é (n) para noite'))

# if turno == 'm':
#     print('bom dia ')
# elif turno == 'v':    
#     print('Boa tarde ')
# elif turno == 'n':
#     print('boa noite ')
    
    
    
    
    
estacao = int(input('digite o numero do més que voce esta'))

if estacao >= 3 or estacao <= 5:
    print('Voce esta no Outono')
elif estacao <= 8:
    print('Inverno')
elif estacao <= 10:
    print('Primavera')
elif estacao <= 12 or estacao == 1 or estacao == 2:
    print('verao')