import numpy as np
from tkinter import *
import tkinter.messagebox


class CardanoSolver:
    """Solver pentru ecuatii de gradul III folosind metoda lui Cardano."""

    @staticmethod
    def solve(a, b, c, d):
        """Calculeaza radacinile ecuatiei de gradul III."""
        p = complex((3 * a * c - b ** 2) / (3 * a ** 2))
        q = complex((2 * b ** 3 - 9 * a * b * c + 27 * a ** 2 * d) / (27 * a ** 3))
        delta = complex((q ** 2 / 4 + p ** 3 / 27))

        if delta.real > 0:
            u = (-q / 2 + np.sqrt(delta)) ** (1 / 3)
            v = (-q / 2 - np.sqrt(delta)) ** (1 / 3)
            x1 = u + v - b / (3 * a)
            x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * np.sqrt(3) / 2j
            x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * np.sqrt(3) / 2j
        elif delta.real == 0:
            u = (-q / 2) ** (1 / 3)
            x1 = 2 * u - b / (3 * a)
            x2 = -u - b / (3 * a)
            x3 = x2
        else:
            u = (-q / 2 + np.sqrt(delta)) ** (1 / 3)
            v = (-q / 2 - np.sqrt(delta)) ** (1 / 3)
            x1 = u + v - b / (3 * a)
            x2 = -(u + v) / 2 - b / (3 * a) + (u - v) * np.sqrt(3) / 2j
            x3 = -(u + v) / 2 - b / (3 * a) - (u - v) * np.sqrt(3) / 2j

        roots = sorted([x1, x2, x3], key=lambda x: (x.real, x.imag))
        return roots


