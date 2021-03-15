from tkinter import *
from tkinter import ttk
from arqui.conversor import Conversor


class Interfaz:


    def mostrar(self):
        c=Conversor()

            
        ventana = Tk()
        ventana.title("Convertidor De Imagenes Python")
        ventana.geometry("550x330")

        e=Label(ventana,text="Convertidor", font=("Verdana",20,"bold"))
        e.pack()

        s=Label(ventana,text="Elige tu archivo")
        s.config(fg="white", bg="red" , anchor="center")
        s.pack()
        s.place(x=150,y=45)


        txt = Entry(ventana,width=42)
        txt.config(state="disabled")
        txt.place(x=120,y=210)


        combo_leng=ttk.Combobox(ventana, width=17)


        imgBoton=PhotoImage(file="arqui/imagenSinFondo.png" )

        boton=Button(ventana, image=imgBoton, height=120, width=120,command=lambda:c.seleccionarImagen(txt,combo_leng)).place(x=250,y=70)


        combo_leng.place(x=120, y=240)



        Button(ventana, text="Convertir", bg='red', fg="white", width=20, height=1, command=lambda:c.convertirImagen(combo_leng)).place(x=300, y=240)



        p=Label(ventana,text="Elija antes de presionar el botón de convertir")
        p.config(fg="white", bg="red" ,anchor="center")
        
        p.pack()
        p.place(x=150,y=290)
        ventana.mainloop()



