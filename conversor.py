from PIL import Image # proporciona una clase con el mismo nombre que se utiliza para representar una imagen PIL. 
from tkinter.filedialog import askopenfilename #selecciona la ruta de archivos
from tkinter.filedialog import asksaveasfilename #guarda la ruta de archivos
from tkinter import messagebox as MessageBox #cuadro de dialogo para informar al usuario sobre alguna cuestión
import pathlib #Ofrece un nivel mas alto en la interfaz
import os #El módulo nos permite acceder a funcionalidades dependientes del Sistema Operativo, sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos).

class Conversor: # Clase conversor donde están las funciones correspondientes para realizar la conversion para el tipo de imagen PNG, JPG, GIF y BMP.

    

    def convertirApng(self, rutaOrigen,nombreArchivo): #En este metodo para convertir a png
        imagenIn = Image.open(rutaOrigen) #Abre he identifica el archivo de imagen dado
        rgb_im = imagenIn.convert('RGB')    #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero).
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".png",defaultextension=".png",filetypes = (("png files","*.png"),("all files","*.*")))#Aqui guardamos la ruta del archivo con la extension o tipo de archivo dado

        path = pathlib.Path(rutaDestino)    #Aqui buscamos la ruta del sistema de archivos    
        ext=path.suffix

        if rutaDestino: # Esta es la condicion para que realice la operacion si es png sino botara unos errores o no se realiza la conversion 
            
            if ext == ".png":
                rgb_im.save(rutaDestino, quality=95)                
                os.startfile(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")

    def convertirAjpg(self, rutaOrigen,nombreArchivo): #Este metodo es para convertir la imagen a jpg
        imagenIn = Image.open(rutaOrigen) #Abre e identifica el archivo de imagen dado
        rgb_im = imagenIn.convert('RGB') #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero).
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".jpg",defaultextension=".jpg",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        path = pathlib.Path(rutaDestino)    #Aqui buscamos la ruta del sistema de archivos     
        ext=path.suffix

        if rutaDestino: #Esta es la condicion para que realice la operacion si es jpg sino botara unos errores o no se realiza la conversion
            
            if ext == ".jpg":
                rgb_im.save(rutaDestino, quality=95)                
                os.startfile(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")
           
        
    def convertirAgif(self, rutaOrigen,nombreArchivo):#Este metodo es para convertir la imagen a gif
        imagenIn = Image.open(rutaOrigen) #Abre e identifica el archivo de imagen dado
        rgb_im = imagenIn.convert('RGB') #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero)
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".gif",defaultextension=".gif",filetypes = (("gif files","*.gif"),("all files","*.*")))
        print("hola "+rutaDestino)

        path = pathlib.Path(rutaDestino)       #Aqui buscamos la ruta del sistema de archivos   
        ext=path.suffix

        if rutaDestino: #Esta es la condicion para que realice la operacion si es gif sino botara unos errores o no se realiza la conversion
            
            if ext == ".gif":
                rgb_im.save(rutaDestino, quality=95)                
                os.startfile(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")

        
    def convertirAbmp(self, rutaOrigen,nombreArchivo): #Este metodo es para convertir la imagen a bmp
        imagenIn = Image.open(rutaOrigen) #Abre e identifica el archivo de imagen dado
        rgb_im = imagenIn.convert('RGB') #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero)
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".bmp",defaultextension=".bmp",filetypes = (("bmp files","*.bmp"),("all files","*.*")))

        path = pathlib.Path(rutaDestino)       #Aqui buscamos la ruta del sistema de archivos    
        ext=path.suffix

        if rutaDestino: #Esta es la condicion para que realice la operacion si es gif sino botara unos errores o no se realiza la conversion
            
            if ext == ".bmp":
                rgb_im.save(rutaDestino, quality=95)                
                os.startfile(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")
            


    def seleccionarImagen(self,txt,combo): #Metodo para seleccionar la imagen


        txt.config(state="normal")
        txt.delete(0,"end")
        self.rutaOrigen = askopenfilename(title = "Seleccione la imagen",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("gif files","*.gif"),("bmp files","*.bmp"),("all files","*.*")))# show an "Open" dialog box and return the path to the selected file

        if not self.rutaOrigen:            
            MessageBox.showinfo("Informacion", "No se selecciono ningun archivo")
            txt.config(state="disabled")
            combo['values']=[]

            
        elif self.rutaOrigen != "":            
            txt.insert(0,self.rutaOrigen)
            txt.place(x=170,y=210)
            txt.config(state="readonly")

            self.rutaSinExtension,ext=os.path.splitext(self.rutaOrigen)
            path=pathlib.Path(self.rutaSinExtension)            
            self.nombreArchivo=path.name
            

            if ext == ".jpg":
                opciones=["PNG" , "BMP" , "GIF"]
            elif ext == ".png":
                opciones=["JPG" , "BMP" , "GIF"]
            elif ext == ".gif":
                opciones=["PNG","JPG" , "BMP"]
            elif ext == ".bmp":
                opciones=["GIF","JPG" , "PNG"]

                
            combo['values']=opciones
    
        

    def convertirImagen(self,combo): #Metodo para convertir imagen 

        extAconvertir=combo.get()

        if extAconvertir == "JPG":
            self.convertirAjpg(self.rutaOrigen,self.nombreArchivo)
        elif extAconvertir == "PNG":
            self.convertirApng(self.rutaOrigen,self.nombreArchivo)
            
        elif extAconvertir == "BMP":
            self.convertirAbmp(self.rutaOrigen,self.nombreArchivo)
            
        elif extAconvertir == "GIF":
            self.convertirAgif(self.rutaOrigen,self.nombreArchivo)
            
        else:
            MessageBox.showwarning("Alerta", "No se selecciono ningun archivo o tipo de extension")
        
