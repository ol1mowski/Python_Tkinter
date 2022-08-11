import tkinter as tk

class Aplikacja:
    
    def __init__(self, okno):
        self.entry01 = tk.Entry(okno, textvariable="")
        self.entry01.grid(row=1, column=1)
        
        self.entry02 = tk.Entry(okno, textvariable="")
        self.entry02.grid(row=1, column=2)
        
        self.bk1 = tk.Button(okno, text="+", command=lambda: self.klik(self.entry02.get()))
        self.bk1.grid(row=2, column=2)
        
        self.bk2 = tk.Button(okno, text="-")
        self.bk2.grid(row=4, column=2)
        
        self.bk3 = tk.Button(okno, text="/")
        self.bk3.grid(row=6, column=2)
        
        self.bk4 = tk.Button(okno, text="*")
        self.bk4.grid(row=8, column=2)
        
        self.entry03 = tk.Entry(okno, textvariable="")
        self.entry03.grid(row=1, column=3)
        
        self.b1 = tk.Button(okno, text="Oblicz", command=lambda: self.oblicz(self.label01, self.entry01.get(), self.entry02.get(), self.entry03.get()))
        self.b1.grid(row=10, column=2)
        
        self.label01 = tk.Label(okno, text="Tu będzie twój wynik")
        self.label01.grid(row=12, column=2)
        
    def oblicz(self, label, liczba1, rodzaj, liczba2):
        if rodzaj == "+":
            label.config(text=int(liczba1) + int(liczba2))
        elif rodzaj == "-":
            label.config(text=int(liczba1) - int(liczba2))
        elif rodzaj == "/":
            label.config(text=float(liczba1) / float(liczba2))
        elif rodzaj == "*":
            label.config(text=int(liczba1) * int(liczba2))
            
            
    def klik(self, rodzaj):
        rodzaj == "+"
        
    
okno = tk.Tk()
okno.geometry("350x400")
okno.title("App")
okno.resizable(False, False)
app = Aplikacja(okno)
okno.mainloop()