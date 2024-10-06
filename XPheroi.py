# Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

# Se XP for menor do que 1.000 = Ferro
# Se XP for entre 1.001 e 2.000 = Bronze
# Se XP for entre 2.001 e 5.000 = Prata
# Se XP for entre 5.001 e 7.000 = Ouro
# Se XP for entre 7.001 e 8.000 = Platina
# Se XP for entre 8.001 e 9.000 = Ascendente
# Se XP for entre 9.001 e 10.000= Imortal
# Se XP for maior ou igual a 10.001 = Radiante

# ## Saída

# Ao final deve se exibir uma mensagem:
# "O Herói de nome **{nome}** está no nível de **{nivel}**"

from random import randint 

jogador = str(input('Digite seu nome herói: '))
nivel = randint(1,12000)



while True:
     
     if 1 <= nivel <=  1000:
          print(f'O Herói de nome {jogador} está com {nivel} no nível ferro')
     elif 1001 <= nivel <= 2000:     
          print(f'O Herói de nome {jogador} está com {nivel} no nível bronze')
     elif 2001 <= nivel <= 5000:     
          print(f'O Herói de nome {jogador} está com {nivel} no nível prata')
     elif 5001 <= nivel <= 7000:     
          print(f'O Herói de nome {jogador} está com {nivel} no nível ouro')
     elif 7001 <= nivel <= 8000:     
          print(f'O Herói de nome {jogador} está com {nivel} no nível platina')
     elif 8001 <= nivel <= 9000:     
          print(f'O Herói de nome {jogador} está com {nivel} no nível ascendente')
     elif 9001 <= nivel <= 10000:     
          print(f'O Herói de nome {jogador} está com {nivel} no nível imortal')
     else:
          print(f'O Herói de nome {jogador} está com {nivel} no nível radiante')

     break

     