from tkinter import *
from tkinter import ttk
from conversor import Conversor


class Interfaz:


    def mostrar(self):
        c=Conversor()

            
        ventana = Tk()
        ventana.title("Convertidor con Python")
        ventana.geometry("600x400")

        e=Label(ventana,text="Convertidor", font=("Verdana",20,"bold"))
        e.pack()

        s=Label(ventana,text="Elige tu archivo")
        s.config(fg="white", bg="red" , width=70)
        s.pack()


        txt = Entry(ventana,width=45)
        txt.config(state="disabled")
        txt.place(x=170,y=210)


        combo_leng=ttk.Combobox(ventana, width=17)


        imgBoton=PhotoImage(file="imagenSinFondo.png" )

        boton=Button(ventana, image=imgBoton, height=120, width=120,command=lambda:c.seleccionarImagen(txt,combo_leng)).place(x=250,y=70)


        combo_leng.place(x=170, y=240)



        Button(ventana, text="Convertir", bg='red', fg="white", width=20, height=1, command=lambda:c.convertirImagen(combo_leng)).place(x=300, y=240)


        l=Label(ventana,text="Elija antes de presionar el botón de convertir", font=("Arial",12)).place(x=150,y=320)

        p=Label(ventana,text="", bg="red",width=62, font=("Arial",10) ).place(x=50,y=350)
        ventana.mainloop()

I=Interfaz()
I.mostrar()

