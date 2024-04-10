



import random

numerosjogador1 = []
numerosjogador2 = []


for i in range(3):

    numero = random.randint(1,6)
    numerosjogador1.append(numero)
    numero = random.randint(1,6)
    numerosjogador2.append(numero)

somajogador1 = sum(numerosjogador1)
somajogador2 = sum(numerosjogador2)

print("Jogador 1:", numerosjogador1, "=> Soma:", somajogador1)
print("Jogador 2:", numerosjogador2, "=> Soma:", somajogador2)

if somajogador1 > somajogador2:
    print("Jogador 1 é o vencedor! ")
elif somajogador2 > somajogador1:
    print("Jogador 2 é o vencedor! ")
else:
    print("Empate")
    


