from random import randint
from time import sleep

pc = randint(0, 10)

print("Sou seu computador...")
print("Acabei de pensar em um número de 0 a 10.")
print("Será que você consegue acertar?")

n = int(input("Qual o seu palpite?:"))
c = 1
while n != pc:
    if pc > n:
        print("Mais...tente mais uma vez.")
        n = int(input("Qual o seu palpite?:"))
        c += 1
    else:
        if pc < n:
            print("Menos...tente mais uma vez.")
            n = int(input("Qual o seu palpite?:"))
            c += 1
print('Analisando...'),sleep(2)
print(f"Acertou com {c} tentativas, parabéns!")