from random import randint

print("Jogo De Dados")

dados1 = randint(1, 6)
dados2 = randint(1, 6)
dados3 = randint(1, 6)
dados4 = randint(1, 6)

print("Dado 1:", dados1)
print("Dado 2:", dados2)

jogador1 = dados1 + dados2


print("Dado 3:", dados3)
print("Dado 4:", dados4)

jogador2 = dados3 + dados4

print("Resultado do jogador 1:", jogador1)
print("Resultado do jogador 2:", jogador2)

