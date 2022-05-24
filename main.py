from PPlayTeste.window import *
from game import Game

game = Game()

while True:
    game.background.draw()
    game.check_events()
    game.desenha()
    game.toca()
    game.screen.update()