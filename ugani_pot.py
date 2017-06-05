import random

GOR = 'gor'
DESNO = 'desno'

START = 'S'
CILJ = 'C'

class Polje:

    def __init__(self, visina=10, sirina=10):
        self.visina = visina
        self.sirina = sirina

        self.polja = []
        #self.naredi_pot

          
        

    

    def __repr__(self):
        return 'Polje(visina={}, sirina={}, pot={})'.format(
            self.visina, self.sirina, self.pot)

    def __str__(self):
        
        for _ in range(self.visina):
            self.polja.append(self.sirina * [' '])

        START = self.polja[self.visina - 1][0] = 'S'
        CILJ = self.polja[0][self.sirina - 1]  = 'C'

        
        smer = random.choice([GOR, DESNO])
        if smer == GOR:
            a = self.polja[self.visina-2][0] = '*'
        else:
            a = self.polja[self.visina-1][1] = '*'
        
            
            
        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in self.polja:
            niz += '|'+ ''.join(vrstica) + '|\n'
        return rob + niz + rob

        

        

    #def naredi_pot(self, pot, polja):
        
        

        

class Pot:
    
    def __init__(self, polj):
        self.polj = polj
        #kordinate

    def __repr__(self):
        return 'Pot({})'.format(self.dolzina)

print(Polje())
