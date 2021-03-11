  **PYTHON CONVERSOR_ESCRITORIO** 
 
  * Librerias Importadas
  		
      * *PIL
      *  La biblioteca de imágenes de Python agrega capacidades de procesamiento de imágenes al intérprete de Python.Esta biblioteca proporciona un amplio 
      	 soporte de formato de archivo, una representación interna eficiente y capacidades de procesamiento de imágenes bastante potentes.La biblioteca de 
         imágenes principal está diseñada para un acceso rápido a los datos almacenados en algunos formatos de píxeles básicos. Debe proporcionar una base 
         sólida para una herramienta general de procesamiento de imágenes.
         
         Para instalar pillow en nuestra aplicación de python utilizamos el comando **pip install pillow**. La libreria pillow se utilizo para convertir las 
	 extensiónes de JPG, PNG, BMP, GIF
      
       * *TKINTER
       * Es una libreria grafica TcL/tk para el lenguaje de programación python. Se considera un estandar para la interfaz grafica de usuario(GUI) y es el que
         viene por defecto para python para microsoft windows 
      
     	* **Comentarios Código Aplicación Shell Lenguaje Python

	**from PIL import Image** en esta linea de codigo se esta importando la libreria Pil la cual se trabajara en el backend de la aplicación, 
     	**from tkinter.filedialog import askopenfilename** selecciona la ruta de archivos
	**from tkinter.filedialog import asksaveasfilename** guarda la ruta de archivos
	**from tkinter import messagebox as MessageBox** cuadro de dialogo para informar al usuario sobre alguna cuestión
	**import pathlib** Ofrece un nivel mas alto en la interfaz
	**import os** El módulo nos permite acceder a funcionalidades dependientes del Sistema Operativo, sobre todo, aquellas que nos refieren 
	información sobre el entorno del mismo y nos permiten manipular la estructura de directorios (para leer y escribir archivos).
	
	Clase donde están las funciones correspondientes para realizar la conversion para el tipo de imagen PNG, JPG, GIF y BMP.
	
	
	**Metodos que se trabajaran en la clase Conversor 
	
	*convertirApng
	*convertirAjpg
	*convertirAgif
	*convertirAbmp
	*seleccionarImagen
	*convertirImagen
	
	**Metodo de convertir a PNG (convertirApng)
	
		def convertirApng(self, rutaOrigen,nombreArchivo): #En este metodo para convertir a png
     			imagenIn = Image.open(rutaOrigen) #Abre he identifica el archivo de imagen dado
        	   	rgb_im = imagenIn.convert('RGB')    #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero).
        		rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".png",defaultextension=".png",filetypes = (("png 			       files","*.png"),("all files","*.*")))#Aqui guardamos la ruta del archivo con la extension o tipo de archivo dado

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
	
	**Metodo de convertir a JPG (convertirAjpg)
	
		def convertirAjpg(self, rutaOrigen,nombreArchivo): #Este metodo es para convertir la imagen a jpg
       			imagenIn = Image.open(rutaOrigen) #Abre e identifica el archivo de imagen dado
        		rgb_im = imagenIn.convert('RGB') #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero).
        		rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".jpg",defaultextension=".jpg",filetypes =(("jpeg 			       files","*.jpg"),("all files","*.*")))

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
			
	**Metodo de convertir a BMP (convertirAbmp)
	
		def convertirAbmp(self, rutaOrigen,nombreArchivo): #Este metodo es para convertir la imagen a bmp
        		imagenIn = Image.open(rutaOrigen) #Abre e identifica el archivo de imagen dado
        		rgb_im = imagenIn.convert('RGB') #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero)
        		rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".bmp",defaultextension=".bmp",filetypes = (("bmp 				files","*.bmp"),("all files","*.*")))

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
	
	**Metodo de convertir a GIF (convertirAgif)
	
	 	def convertirAgif(self, rutaOrigen,nombreArchivo):#Este metodo es para convertir la imagen a gif
        		imagenIn = Image.open(rutaOrigen) #Abre e identifica el archivo de imagen dado
        		rgb_im = imagenIn.convert('RGB') #El modo de la imagen se convierte a RGB (Píxeles de 3x8 bits, color verdadero)
       			rutaDestino = asksaveasfilename(title = "Seleccione donde guardar",initialfile=nombreArchivo+".gif",defaultextension=".gif",filetypes = (("gif 			       files","*.gif"),("all files","*.*")))
			
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
