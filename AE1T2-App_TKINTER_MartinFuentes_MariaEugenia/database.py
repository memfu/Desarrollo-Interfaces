import sqlite3
import os
import subprocess

db_path = 'AE1T2-App_TKINTER_MartinFuentes_MariaEugenia/database/appEmpleados.db'

def crear_tabla():
    conexion = sqlite3.connect(db_path)
    # sin cursor no podemos ejecutar los comandos
    cursor = conexion.cursor()
    """ Explicación:
    - Uso VARCHAR() en lugar de TEXT() para tener compatibilidad con otros motores (MySQL, PostgreSQL, etc.)
    - En SQLite, no existe un tipo de datos DATE o DATETIME nativo como en MySQL o PostgreSQL. 
    Por eso se almacenan como TEXT en formato YYYY-MM-DD
    - SQLite no tiene ENUM, así que usamos CHECK (genero IN (...)) para limitar los valores posibles.
    - SQLite no tiene DECIMAL, así que se usa REAL para almacenar valores con decimales.
    """
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS EMPLEADOS (
        id_empleado INTEGER PRIMARY KEY AUTOINCREMENT,
        nombreYApellidos VARCHAR(150) NOT NULL,
        fecha_inicio TEXT NOT NULL, 
        fecha_nacimiento TEXT NOT NULL,
        direccion VARCHAR(255) NOT NULL,
        nif VARCHAR(9) UNIQUE NOT NULL,
        datos_bancarios VARCHAR(50) NOT NULL,
        nr_afiliacion_seg_social VARCHAR(15) UNIQUE NOT NULL,
        genero TEXT NOT NULL,
        departamento VARCHAR(50) NOT NULL,
        puesto VARCHAR(50) NOT NULL,
        telefono VARCHAR(15) NOT NULL,
        salario_anual REAL NOT NULL,
        irpf REAL NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL,
        pagas_extra INTEGER,
        seg_social REAL NOT NULL
);
""")
    conexion.commit()
    conexion.close()

def darAltaEmpleado(nombre, fecha_inicio, fecha_nacimiento, direccion, nif, banco, nrSS, genero, dept, puesto, telefono, salarioAnual, irpf, email, pagExt, ss):   
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()

    # Normalizar el género a minúsculas
    genero = genero.lower()
    
    try:
        cursor.execute("""
        INSERT INTO EMPLEADOS (nombreYApellidos, fecha_inicio, fecha_nacimiento, direccion, nif, datos_bancarios, nr_afiliacion_seg_social, genero, departamento, puesto, telefono, salario_anual, irpf, email, pagas_extra, seg_social) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (nombre, fecha_inicio, fecha_nacimiento, direccion, nif, banco, nrSS, genero, dept, puesto, telefono, salarioAnual, irpf, email, pagExt, ss))
        conexion.commit()
        conexion.close()
        return True
    except sqlite3.IntegrityError:
        conexion.close()
        return False
    

def generar_fichero_empleados():
    """
        Función para generar un archivo .txt a partir de los datos guardados en la bbdd previamente.
        En caso de no encontrar ningún registro, muestra un mensaje avisando al usuario.
        La ruta del fichero es específica del proyecto. En caso de querer otra ruta y otro nombre, habría que especificarlo.
        Si se hubiera realizado ya la generación del fichero previamente, esta función sobreescribirá el fichero con los datos
        que sean actuales a la hora de pulsar el botón.
        Además se ha incluido un comando para que el archivo se abra una vez que se haya generado.
    """
    conexion = sqlite3.connect(db_path)
    cursor = conexion.cursor()
    
    cursor.execute("""
                   SELECT nombreYApellidos, 
                   direccion, 
                   nif, datos_bancarios, nr_afiliacion_seg_social, 
                   salario_anual, irpf, 
                   pagas_extra, seg_social 
                   FROM EMPLEADOS
                   """)
    empleados = cursor.fetchall()
    
    conexion.close()

    if not empleados:
        return "No hay empleados en la base de datos."
    
    # Nombre del archivo y ruta
    nombre_fichero = "AE1T2-App_TKINTER_MartinFuentes_MariaEugenia/fichero/fichero_empleados.txt"

    # "w" sobreescribe el archivo si existe
    with open(nombre_fichero, "w", encoding="utf-8") as f:
        for empleado in empleados:
            nombreYApellidos, direccion, nif, datos_bancarios, nr_afiliacion_seg_social, salario_anual, irpf, pagas_extra, seg_social = empleado
            
            # Formato del archivo de texto
            f.write(f"{nombreYApellidos.upper()}\n")
            f.write(f"{direccion}\n")
            f.write(f"NIF {nif}\t\tNAF {nr_afiliacion_seg_social}\t\tCCC {datos_bancarios}\n")
            f.write("CONCEPTOS SALARIALES " + "-" * 50 + "\n")
            f.write(f"SALARIO ANUAL: {salario_anual}€\t\tPAGAS: {pagas_extra}\t\tIRPF: {irpf}%\t\tSEGURIDAD SOCIAL: {seg_social}€\n")
            f.write("\n" + "=" * 80 + "\n\n")  # Separador entre empleados

    # **Abrir el archivo después de crearlo**
        try:
            if os.name == "nt":  # Windows
                os.startfile(nombre_fichero)
            elif os.name == "posix":  # macOS & Linux
                subprocess.run(["open", nombre_fichero]) if "darwin" in os.sys.platform else subprocess.run(["xdg-open", nombre_fichero])
        except Exception as e:
            return f"Fichero generado, pero no se pudo abrir: {e}"

        return "Fichero generado y abierto correctamente."
# Ejecutar la creación de tabla al importar este módulo
crear_tabla()