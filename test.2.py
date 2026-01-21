import random


health_player = 100
attack_player = 15

health_enemy1 = random.randint(100,200)
attack_enemy1 = random.randint(10, 20)


health_enemy2 = random.randint(60,180)
attack_enemy2 = random.randint(23, 40)


health_enemy3 = random.randint(40,120)
attack_enemy3 = random.randint(5, 15)


turn = 1 # turn 1 = jucator alege,turn 2 = inamicul alege

def attack1():
    global health_enemy1, turn
    if turn == 1:
     health_enemy1 -= attack_player + random.randint(1,5)
    turn = 2
    if health_enemy1 <= 0:
        print("ai cistigat")
        exit()

def attack2():
    global health_enemy2, turn
    if turn == 1:
     health_enemy2 -= attack_player + random.randint(2,5)
    turn = 2
    if health_enemy2 <= 0:
        print("ai cistigat")
        exit()

def attack3():
    global health_enemy2, turn
    if turn == 1:
     health_enemy2 -= attack_player + random.randint(2,5)
    turn = 2
    if health_enemy2 <= 0:
        print("ai pierdut")
        exit()

def attack_enemyy1():
    print("viata jucatorului:", health_player, "viata inami:", health_enemy1)
    global health_player, turn
    health_player -= attack_enemy1
    if health_player <= 0:
        print("ai pierdut")
        exit()

def attack_enemyy2():
    print("viata jucatorului:", health_player, "viata inami:", health_enemy2)
    global health_player, turn
    health_player -= attack_enemy2
    if health_player <= 0:
        print("ai pierdut")
        exit()

def attack_enemyy3():
    print("viata jucatorului:", health_player, "viata inami:", health_enemy3)
    global health_player, turn
    health_player -= attack_enemy3
    if health_player <= 6:
        print("ai cistigat")
        exit()




def optiuni():
    print("1 - attack")
    print("2 - heal")
    print("3 - leave game")

while True:
    optiuni()
    n = int(input('ce optiune alegeti:'))
    if n == 1:
        attack1()
    elif n ==2:
        print("la revedere")
        break
        pass
    else:
        print("ati scris gresit")

