import random

GOR = 'gor'
DESNO = 'desno'

class Polje:

    def __init__(self, visina=10, sirina=10):
        self.visina = visina
        self.sirina = sirina
        self.korak = 0
        self.seznam = []
        self.resitev = []
        self.stevec = 0
        
        
    def nova_igra(self):
        # Ob začetku igre ustvari pot (rešitev)
        self.seznam = (self.visina - 1)*[DESNO] + (self.sirina - 1)*[GOR]
        random.shuffle(self.seznam)
        self.resitev = []
        i, j = (self.visina - 1, 0)
        for smer in self.seznam:
            if smer == GOR:
                i -= 1
            else:
                j += 1
            self.resitev.append((i,j))


    def ugibaj(self, smer):
        # Preveri če si zadel pot ali ne, tako da primerja
        # pritisnjeno tipko s seznamom rešitve
        
        if smer == self.seznam[self.korak]:
            self.korak += 1
        else:
            # zgrešena poteza
            self.korak = 0
            self.stevec += 1
            

    def __repr__(self):
        return 'Polje(visina={}, sirina={}, resitev={})'.format(
            self.visina, self.sirina, self.resitev)




