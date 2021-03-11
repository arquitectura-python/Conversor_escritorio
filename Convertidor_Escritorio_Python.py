from tkinter import *  # se importa la liberia tkinter para GUI
from tkinter import ttk  # proporciona acceso al conjunto de widgets
from conversor import Conversor #Se importa la clase conversor que vamos a utilizar en la clase interfaz


class Interfaz: #nombre de la clase 


    def mostrar(self): # Aqui se crean los objetos y las funciones definidas por el usuario
        c=Conversor()# Metodo de la clase conversor 

            
        ventana = Tk() # Aqui creamos la ventana GUI
        ventana.title("Convertidor con Python") #Aqui le damos el titulo a la ventana 
        ventana.geometry("600x400") #Con esto le damos la altura y el ancho a la ventana

        e=Label(ventana,text="Convertidor", font=("Verdana",20,"bold")) # Este label se utiliza para darle un nombre al programa en la interfaz, se le da un tipo de letra y su tamaño
        e.pack() # Sirve para posicionar el elemento en el primer espacio que encuentre

        s=Label(ventana,text="Elige tu archivo") # label donde se muestra la opcion de elegir el archivo 
        s.config(fg="white", bg="red" , width=70) # Aqui le damos un color de fondo al label y color de letra y el ancho
        s.pack() # Se ubica debajo del anterior ubicacion que se le dio al label


        txt = Entry(ventana,width=45) # Este txt es donde va la direccion del archivo 
        txt.config(state="disabled")  # Para cambiar el estado del txt
        txt.place(x=170,y=210) # Para la ubicacion del txt


        combo_leng=ttk.Combobox(ventana, width=17) # Aqui creamos el combobox y le damos el ancho 


        imgBoton=PhotoImage(file="imagenSinFondo.png" ) #Esta opcion sirve para colocar la imagen que vamos a mostrar en la interfaz GUI 

        boton=Button(ventana, image=imgBoton, height=120, width=120,command=lambda:c.seleccionarImagen(txt,combo_leng)).place(x=250,y=70) # Esta linea es para volver la imagen en el boton con su respectivo comando que va a seleccionar la imagen de su pc


        combo_leng.place(x=170, y=240)# Para la ubicacion del combobox



        Button(ventana, text="Convertir", bg='red', fg="white", width=20, height=1, command=lambda:c.convertirImagen(combo_leng)).place(x=300, y=240)#Aqui creamos el boton para convertir con su respectiva funcion, le damos el ancho y la ubicacion


        l=Label(ventana,text="Elija antes de presionar el botón de convertir", font=("Arial",12)).place(x=150,y=320)# Este label es para dar informacion sobre lo que tiene que hacer anteriormmente y se le da un tipo de letra, tamaño y ubicacion 

        p=Label(ventana,text="", bg="red",width=62, font=("Arial",10) ).place(x=50,y=350)#Aqui un label para el diseño
        ventana.mainloop() #Indica a la interfaz para que se quede esperando a que el usuario haga algo 

I=Interfaz() #Aqui invocamos la clase
I.mostrar() # invocamos el metodo de la clase interfaz

