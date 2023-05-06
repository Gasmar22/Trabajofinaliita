import tkinter as tk
import enviarcorreo as correo
import ARCHIVO_PRECIOS as precios
from ARCHIVO_PRECIOS import LeerArchivoPrecios

# creamos la ventana=root
root = tk.Tk()
root.title("Toxicase iPhone")
root.geometry('1080x600+1200+100')
root.configure(background='gold')
root.iconbitmap("applelogo.ico")

# TITULO 

label4 = tk.Label(root,text="¡BIENVENIDOS A TOXICASE!",bg="black",fg="white")
label4.config(height=1,width=1080)
label4.pack()

# agregar el correo del cliente

correo_entrada = tk.Entry(root)
correo_entrada.config(width=30)
correo_entrada.pack(side="bottom")
correo_label = tk.Label(root, text="Correo:")
correo_label.config(width=30)
correo_label.pack(side="bottom")

# agregar el DNI del cliente

dni_entrada = tk.Entry(root)
dni_entrada.config(width=30)
dni_entrada.pack(side="bottom")
dni_label = tk.Label(root, text="DNI:")
dni_label.config(width=30)
dni_label.pack(side="bottom")

# agregar el nombre del cliente

nombre_entrada = tk.Entry(root)
nombre_entrada.config(width=30)
nombre_entrada.pack(side="bottom")
nombre_label = tk.Label(root, text="Nombre:")
nombre_label.config(width=30)
nombre_label.pack(side="bottom")

# agregar botón para enviar el correo electrónico

enviar_button = tk.Button(root, text="Enviar correo", command=lambda:correo.EnviarCorreo(nombre_entrada.get(),dni_entrada.get(),correo_entrada.get()))
enviar_button.pack(side="bottom")

#LEER ARCHIVOS E INTEGRAR A ARCHIVOS_PRECIOS  
precios.LeerArchivoPrecios("Precios.txt")
diccionario_precios = LeerArchivoPrecios("Precios.txt")

# definir la función que se llamará cuando seleccione una opción en la primera lista
def seleccion_modelo(opcion_seleccionada):
    # obtener los valores correspondientes del diccionario
    valores = diccionario_precios[opcion_seleccionada]
    
    # crear una lista de opciones para los valores
    opciones_valores = list(valores.keys())
    
    # borrar las opciones anteriores (si existen)
    var2.set('')
    opcion2['menu'].delete(0, 'end')
    
    # agregar las nuevas opciones a la segunda lista
    for opcion in opciones_valores:
        opcion2['menu'].add_command(label=opcion, command=lambda val=opcion: var2.set(val))

def calcular_precio():
    # obtener el modelo seleccionado y el arreglo seleccionado
    modelo_seleccionado = var.get()
    arreglo_seleccionado = var2.get()
    
    # buscar el precio en el diccionario de precios
    precio = diccionario_precios[modelo_seleccionado][arreglo_seleccionado]
    
    # actualizar la etiqueta de texto con el precio encontrado
    precio_texto.set(f"Precio: {precio}")

# crear la primera lista de opciones
var = tk.StringVar(root)
var.set('Modelo')
opcion1 = list(diccionario_precios.keys())
opcion = tk.OptionMenu(root, var, *opcion1, command=seleccion_modelo)
opcion.config(width=30)
opcion.pack()

# crear la segunda lista de opciones
var2 = tk.StringVar(root)
var2.set('Arreglo')
opcion2 = tk.OptionMenu(root, var2, '')
opcion2.config(width=30)
opcion2.pack()

# crear el botón "Calcular" y la etiqueta de texto para el precio
calcular_boton = tk.Button(root, text="Calcular", command=calcular_precio)
calcular_boton.pack(pady=10)
calcular_boton.config(width=30)

precio_texto = tk.StringVar()
precio_texto.set("Precio: ")
precio_label = tk.Label(root, textvariable=precio_texto)
precio_label.config(width=30)
precio_label.pack()

root.mainloop()

# gastonmh46@gmail.com 