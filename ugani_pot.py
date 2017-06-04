import random

GOR = 'gor'
DESNO = 'desno'

class Polje:

    def __init__(self, visina=10, sirina=10, pot=None):
        self.visina = visina
        self.sirina = sirina
        if pot is None:
            self.pot = []
        else:
            self.pot = pot
            
        self.izbrana_pot = []

    

    def __repr__(self):
        return 'Polje(visina={}, sirina={}, pot={})'.format(
            self.visina, self.sirina, self.pot)

    def __str__(self):
        polja = []
        for _ in range(self.visina):
            polja.append(self.sirina * [' '])

        polja[self.visina - 1][0] = str('S')
        polja[0][self.sirina - 1] = str('C')

        self.izbrana_pot = str('*')
            
        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in polja:
            niz += '|'+ ''.join(vrstica) + '|\n'
        return rob + niz + rob

        

        

    def naredi_pot(self, pot, polja):
        smer = random.choice('gor', 'desno')
        if smer == 'gor':
            self.izbrana_pot=polja[self.visina-2][0]
        else:
            self.izbrana_pot=polja[self.visina-1][1]
        

class Pot:

    def __init__(self, polj):
        self.polj = polj
        #kordinate

    def __repr__(self):
        return 'Pot({})'.format(self.dolzina)

print(Polje())
