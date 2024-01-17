from IMPORTACION import ejecutar_script1
import tkinter as tk

ventanacolor = "#F0F8FF"  # Azul claro para el fondo
labelcolor = "#008B8B"   # Azul verdoso para las etiquetas
labelletracolor = "#FFFFFF" # Blanco para el texto, para contraste
botoncolor = "#F5DEB3"   # Color trigo para los botones, complementando el esquema
botonletracolor = "#2E8B57" # Verde oscuro para el texto de los botones

Fuente_Label = ("Calibri",10)
Fuente_Button = ("Calibri",10)

ventana = tk.Tk()
ventana.title("SHOW_PROCESSLIST")
ventana.config(bg=ventanacolor)
ventana.geometry("320x40")
ventana.resizable(0, 0)
ventana.iconbitmap("C:/Ingresa/tuRuta/Aqui/MYSQL.ico")

etiqueta1 = tk.Label(ventana, text="SHOW_PROCESSLIST", bg=labelcolor, fg=labelletracolor, font=Fuente_Label, width=20, height=1)
etiqueta1.grid(row=0, column=0, padx=5, pady=5)
boton1 = tk.Button(ventana, text="RUN", command=ejecutar_script1, bg=botoncolor, fg=botonletracolor, width=20, height=1)
boton1.grid(row=0, column=1, padx=5, pady=5)

ventana.mainloop()