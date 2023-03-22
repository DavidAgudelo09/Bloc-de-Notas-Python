import os

from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *


def TdeA():
    showinfo("Estudiantes", "David Agudelo Ardila\nYuli Andrea Silva Muñoz\nAndres Felipe Gomez Marin")


class BlocDeNotas:
    raiz = Tk()

    EsteAncho = 300
    EstaAltura = 300
    AreadeTexto = Text(raiz)
    MenuBar = Menu(raiz)
    MenuArchivo = Menu(MenuBar, tearoff=0)
    MenuEdicion = Menu(MenuBar, tearoff=0)
    MenuAyuda = Menu(MenuBar, tearoff=0)

    BarraDeDesplazamiento = Scrollbar(AreadeTexto)
    archivo = None

    def __init__(self, **kwargs):

        try:
            self.raiz.wm_iconbitmap("Notepad.ico")
        except:
            pass

        try:
            self.EsteAncho = kwargs['width']
        except KeyError:
            pass

        try:
            self.EstaAltura = kwargs['height']
        except KeyError:
            pass

        self.raiz.title("Sin título: Bloc de Notas")

        AnchodePantalla = self.raiz.winfo_screenwidth()
        AlturadePantalla = self.raiz.winfo_screenheight()

        left = (AnchodePantalla / 2) - (self.EsteAncho / 2)

        top = (AlturadePantalla / 2) - (self.EstaAltura / 2)

        self.raiz.geometry('%dx%d+%d+%d' % (self.EsteAncho,
                                            self.EstaAltura,
                                            left, top))

        self.raiz.grid_rowconfigure(0, weight=1)
        self.raiz.grid_columnconfigure(0, weight=1)

        self.AreadeTexto.grid(sticky=N + E + S + W)

        self.MenuArchivo.add_command(label="Nuevo",
                                     command=self.ArchivoNuevo)

        self.MenuArchivo.add_command(label="Abrir",
                                     command=self.AbrirDocumento)

        self.MenuArchivo.add_command(label="Guardar",
                                     command=self.GuardarArchivo)

        self.MenuArchivo.add_separator()
        self.MenuArchivo.add_command(label="Salir",
                                     command=self.SalirAplicacion)
        self.MenuBar.add_cascade(label="Archivo",
                                 menu=self.MenuArchivo)

        self.MenuEdicion.add_command(label="Cortar",
                                     command=self.cortar)

        self.MenuEdicion.add_command(label="Copiar",
                                     command=self.copiar)

        self.MenuEdicion.add_command(label="Pegar",
                                     command=self.pegar)

        self.MenuBar.add_cascade(label="Edición",
                                 menu=self.MenuEdicion)

        self.MenuAyuda.add_command(label="Creadores",
                                   command=TdeA)
        self.MenuBar.add_cascade(label="TdeA",
                                 menu=self.MenuAyuda)

        self.raiz.config(menu=self.MenuBar)

        self.BarraDeDesplazamiento.pack(side=RIGHT, fill=Y)

        self.BarraDeDesplazamiento.config(command=self.AreadeTexto.yview)
        self.AreadeTexto.config(yscrollcommand=self.BarraDeDesplazamiento.set)

    def SalirAplicacion(self):
        self.raiz.destroy()

    def AbrirDocumento(self):

        self.archivo = askopenfilename(defaultextension=".txt",
                                       filetypes=[("Todos los archivos", "*.*"),
                                                  ("Documentos de texto", "*.txt")])

        if self.archivo == "":

            self.archivo = None
        else:

            self.raiz.title(os.path.basename(self.archivo) + " - Bloc de Notas")
            self.AreadeTexto.delete(1.0, END)

            file = open(self.archivo, "r")

            self.AreadeTexto.insert(1.0, file.read())

            file.close()

    def ArchivoNuevo(self):
        self.raiz.title("Sin título: Bloc de Notas")
        self.archivo = None
        self.AreadeTexto.delete(1.0, END)

    def GuardarArchivo(self):

        if self.archivo is None:

            self.archivo = asksaveasfilename(initialfile='SinTitulo.txt',
                                             defaultextension=".txt",
                                             filetypes=[("Todos los archivos", "*.*"),
                                                        ("Documentos de texto", "*.txt")])

            if self.archivo == "":
                self.archivo = None
            else:

                file = open(self.archivo, "w")
                file.write(self.AreadeTexto.get(1.0, END))
                file.close()

                self.raiz.title(os.path.basename(self.archivo) + " - Bloc de Notas")


        else:
            file = open(self.archivo, "w")
            file.write(self.AreadeTexto.get(1.0, END))
            file.close()

    def cortar(self):
        self.AreadeTexto.event_generate("<<Cut>>")

    def copiar(self):
        self.AreadeTexto.event_generate("<<Copy>>")

    def pegar(self):
        self.AreadeTexto.event_generate("<<Paste>>")

    def correr(self):

        self.raiz.mainloop()


blocdenotas = BlocDeNotas(width=600, height=400)
blocdenotas.correr()
