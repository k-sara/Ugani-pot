import tkinter as tk
import model

class Pot:
    def __init__(self, okno):
        self.polje = model.Polje(10, 10)

        self.okvir = tk.Frame(okno, height=200, width=200)
        self.okvir.place(x=0,y=0)
        
        self.prikaz_polja = tk.Canvas(self.okvir, height=200 , width=200)
        self.prikaz_polja.place(x=0,y=0)

        
        okno.bind('<Key>', self.tipka)
        

    def narisi(self):
        
        for i in range(self.polje.visina):
            for j in range(self.polje.sirina):
                self.prikaz_polja.create_polygon(20*j+2,20*i+2,20*j+20-2,20*i+2,20*j+20-2,20*i+20-2,20*j+2,20*i+20-2, fill='white')  


        
        i = 0
        j = 9
        self.prikaz_polja.create_polygon(20*j+2,20*i+2,20*j+20-2,20*i+2,20*j+20-2,20*i+20-2,20*j+2,20*i+20-2,fill = 'red')
        self.prikaz_polja.create_text(20*j+10,20*i+10, text='C')

        
        for k in range(self.polje.korak):
            i, j = self.polje.resitev[k]
            self.prikaz_polja.create_polygon(20*j+2,20*i+2,20*j+20-2,20*i+2,20*j+20-2,20*i+20-2,20*j+2,20*i+20-2,fill = 'red')
            
        self.prikaz_polja.create_text(10,20*9+10, text='S')

    def tipka(self, event):
        if event.keysym == 'Right':
            self.polje.ugibaj(model.DESNO)
            self.narisi()
        elif event.keysym == 'Up':
            self.polje.ugibaj(model.GOR)
            self.narisi() 


okno = tk.Tk()
a = Pot(okno)
a.polje.nova_igra()
a.narisi()
okno.mainloop()
