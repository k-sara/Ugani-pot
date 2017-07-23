import tkinter as tk
import model

class Pot:
    def __init__(self, okno):
        self.polje = model.Polje(10, 10)
        
        self.okno = okno
        self.okvir = tk.Frame(okno, height=400, width=400)
        self.okvir.grid(row=0, column=0)
        
        self.prikaz_polja = tk.Canvas(self.okvir, height=200, width=200)
        self.prikaz_polja.grid(row=0, column=0)

        self.okno.bind('<Key>', self.tipka)

        def gumb_nova_igra():
            self.polje.korak = 0
            self.polje.stevec = 0
            self.polje.nova_igra()
            self.narisi()
            
        gumb = tk.Button(self.okvir, text='NOVA IGRA', height=2, width=10,
                         command=gumb_nova_igra)
        gumb.grid(row=0, column=1)

        self.stevilo_poskusov = tk.Label(self.okvir, text='Število poskusov:')
        self.stevilo_poskusov.grid(row=1, column=0)

        self.stevilo_poskusov = tk.Label(self.okvir,
                                         text=' 0 ',
                                         bg='black',
                                         fg='white',
                                         relief='raised')
        self.stevilo_poskusov.grid(row=1, column=1)

        self.ime_igralca = tk.Label(self.okvir,text='Ime:')
        self.ime_igralca.grid(row=2, column=0)
        
        self.ime_igralca = tk.Entry(self.okvir, bg='white')
        self.ime_igralca.grid(row=2, column=1)

        self.posodobi_poskuse() 
     
    def posodobi_poskuse(self):
        self.stevilo_poskusov.configure(text=str(self.polje.stevec))
    
    def narisi(self):
        #Nariše kvadratke
        for i in range(self.polje.visina):
            for j in range(self.polje.sirina):
                self.prikaz_polja.create_polygon(20*j+2,20*i+2,
                                                 20*j+20-2,20*i+2,
                                                 20*j+20-2,20*i+20-2,
                                                 20*j+2,20*i+20-2,
                                                 fill='white')  

        #Cilj
        i = 0
        j = 9
        self.prikaz_polja.create_polygon(20*j+2,20*i+2,
                                         20*j+20-2,20*i+2,
                                         20*j+20-2,20*i+20-2,
                                         20*j+2,20*i+20-2,
                                         fill = 'red')
        self.prikaz_polja.create_text(20*j+10,20*i+10, text='C')

        #Start
        i = 9
        j = 0
        self.prikaz_polja.create_polygon(20*j+2,20*i+2,
                                         20*j+20-2,20*i+2,
                                         20*j+20-2,20*i+20-2,
                                         20*j+2,20*i+20-2,
                                         fill = 'red')        
        self.prikaz_polja.create_text(10,20*9+10, text='S')

        for k in range(self.polje.korak):
            #Rdeče obarva že zadete kvadratke
            i, j = self.polje.resitev[k]
            self.prikaz_polja.create_polygon(20*j+2, 20*i+2,
                                             20*j+20-2, 20*i+2,
                                             20*j+20-2, 20*i+20-2,
                                             20*j+2, 20*i+20-2,
                                             fill = 'red')
            
        if self.polje.korak == 18:
            #Ko pot pride do Cilja, se rezultat potez shrani, mreža s kvadratki
            #pa izgine.
            self.shrani_rezultat()
            self.prikaz_polja.delete('all')

        self.posodobi_poskuse()

    def tipka(self, event):
        if event.keysym == 'Right':
            self.polje.ugibaj(model.DESNO)
            self.narisi()
        elif event.keysym == 'Up':
            self.polje.ugibaj(model.GOR)
            self.narisi()

    def shrani_rezultat(self):
        with open('rezultati.txt', 'a') as datoteka:
            print(self.ime_igralca.get(), str(self.polje.stevec),
                  file=datoteka)



okno = tk.Tk()
igra = Pot(okno)
igra.polje.nova_igra()
igra.narisi()
okno.mainloop()
