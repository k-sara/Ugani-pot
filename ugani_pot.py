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
    
        
    def nova_igra(self):
        # Ob začetku igre ustvari pot (rešitev)
        seznam = 9*[DESNO] + 9*[GOR]
        random.shuffle(seznam)
        self.resitev = [(self.visina -1, 0)]
        i, j = (self.visina - 1, 0)
        for smer in seznam:
            if smer == GOR:
                i -= 1
            else:
                j += 1
            self.resitev.append((i,j))

        self.korak = 0

    def ugibaj(self, smer):
        if self.korak == 18:
            return None
        #Preveri če si zadel pot ali ne
        i, j = self.resitev[self.korak]
        if smer == GOR and self.resitev[self.korak + 1] == (i - 1, j):
            self.korak += 1
        elif smer == DESNO and self.resitev[self.korak + 1] == (i, j + 1):
            self.korak +=1
        else:
            #zgrešiš
            self.korak = 0
            
        

    

    def __repr__(self):
        return 'Polje(visina={}, sirina={}, pot={})'.format(
            self.visina, self.sirina, self.pot)

    def __str__(self):
        
        for _ in range(self.visina):
            self.polja.append(self.sirina * [' '])

        START = self.polja[self.visina - 1][0] = 'S'
        CILJ = self.polja[0][self.sirina - 1] = 'C'

            
        niz = ''
        rob = '+' + self.sirina * '-' + '+\n'
        for vrstica in self.polja:
            niz += '|'+ ''.join(vrstica) + '|\n'
        return rob + niz + rob



print(Polje())
