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
	
	
	
	
	
						
