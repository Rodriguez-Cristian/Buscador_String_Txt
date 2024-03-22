import os #libreria para poder abrir archivos
import tkinter as tk
from tkinter import filedialog #para dialogar con los archivos

#aca voy a armar las funciones!
#BUSCAR LA CADENA
def buscar_cadena(ruta, cadena): #recibe la ruta(path) y cadena(busco)
    archivos_con_cadena = []#armo un arreglo
    for archivo in os.listdir(ruta):#listo mis archivos
        #si mis archivos son txt o log
        if archivo.endswith(".txt") or archivo.endswith(".log"):
            ruta_archivo = os.path.join(ruta, archivo)
            with open(ruta_archivo, 'r') as file: #lo leo
                contenido = file.read()
                #esto es para contar cuantas veces se me dio
                #ese error dentro del log
                veces_aparece = contenido.count(cadena)
                if veces_aparece > 0:
                    archivos_con_cadena.append((archivo, 
                                                veces_aparece))
        #me falto devolver la cadena
    return archivos_con_cadena
#Funcion para buscar y mostrar
def buscar_y_mostrar():
    ruta_carpeta = entry_ruta.get() #la ruta que elegi
    cadena_buscada = entry_cadena.get() #la cadena que escribi
    if os.path.isdir(ruta_carpeta):
        archivos_encontrados = buscar_cadena(ruta_carpeta,
                                             cadena_buscada)
        if archivos_encontrados:
            resultado_text = "La cadena '{}' se encontró en los siguientes archivos:\n".format(cadena_buscada)
#"La cadena '{}' se encontró en los siguientes archivos:\n".format
# (cadena_buscada)
            for archivo, veces in archivos_encontrados:
                resultado_text += "{} - Se encontró: {} veces:\n".format(archivo,veces)
#resultado_text = "{} - Se encontró: {} veces:\n".format(archivo,veces)
            resultado_label.config(text=resultado_text)
        else:
            resultado_label.config(text=f"No se encontrola cadena '{cadena_buscada}' en ningun archivo.")
#resultado_label.config(text=f"No se encontrola cadena 
# '{cadena_buscada}' en ningun archivo.")
    else:
        resultado_label.config(text="La ruta especificada no es de una carpeta valida")
        #"La ruta especificada no es de una carpeta valida")
        
#creamos la ventana principal
ventana = tk.Tk()
ventana.title("Buscador de cadenas en archivos .txt .log / Colo R.")

#mejor la coloco dentro:
def limpiar_entry():
    entry_ruta.delete(0,tk.END)
#creamos y colocamos los elementos en esta ventana

#ACA SELECCIONO LA CARPETA
label_ruta =  tk.Label(ventana, text="Ruta de carpeta:")
label_ruta.grid(row=0, column=0,padx=5,pady=5)

entry_ruta = tk.Entry(ventana,width=50)
entry_ruta.grid(row=0, column=1 ,padx=5,pady=5)

boton_examinar = tk.Button(ventana,text="Examinar",command=lambda: [limpiar_entry(),entry_ruta.insert(tk.END,filedialog.askdirectory())])#aca va la fución
#command=lambda: [limpiar_entry(),entry_ruta.insert(tk.END,filedialog.
# askdirectory())])#aca va la fución
boton_examinar.grid(row=0, column=2,padx=5,pady=5)

#Aca armo ahora el entry para buscar la cadena que necesito

label_cadena =  tk.Label(ventana, text="Cadena a buscar:")
label_cadena.grid(row=1, column=0,padx=5,pady=5)

entry_cadena = tk.Entry(ventana,width=50)
entry_cadena.grid(row=1, column=1 ,padx=5,pady=5)

boton_buscar = tk.Button(ventana,text="Buscar",command=buscar_y_mostrar)#aca va la fución
boton_buscar.grid(row=1, column=2,padx=5,pady=5)

#Aca muestro los resultados
resultado_label = tk.Label(ventana,text="")
resultado_label.grid(row=2,column=0,columnspan=3,padx=5,pady=5)

#ejecuto la ventana en un bucle
ventana.mainloop()
