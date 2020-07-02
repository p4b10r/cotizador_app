from Tkinter import *
import ttk



#self.pestana=ttk.Notebook(self.wind)
#self.pestana.pack()


class Cotizador:
    def __init__(self, main_window):

        main_window.geometry("500x300")
        self.pestana=ttk.Notebook(main_window)

        self.pestana.pack()

        self.p1=ttk.Frame(main_window)
        self.p2=ttk.Frame(main_window)
        self.pestana.add(self.p1, text="pestana1")
        self.pestana.add(self.p2, text="pestana2")




if __name__=="__main__":
    main_window=Tk()
    app=Cotizador(main_window)

    main_window.mainloop()
