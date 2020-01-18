""" Main module to start application"""
from exceptions import EnemyDown
from exceptions import GameOver
from models import Enemy
from models import Player

def play():
    """ Method to start the game"""
    name = input("Enter your name : ")
    player = Player(name)
    start = input("Enter 'start' when you are ready for battle: ")
    if start == 'start':
        print('Get ready')
    else:
        play()
    level = 1
    enemy = Enemy(1)
    while True:
        try:
            player.attack(enemy)
            player.defense(enemy)
        except EnemyDown:
            level += 1
            player.score += 5
            enemy = Enemy(level)


if __name__ == "__main__":
    try:
        play()
    except GameOver:
        GameOver.save_result
    except KeyboardInterrupt:
        pass
    finally:
        scores = input("If you want to check latest scores print 'scores': ")
        if scores == 'scores':
            with open('scores.txt', 'r') as file:
                line = file.read()
                print(line)


