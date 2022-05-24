from PPlayTeste.gameimage import *
from PPlayTeste.sound import *

class Piano:
    def __init__(self) -> None:
        self.do, self.re, self.mi, self.fa, self.sol, self.la, self.si = False,False,False,False,False,False,False
        self.sustain = False
        self.nota_do = GameImage("notas/do.png")
        self.som_do = Sound("notas/do.ogg")
        self.som_do.decrease_volume(30)
        self.nota_do.set_position(1,7)
        self.nota_re = GameImage("notas/re.png")
        self.som_re = Sound("notas/re.ogg")
        self.som_re.decrease_volume(30)
        self.nota_re.set_position(31,7)
        self.nota_mi = GameImage("notas/mi.png")
        self.som_mi = Sound("notas/mi.ogg")
        self.som_mi.decrease_volume(30)
        self.nota_mi.set_position(74,7)
        self.nota_fa = GameImage("notas/fa.png")
        self.som_fa = Sound("notas/fa.ogg")
        self.som_fa.decrease_volume(30)
        self.nota_fa.set_position(108,7)
        self.nota_sol = GameImage("notas/sol.png")
        self.som_sol = Sound("notas/sol.ogg")
        self.som_sol.decrease_volume(30)
        self.nota_sol.set_position(134,7)
        self.nota_la = GameImage("notas/la.png")
        self.som_la = Sound("notas/la.ogg")
        self.som_la.decrease_volume(30)
        self.nota_la.set_position(175,7)
        self.nota_si = GameImage("notas/si.png")
        self.som_si = Sound("notas/si.ogg")
        self.som_si.decrease_volume(30)
        self.nota_si.set_position(207,7)
        self.with_sustain = GameImage("sutain.png")
        self.with_sustain.set_position(50, 132)
        self.without_sustain = GameImage("sustain.png")
        self.without_sustain.set_position(50,132)

    def reset_keys(self):
        self.do, self.re, self.mi, self.fa, self.sol, self.la, self.si = False,False,False,False,False,False,False