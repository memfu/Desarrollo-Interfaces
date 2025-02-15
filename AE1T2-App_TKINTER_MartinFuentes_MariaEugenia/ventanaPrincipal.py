from tkinter import *
from ventanaAltas import abrir_ventana_altas
from database import generar_fichero_empleados

def exportar_empleados():
    mensaje = generar_fichero_empleados()
    lbl_status.config(text=mensaje, fg="green" if "correctamente" in mensaje else "red")


root = Tk()

# 4 filas, 3 columnas (0-2)

root.config(bd=20)# bd se refiere al padding
root.title("Gestión de empleados")

root.geometry("400x250+250+400")# tamaño anchoxalto+coordenadaX+coordenadaY
root.resizable(1,1)# 0,0 es para que no se pueda cambiar el tamaño de la ventana

# Aquí se configuran las columnas para centrar correctamente los elementos
root.columnconfigure(0, weight=1)  # Columna izquierda (vacía)
root.columnconfigure(1, weight=2)  # Columna central (más grande)
root.columnconfigure(2, weight=1)  # Columna derecha (vacía)

# Etiqueta vacía en columna 0 para forzar el centrado
Label(root, text="").grid(row=0, column=0, padx=5, pady=5)

Label(root, text="PERSONAL +").grid(row=0,
                                    column=1,
                                    padx=5, pady=5,
                                    sticky=EW)

imagen = PhotoImage(file="AE1T2-App_TKINTER_MartinFuentes_MariaEugenia/img/seta.png").subsample(4)

Label(root, image = imagen).grid(row=1,
                                 column=1,
                                 padx=5, pady=5,
                                 sticky=EW)

Button(root, text='ALTA EMPLEADO', bg='#FDE499', command=abrir_ventana_altas).grid(row=2, 
                                                      column=1,
                                                      padx=5, pady=5,
                                                      sticky=EW)

# command=generar_fichero_empleados() → Lo ejecutaba al iniciar la app.
# command=generar_fichero_empleados → Se ejecuta solo cuando se hace clic en el botón.
Button(root, text="FICHERO EMPLEADOS", bg='#FDE499', command=generar_fichero_empleados).grid(row=3, 
                                                          column=1, 
                                                          padx=5, pady=5,
                                                          sticky=EW)

lbl_status = Label(root, text="")
lbl_status.grid(row=5, column=1, padx=5, pady=5)

# Etiqueta vacía en columna 2 para forzar el centrado
Label(root, text="").grid(row=0, column=2, padx=5, pady=5)

#print("Tamaño de la cuadrícula (filas, columnas):", root.grid_size())  # Devuelve (2, 3) → 2 filas y 3 columnas

root.mainloop()