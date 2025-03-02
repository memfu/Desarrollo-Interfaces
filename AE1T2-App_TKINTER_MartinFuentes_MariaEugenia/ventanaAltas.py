from tkinter import *
from tkinter import ttk
from database import darAltaEmpleado
import re
from datetime import datetime


def abrir_ventana_altas():
    # TK es la ventana inicial de la aplicación. 
    #Toplevel son ventanas que genera el objeto por encima de la ventana inicial
    ventAltas = Toplevel()
    ventAltas.title("ALTAS")
    ventAltas.resizable(0,0)
    ventAltas.config(bd=20) # Espacio entre el borde de la ventana y el contenido puesto

    # Seis columnas, 12 filas
    
    Label(ventAltas, text="APELLIDOS Y NOMBRE").grid(row=0, 
                                                column=0, 
                                                columnspan=6, 
                                                padx=5, pady=5)
    
    # .grid() debe ir en otra línea porque devuelve None en lugar de Entry, de manera que no se puede almacenar la referencia al campo de entrada                                            padx=5, pady=5)
    entryNombre = Entry(ventAltas)
    entryNombre.grid(row=1, 
                     column=0, 
                     columnspan=6, 
                     padx=5, pady=5,
                    sticky=EW)
    
    ##########################################################################
    Label(ventAltas, text="FECHA INICIO (YYYY-MM-DD)").grid(row=2, 
                                          column=0, 
                                          #columnspan=6, 
                                          padx=5, pady=5)
    entryFechaIni = Entry(ventAltas)
    entryFechaIni.grid(row=3, 
                     column=0, 
                     #columnspan=6, 
                     padx=5, pady=5)


    Label(ventAltas, text="FECHA NACIMIENTO (YYYY-MM-DD)").grid(row=2, 
                                              column=1, 
                                              #columnspan=6, 
                                              padx=5, pady=5)
    entryFechaNac = Entry(ventAltas)
    entryFechaNac.grid(row=3, 
                     column=1, 
                     #columnspan=6, 
                     padx=5, pady=5)

    Label(ventAltas, text="DIRECCIÓN").grid(row=2, 
                                       column=2, 
                                       columnspan=4, 
                                       padx=5, pady=5)
    entryDire = Entry(ventAltas)
    entryDire.grid(row=3, 
                     column=2, 
                     columnspan=4, 
                     padx=5, pady=5,
                    sticky=EW)
    ##########################################################################
    Label(ventAltas, text="NIF").grid(row=4, 
                                 column=0,
                                 #columnspan=6, 
                                 padx=5, pady=5)
    entryNIF = Entry(ventAltas)
    entryNIF.grid(row=5,
                     column=0, 
                     #columnspan=6,
                     padx=5, pady=5)
    Label(ventAltas, text="DATOS BANCARIOS").grid(row=4, 
                                             column=1,
                                             columnspan=3,
                                             padx=5, pady=5)
    entryBanco = Entry(ventAltas)
    entryBanco.grid(row=5, 
                     column=1, 
                     columnspan=3, 
                     padx=5, pady=5,
                    sticky=EW)
    Label(ventAltas, text="NÚMERO DE AFILIACIÓN SS").grid(row=4, 
                                                     column=4,
                                                     columnspan=2,
                                                     padx=5, pady=5)
    entryNrSS = Entry(ventAltas)
    entryNrSS.grid(row=5, 
                     column=4,
                     columnspan=2,
                     padx=5, pady=5,
                    sticky=EW)
    ##########################################################################
    Label(ventAltas, text="GÉNERO").grid(row=6, 
                                    column=0, 
                                    #columnspan=6, 
                                    padx=5, pady=5)
    entryGenero = Entry(ventAltas)
    # ComboBox para el género
    opciones_genero = ['Hombre', 'Mujer', 'Otro']
    comboGenero = ttk.Combobox(ventAltas, values=opciones_genero, state="readonly")
    comboGenero.grid(row=7, 
                     column=0, 
                     #columnspan=6, 
                     padx=5, pady=5)
    comboGenero.current(0)  # Establece "Masculino" como valor predeterminado


    Label(ventAltas, text="DEPARTAMENTO").grid(row=6, 
                                          column=1, 
                                          columnspan=3, 
                                          padx=5, pady=5)
    entryDept = Entry(ventAltas)
    entryDept.grid(row=7, 
                     column=1, 
                     columnspan=3, 
                     padx=5, pady=5,
                    sticky=EW)
    Label(ventAltas, text="PUESTO").grid(row=6, 
                                    column=4, 
                                    columnspan=2, 
                                    padx=5, pady=5)
    entryPuesto = Entry(ventAltas)
    entryPuesto.grid(row=7, 
                     column=4,
                     columnspan=2,
                     padx=5, pady=5,
                    sticky=EW)
    ##########################################################################
    Label(ventAltas, text="").grid(column=0, row=8, padx=5, pady=5)
    ##########################################################################
    Label(ventAltas, text="TELÉFONO").grid(row=9, 
                                      column=0, 
                                      padx=5, pady=5,
                                      sticky=E)
    entryTel = Entry(ventAltas)
    entryTel.grid(row=9, 
                     column=1, 
                     padx=5, pady=5)
    Label(ventAltas, text="SALARIO ANUAL").grid(row=9, 
                                           column=2, 
                                           padx=5, pady=5,
                                           sticky=E)
    entrySalario = Entry(ventAltas)
    entrySalario.grid(row=9, 
                     column=3, 
                     padx=5, pady=5)
    Label(ventAltas, text="IRPF").grid(row=9, 
                                  column=4,
                                  padx=5, pady=5,
                                  sticky=E)
    entryIRPF = Entry(ventAltas)
    entryIRPF.grid(row=9, 
                     column=5, 
                     padx=5, pady=5)
    ##########################################################################
    Label(ventAltas, text="EMAIL").grid(row=10, 
                                   column=0, 
                                   padx=5, pady=5,
                                   sticky=E)
    entryEmail = Entry(ventAltas)
    entryEmail.grid(row=10, 
                     column=1, 
                     padx=5, pady=5)
    Label(ventAltas, text="PAGAS EXTRA").grid(row=10, 
                                         column=2, 
                                         padx=5, pady=5,
                                         sticky=E)
    entryPagExt = Entry(ventAltas)
     # ComboBox para las pagas extra
    opciones_pagas = [0,12,14]
    comboPagas = ttk.Combobox(ventAltas, values=opciones_pagas, state="readonly")
    comboPagas.grid(row=10, 
                     column=3, 
                     padx=5, pady=5)
    comboPagas.current(1)  # Establece 12 como valor predeterminado
  
    Label(ventAltas, text="SEG. SOCIAL").grid(row=10,
                                         column=4, 
                                         padx=5, pady=5,
                                         sticky=E)
    entrySS = Entry(ventAltas)
    entrySS.grid(row=10, 
                     column=5, 
                     padx=5, pady=5)
    ##########################################################################

    def validar_fecha(fecha):
        """ 
            Esta función verifica que la fecha tenga el formato YYYY-MM-DD y sea válida 
        """
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):  # Expresión regular para formato YYYY-MM-DD
            return False
        try:
            datetime.strptime(fecha, "%Y-%m-%d")  # Comprueba si la fecha es válida
            return True
        except ValueError:
            return False
    
    def btnInsertar():
        """
            Esta función comprueba primero con la función de validar_fecha que los datos de fechas sean correctos antes de
            empaquetarlos para la función de insertar datos del archivo database.py
            Si las fechas son válidas, coge el resto de datos de los campos de entrada (tanto de texto como de ComboBox).
            Seguidamente comprueba que todos los campos hayan sido rellenados y se crea una variable que será el resultado de 
            pasar los datos a la función de darAltaEmpleado() del archivo database.py.
            El * se usa para desempaquetar la tupla en argumentos individuales y que se puedan asociar a los parámetros requeridos
            en la otra función.
            El usuario recibe un mensaje informativo.
        """
        if not (validar_fecha(entryFechaIni.get()) and validar_fecha(entryFechaNac.get())):
            lbl_status.config(text="⚠️ Formato de fecha incorrecto. Usa YYYY-MM-DD.", fg="red")
        else:
            datos = (
                        entryNombre.get(),
                        entryFechaIni.get(),
                        entryFechaNac.get(),
                        entryDire.get(),
                        entryNIF.get(),
                        entryBanco.get(),
                        entryNrSS.get(),
                        comboGenero.get(),
                        entryDept.get(),
                        entryPuesto.get(),
                        entryTel.get(),
                        entrySalario.get(),
                        entryIRPF.get(),
                        entryEmail.get(),
                        comboPagas.get(),
                        entrySS.get()
                    )
            if all(datos): # para comprobar que todos los campos están rellenados
                resultado = darAltaEmpleado(*datos)  # Desempaqueta la tupla en argumentos individuales
                if resultado:
                    lbl_status.config(text="✅ Empleado insertado correctamente", fg="green")
                else:
                    lbl_status.config(text="❌ Error al insertar. NIF, email y/o nr. SS duplicado", fg="red")
            else:
                    lbl_status.config(text="⚠️ Rellena todos los campos", fg="red")     
            return

       
    
    def limpiar_campos():
        # Borra el texto del Entry
        entryNombre.delete(0, END)
        entryFechaIni.delete(0, END)
        entryFechaNac.delete(0, END)
        entryDire.delete(0, END)
        entryNIF.delete(0, END)
        entryBanco.delete(0, END)
        entryNrSS.delete(0, END)
        entryDept.delete(0, END)
        entryPuesto.delete(0, END)
        entryTel.delete(0, END)
        entrySalario.delete(0, END)
        entryIRPF.delete(0, END)
        entryEmail.delete(0, END)
        entrySS.delete(0, END) 
        comboGenero.current(0)  # Reinicia el Combobox a la opción inicial
        comboPagas.current(1)  # Reinicia el Combobox de Pagas Extra
    
    Button(ventAltas, text="LIMPIAR", command=limpiar_campos).grid(row=11,  column=4, sticky=E)

    Button(ventAltas, text="INSERTAR", command=btnInsertar).grid(row=11, column=5, columnspan=2, sticky=E)

    lbl_status = Label(ventAltas, text="")
    lbl_status.grid(row=11, column=0, columnspan=2, sticky=W)
    
    
    #print("Tamaño de la cuadrícula (filas, columnas):", ventAltas.grid_size())  # Devuelve (2, 3) → 2 filas y 3 columnas

    ventAltas.mainloop()