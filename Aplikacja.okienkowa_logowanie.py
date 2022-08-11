import tkinter as tk
from time import sleep

#Słownik
a = {"admin": "123", "user": "haslo"}

class EntryRozszerzone(tk.Entry):
    #konstruktor klasy
    def __init__(self, master=None, tekst_zastepczy="podaj liczbe", color="grey"):
        super().__init__(master, width=26)
        
        #Zmienna wyświetlająca siegdy input jest pusty
        self.tekst_zastepczy = tekst_zastepczy
        self.tekst_zastepczy_color = color
        self.default_fg_color = self['fg']

        #Sprawdzenire czy user wcisnął coś
        self.bind("<Key>", self.foc_in)
        
        #Sprawdzenire czy user opuścił pole
        self.bind("<Leave>", self.foc_out)
        
        self.put_tekst_zastepczy()
        
    def put_tekst_zastepczy(self):
        self.delete('0', 'end')
        self.insert(0, self.tekst_zastepczy)
        self['fg'] = self.tekst_zastepczy_color
    
    def foc_in(self, *args):
        if self['fg'] == self.tekst_zastepczy_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color
    
    def foc_out(self, *args):
        if not self.get():
            self.put_tekst_zastepczy()
            
#Klasa Tkinter            
class Aplikacja:

    def __init__(self, okno):

        #Puste elementy
        self.label01 = tk.Label(okno, text="            ")
        self.label01.grid(row=0, column=0)
        self.label01 = tk.Label(okno, text="            ")
        self.label01.grid(row=2, column=0)
        self.label01 = tk.Label(okno, text="            ")
        self.label01.grid(row=4, column=0)
        self.label01 = tk.Label(okno, text="            ")
        self.label01.grid(row=6, column=0)
        
        #Wejście User na nazwę
        self.enter01 = EntryRozszerzone(okno, tekst_zastepczy="Podaj nazwę użytkownika: ",)
        self.enter01.grid(row=1, column=1)
        
        #Hasło
        self.enter02 = EntryRozszerzone(okno, tekst_zastepczy="Podaj Hasło: ")
        self.enter02.grid(row=3, column=1)
        
        #Przycisk z wywołaniem metody
        self.b1 = tk.Button(okno, text="Zaloguj się", command=lambda: self.zmien_tekst(self.label01, self.enter01.get(), self.enter02.get()))
        self.b1.grid(row=5, column=1)
        
        #Tekst 1
        self.label01 = tk.Label(okno, text="Czekam na zalogowanie")
        self.label01.grid(row=7, column=1)
        
    def zmien_tekst(self, label, user, passwd):
        if user in a:
            pass
            if passwd == a[user]:
                sleep(1)
                label.config(text="Użytkownik zalogowany")
            else:
                sleep(1)
                label.config(text="Złe hasło")
        else:
            sleep
            label.config(text="Użytkownik nie istnieje")
                   
okno = tk.Tk()
okno.title("Aplikacja")
okno.geometry("300x400")
okno.resizable(False, False)

app = Aplikacja(okno)

okno.mainloop()  