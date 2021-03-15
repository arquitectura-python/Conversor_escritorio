from PIL import Image
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox as MessageBox
import pathlib
import os,sys, subprocess

class Conversor:


    

    def abrirArchivo(self,ruta):
        if sys.platform == "win32":
            os.startfile(ruta)
        elif sys.platform == "linux":
            subprocess.call(["xdg-open", ruta])

    def convertirApng(self, rutaOrigen,nombreArchivo):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')    
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".png",defaultextension=".png",filetypes = (("png files","*.png"),("all files","*.*")))

        path = pathlib.Path(rutaDestino)        
        ext=path.suffix

        if rutaDestino:
            
            if ext == ".png":
                rgb_im.save(rutaDestino, quality=95)                
                self.abrirArchivo(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")

    def convertirAjpg(self, rutaOrigen,nombreArchivo):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".jpg",defaultextension=".jpg",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))

        path = pathlib.Path(rutaDestino)        
        ext=path.suffix

        if rutaDestino:
            
            if ext == ".jpg":
                rgb_im.save(rutaDestino, quality=95)                
                self.abrirArchivo(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")
           
        
    def convertirAgif(self, rutaOrigen,nombreArchivo):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".gif",defaultextension=".gif",filetypes = (("gif files","*.gif"),("all files","*.*")))

        path = pathlib.Path(rutaDestino)        
        ext=path.suffix

        if rutaDestino:
            
            if ext == ".gif":
                rgb_im.save(rutaDestino, quality=95)                
                self.abrirArchivo(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")

        
    def convertirAbmp(self, rutaOrigen,nombreArchivo):
        imagenIn = Image.open(rutaOrigen)
        rgb_im = imagenIn.convert('RGB')
        rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".bmp",defaultextension=".bmp",filetypes = (("bmp files","*.bmp"),("all files","*.*")))

        path = pathlib.Path(rutaDestino)        
        ext=path.suffix

        if rutaDestino:
            
            if ext == ".bmp":
                rgb_im.save(rutaDestino, quality=95)                
                self.abrirArchivo(rutaDestino)
                
            else:
                MessageBox.showerror("Error", "Ha ocurrido un error por favor no modifique la extension.")

        else:
            MessageBox.showinfo("Informacion", "No se convirtio la imagen")
            


    def seleccionarImagen(self,txt,combo):


        txt.config(state="normal")
        txt.delete(0,"end")
        self.rutaOrigen = askopenfilename(title = "Seleccione la imagen",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("gif files","*.gif"),("bmp files","*.bmp"),("all files","*.*")))# show an "Open" dialog box and return the path to the selected file

        if not self.rutaOrigen:            
            MessageBox.showinfo("Informacion", "No se selecciono ningun archivo")
            txt.config(state="disabled")
            combo['values']=[]

            
        elif self.rutaOrigen != "":            
            txt.insert(0,self.rutaOrigen)
            txt.place(x=120,y=210)
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
    
        

    def convertirImagen(self,combo):

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
        
