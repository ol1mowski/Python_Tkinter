import tkinter as tk

class Aplikacja:
    
    def __init__(self, okno):
        #Zmienne Tekst
        self.tekst1 = tk.StringVar()
        self.tekst2 = tk.StringVar()
        #Label 1
        self.label101 = tk.Label(okno, text="Podaj liczbę")
        self.label101.grid(row=0, column=0)
        #Wejście od user
        self.enter01 = tk.Entry(okno, textvariable=self.tekst1, font=('none',9,'italic'))
        self.enter01.grid(row=0, column=1)
        #Przycisk 1
        self.b1 = tk.Button(okno, text="Przekaż liczbę", command=lambda: self.zmien_tekst(self.label03, self.tekst1, "Podana liczba: "))
        self.b1.grid(row=0, column=2)
        #label 2
        self.label02 = tk.Label(okno, text="Podaj hasło")
        self.label02.grid(row=1, column=0)
        #Drugi wejście
        self.entry02 = tk.Entry(okno, textvariable=self.tekst2, show="*")
        self.entry02.grid(row=1, column=1)
        #Przycisk 2
        self.b1 = tk.Button(okno, text="Przkaż hasło", command=lambda: self.zmien_tekst(self.label04, self.tekst2, "Hasło to: "))
        self.b1.grid(row=1, column=2)
        #label 3
        self.label03 = tk.Label(okno, text="Tu będzie podany przez Ciebie tekst")
        self.label03.grid(row=2, column=1)
        #label 4
        self.label04 = tk.Label(okno, text="Tu będzie podane przez Ciebie hasło")
        self.label04.grid(row=3, column=1)
    
    def zmien_tekst(self, label, textvar, text):
        label.config(text=(str(text)+ str(textvar.get())))
        
okno = tk.Tk()
okno.title("Aplikacja")
okno.geometry("300x400")
okno.resizable(False, False)
app = Aplikacja(okno)
okno.mainloop()