class App:
    """Aplicatia grafica pentru rezolvarea ecuatiilor de gradul III."""

    def __init__(self, root):
        self.root = root
        self.root.title("Ecuatii de Gradul III")
        self.root.geometry("1000x700+0+0")
        self.root.configure(bg="#ffcccc")

        self.A = StringVar()
        self.B = StringVar()
        self.C = StringVar()
        self.D = StringVar()
        self.Sol1 = StringVar()
        self.Sol2 = StringVar()
        self.Sol3 = StringVar()

        self.setup_ui()

    def setup_ui(self):
        """Seteaza interfata grafica."""
        frmPrincipal = Frame(self.root, bd=10, width=800, bg="#ffcccc")
        frmPrincipal.grid()

        frmGrafic = Frame(frmPrincipal, bd=10, width=300, relief=RIDGE, bg="#ffcccc")
        frmGrafic.grid(row=0, column=0, padx=10, pady=10)

        lblGrafic = LabelFrame(frmGrafic, bd=10, width=300, height=600, font=('Helvetica', 12, 'bold'),
                               text='Grafic', relief=RIDGE, bg="#ffcccc")
        lblGrafic.pack(side=TOP, padx=10, pady=10)

        self.cnvPanza = Canvas(lblGrafic, width=275, height=560, bg="white")
        self.cnvPanza.pack()

        frmDateSolutiiOptiuni = Frame(frmPrincipal, bd=10, width=300, relief=RIDGE, bg="#ffcccc")
        frmDateSolutiiOptiuni.grid(row=0, column=1, padx=10, pady=10)

        lblDate = LabelFrame(frmDateSolutiiOptiuni, bd=10, width=300, height=150, font=('Helvetica', 12, 'bold'),
                             text='Date', relief=RIDGE, bg="#ffcccc")
        lblDate.pack(side=TOP, padx=10, pady=10)

        lblSolutii = LabelFrame(frmDateSolutiiOptiuni, bd=10, width=300, height=150, font=('Helvetica', 12, 'bold'),
                                text='Solutii', relief=RIDGE, bg="#ffcccc")
        lblSolutii.pack(side=TOP, padx=10, pady=10)

        lblOptiuni = LabelFrame(frmDateSolutiiOptiuni, bd=10, width=300, height=150, font=('Helvetica', 12, 'bold'),
                                text='Optiuni', relief=RIDGE, bg="#ffcccc")  
        lblOptiuni.pack(side=TOP, padx=10, pady=10)

        self.create_widgets(lblDate, lblSolutii, lblOptiuni)

    def create_widgets(self, lblDate, lblSolutii, lblOptiuni):
        """Creeaza widgeturile din aplicatie."""
        Label(lblDate, font=('Helvetica', 16, 'bold'), text="a=", bd=7, bg="#ffcccc").grid(row=0, column=0,
                                                                                           sticky=W)
        Entry(lblDate, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.A, width=34).grid(row=0, column=1)

        Label(lblDate, font=('Helvetica', 16, 'bold'), text="b=", bd=7, bg="#ffcccc").grid(row=1, column=0,
                                                                                           sticky=W)
        Entry(lblDate, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.B, width=34).grid(row=1, column=1)

        Label(lblDate, font=('Helvetica', 16, 'bold'), text="c=", bd=7, bg="#ffcccc").grid(row=2, column=0,
                                                                                           sticky=W)
        Entry(lblDate, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.C, width=34).grid(row=2, column=1)

        Label(lblDate, font=('Helvetica', 16, 'bold'), text="d=", bd=7, bg="#ffcccc").grid(row=3, column=0,
                                                                                           sticky=W)
        Entry(lblDate, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.D, width=34).grid(row=3, column=1)

        Label(lblSolutii, font=('Helvetica', 16, 'bold'), text="x1=", bd=7, bg="#ffcccc").grid(row=0, column=0,
                                                                                                   sticky=W)
        Entry(lblSolutii, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.Sol1, width=34,
              state=DISABLED).grid(row=0, column=1, padx=8, pady=8)

        Label(lblSolutii, font=('Helvetica', 16, 'bold'), text="x2=", bd=7, bg="#ffcccc").grid(row=1, column=0,
                                                                                                   sticky=W)
        Entry(lblSolutii, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.Sol2, width=34,
              state=DISABLED).grid(row=1, column=1, padx=8, pady=8)

        Label(lblSolutii, font=('Helvetica', 16, 'bold'), text="x3=", bd=7, bg="#ffcccc").grid(row=2, column=0,
                                                                                                   sticky=W)
        Entry(lblSolutii, font=('Helvetica', 13, 'bold'), bd=7, textvariable=self.Sol3, width=34,
              state=DISABLED).grid(row=2, column=1, padx=8, pady=8)

        # Modificare ordine butoane
        Button(lblOptiuni, padx=18, bd=7, font=('Helvetica', 16, 'bold'), width=10, command=self.iesire,
               text="Iesire",
               bg="#ff6f61").grid(row=0, column=0, pady=12)
        Button(lblOptiuni, padx=18, bd=7, font=('Helvetica', 16, 'bold'), width=10, command=self.reset,
               text="Resetare",
               bg="#ffa500").grid(row=0, column=1, pady=12)
        Button(lblOptiuni, padx=18, bd=7, font=('Helvetica', 16, 'bold'), width=10, command=self.calculeaza,
               text="Calculeaza", bg="#ffcccc").grid(row=0, column=2, pady=12)

    def reset(self):
        """Resetează valorile din câmpurile de intrare și ieșire."""
        self.A.set("")
        self.B.set("")
        self.C.set("")
        self.D.set("")
        self.Sol1.set("")
        self.Sol2.set("")
        self.Sol3.set("")

    def iesire(self):
        """Închide aplicația."""
        q = tkinter.messagebox.askyesno("Confirmare", "Sunteți sigur că doriți să părăsiți aplicația?")
        if q > 0:
            self.root.destroy()

    def calculeaza(self):
        """Calculează soluțiile ecuației de gradul III și desenează graficul."""
        a = self.A.get()
        b = self.B.get()
        c = self.C.get()
        d = self.D.get()
        try:
            a = complex(a)
            b = complex(b)
            c = complex(c)
            d = complex(d)
            sol1, sol2, sol3 = CardanoSolver.solve(a, b, c, d)
            self.Sol1.set(sol1)
            self.Sol2.set(sol2)
            self.Sol3.set(sol3)
            self.deseneaza_grafic(a, b, c, d)
        except ValueError:
            tkinter.messagebox.showwarning("Eroare", "Valorile introduse trebuie să fie numere complexe")
            self.reset()

    def deseneaza_grafic(self, a, b, c, d):
        """Desenează graficul ecuației de gradul III."""
        self.cnvPanza.delete("all")
        panWidth = 275
        panHeight = 560
        valoriX = np.linspace(-3, 4, 1000)
        valoriY = a * valoriX ** 3 + b * valoriX ** 2 + c * valoriX + d
        valxScalate = ((valoriX - min(valoriX)) / (max(valoriX) - min(valoriX)) * panWidth).astype(int)
        valyScalate = ((valoriY - min(valoriY)) / (max(valoriY) - min(valoriY)) * panHeight).astype(int)
        for i in range(len(valxScalate) - 1):
            self.cnvPanza.create_line(valxScalate[i], panHeight - valyScalate[i], valxScalate[i + 1],
                                       panHeight - valyScalate[i + 1], fill='blue', width=2)
        self.cnvPanza.create_line(0, panHeight / 2, panWidth, panHeight / 2, fill='black', width=1)
        self.cnvPanza.create_line(panWidth / 2, 0, panWidth / 2, panHeight, fill='black', width=1)


if __name__ == '__main__':
    root = Tk()
    application = App(root)
    root.mainloop()

