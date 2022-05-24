from PPlayTeste.window import *
from PPlayTeste.gameimage import *
from keys import Piano

class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 480, 156
        self.running = True
        self.screen = Window(self.WIDTH, self.HEIGHT)
        self.screen.set_title("Pianasso")
        self.background = GameImage("piano.jpg")
        self.keyboard = self.screen.get_keyboard()
        self.piano = Piano()

    def check_events(self):
        if self.keyboard.key_pressed("z"):
            self.piano.sustain = True
        if self.keyboard.key_pressed("x"):
            self.piano.sustain = False

        if self.keyboard.key_pressed("a"):
            self.piano.do = True
        else:
            self.piano.do = False
        if self.keyboard.key_pressed("s"):
            self.piano.re = True
        else:
            self.piano.re = False
        if self.keyboard.key_pressed("d"):
            self.piano.mi = True
        else:
            self.piano.mi = False
        if self.keyboard.key_pressed("f"):
            self.piano.fa = True
        else:
            self.piano.fa = False
        if self.keyboard.key_pressed("g"):
            self.piano.sol = True
        else:
            self.piano.sol = False
        if self.keyboard.key_pressed("h"):
            self.piano.la = True
        else:
            self.piano.la = False
        if self.keyboard.key_pressed("j"):
            self.piano.si = True
        else:
            self.piano.si = False
        

    def desenha(self):
        piano = self.piano
        if piano.sustain:
            piano.with_sustain.draw()
        else:
            piano.without_sustain.draw()
        if piano.do:
            piano.nota_do.draw()
        if piano.re:
            piano.nota_re.draw()
        if piano.mi:
            piano.nota_mi.draw()
        if piano.fa:
            piano.nota_fa.draw()
        if piano.sol:
            piano.nota_sol.draw()
        if piano.la:
            piano.nota_la.draw()
        if piano.si:
            piano.nota_si.draw()

    def toca(self):
        piano = self.piano
        # print(piano.do,piano.re,piano.mi,piano.fa,piano.sol,piano.la,piano.si)
        print(piano.som_do.is_playing(),piano.som_re.is_playing(),piano.som_mi.is_playing(),piano.som_fa.is_playing(),piano.som_sol.is_playing(),piano.som_la.is_playing(),piano.som_si.is_playing())
        if piano.do:
            piano.som_do.play()
        else:
            if piano.som_do.is_playing() and not piano.sustain:
                piano.som_do.stop()
        if piano.re:
            piano.som_re.play()
        else:
            if piano.som_re.is_playing() and not piano.sustain:
                piano.som_re.stop()
        if piano.mi:
            piano.som_mi.play()
        else:
            if piano.som_mi.is_playing() and not piano.sustain:
                piano.som_mi.stop()
        if piano.fa:
            piano.som_fa.play()
        else:
            if piano.som_fa.is_playing() and not piano.sustain:
                piano.som_fa.stop()
        if piano.sol:
            piano.som_sol.play()
        else:
            if piano.som_sol.is_playing() and not piano.sustain:
                piano.som_sol.stop()
        if piano.la:
            piano.som_la.play()
        else:
            if piano.som_la.is_playing() and not piano.sustain:
                piano.som_la.stop()
        if piano.si:
            piano.som_si.play()
        else:
            if piano.som_si.is_playing() and not piano.sustain:
                piano.som_si.stop()
