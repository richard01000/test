import random

health_player = 100
attack_player = 15

health_enemy = random.randint(100,200)
attack_enemy = random.randint(10,20)

turn 1 # turn 1 = jucator alege

def attack():
    global health_enemy, turn
    if turn == 1:
    health_enemy -= attack_player + random.randint(1,5)
    turn = 2
    if health_enemy <= 0:
        print("ai cistigat")
        exit()



def heal():
    global health_player, turn
    if turn == 1:
       health_player += random.randint(10,20)
       turn = 2
       if health_player > 100:
            health_player = 100


def attack_enemyy():
    global health_player, turn
    health_player -= attack_enemy
    if health_player <= 0:
        print("ai pierdut")
        exit()

def heal_enemy():
    global health_enemy, turn
    health_player += random.randint(1,5)
    turn = 1




def choise():
    c = random.randint(1,2)
    if c == 1:
        attack_enemy()
    elif c ==2:
        heal_enemy




def optiuni():
    print("viata jucatorului:",health_player,"viata inami:",health_enemy)
    print("1 - attack")
    print("2 - heal")
    print("3 - leave game")

while True:
    optiuni()
    n = int(input('ce optiune alegeti:'))
    if n == 1:
        attack()
    elif n == 2:
        heal()
    elif n ==3:
        print("la revedere")
        break
        pass
    else:
        print("ati scris gresit")

