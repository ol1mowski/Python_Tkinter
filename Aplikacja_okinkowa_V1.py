import tkinter as tk

class Aplikacja:
   
    def __init__(self, okno):
        #zmienna tekst
        self.tekst = tk.StringVar()
        self.tekst.set("Witaj")
        #Pierwszy napis
        self.label101 = tk.Label(okno, textvariable=self.tekst)
        self.label101.grid(row=0, column=0)
        #Pierwszy przycisk
        self.b1 = tk.Button(okno, text="Przycisk nr 1", command=self.zmien_tekst)
        self.b1.grid(row=0, column=1)
        #Drugi napis
        self.label102 = tk.Label(okno, text="Zmień mnie")
        self.label102.grid(row=1, column=0)
        #Drugi przycisk
        self.b1 = tk.Button(okno, text="Przycisk nr 2", command=lambda: self.zmien_tekst_w(self.label102))
        self.b1.grid(row=1, column=1)
    def zmien_tekst(self):
        self.tekst.set("Tekst został zmieniony")
        
    def zmien_tekst_w(self, label):
        label.config(text="Tekst został zmieniony 2")
                   
okno = tk.Tk()
okno.title("Aplikacja")
okno.geometry("300x400")
okno.resizable(False, False)

app = Aplikacja(okno)

okno.mainloop()  