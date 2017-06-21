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
        self.korak = 1
        self.seznam = []
        self.resitev = []
        
        
    def nova_igra(self):
        # Ob začetku igre ustvari pot (rešitev)
        self.seznam = 9*[DESNO] + 9*[GOR]
        random.shuffle(self.seznam)
        self.resitev = [(self.visina -1, 0)]
        i, j = (self.visina - 1, 0)
        for smer in self.seznam:
            if smer == GOR:
                i -= 1
            else:
                j += 1
            self.resitev.append((i,j))



    def ugibaj(self, smer):
        if self.korak == 18:
            return None
        #Preveri če si zadel pot ali ne
        #i, j = self.resitev[self.korak]
        if smer == self.seznam[self.korak]:
            self.korak += 1

        else:
            #zgrešiš
            self.korak = 1
            
        
    

    def __repr__(self):
        return 'Polje(visina={}, sirina={}, resitev={})'.format(
            self.visina, self.sirina, self.resitev)

#    def __str__(self):


#        for _ in range(self.visina):
#           self.polja.append(self.sirina * [' '])

#        START = self.polja[self.visina - 1][0] = 'S'
#        CILJ = self.polja[0][self.sirina - 1] = 'C'

            
#        niz = ''
#        rob = '+' + self.sirina * '-' + '+\n'
#        for vrstica in self.polja:
#            niz += '|'+ ''.join(vrstica) + '|\n'
#        return rob + niz + rob


