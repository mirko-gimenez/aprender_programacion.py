import tkinter as tk
from tkinter import messagebox

#funcion para verificar si el numero es par o impar
def verificar_par_impar():
    try:
        numero = int(entry_numero.get())#obtiene el numero ingresado por el usuario
        
        if numero % 2 == 0:
            resultado = "el numero es par."
        else:
            resultado = "el numero es impar."
        #muestra el resultado en una ventana de mensaje
        messagebox.showinfo("resultado", resultado)
    except ValueError:
    #muestra un mensaje de error si la entra no es un numero entero
        messagebox.showerror("entrada no valida", "por favor, ingrse un numero entero.")

#crear ventana peincipal
ventana = tk.Tk()
ventana.title("verificador de numero par o impar")
ventana.geometry("300x200")

#crear y colocar la etiqueta y el cuadro de entra para el numero
etiqueta = tk.Label(ventana, text="ingrese un numero entero:")
etiqueta.pack(pady=10)#empaquetar con un margen vertical

entry_numero = tk.Entry(ventana)
entry_numero.pack(pady=5) #empaquetar con un margen vertical

#crear y colocar el buton para verificar
boton_verificar = tk.Button(ventana, text="verificar", command=verificar_par_impar)
boton_verificar.pack(pady=20) #empaquetar con un margen veertical

#iniciar el bucle principal de la interfaz grafica
ventana.mainloop()