import re
from datetime import datetime

def validar_fecha(fecha):
        """ 
        Esta función verifica que la fecha tenga el formato YYYY-MM-DD y sea válida

        Parámetros:
        fecha (str): La fecha en formato 'YYYY-MM-DD'.
    
        Retorna:
        bool: 'True' si la fecha es válida, 'False' en caso contrario.
    
        Ejemplos:
        >>> validar_fecha('2025-03-02')
        True
        >>> validar_fecha('25-25-11')
        False
        >>> validar_fecha('02-03-2025')
        True
        """
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", fecha):  # Expresión regular para formato YYYY-MM-DD
            return False
        try:
            datetime.strptime(fecha, "%Y-%m-%d")  # Comprueba si la fecha es válida
            return True
        except ValueError:
            return False
        
def calcular_irpf(salario):
    """
    Calcula el porcentaje de IRPF según el salario anual.

    Parámetros:
    salario (float): Salario anual en euros.

    Retorna:
    float: Tipo de IRPF aplicable.

    Ejemplos:
    >>> calcular_irpf(12000)
    19
    >>> calcular_irpf(15000)
    24
    >>> calcular_irpf(40000)
    37
    >>> calcular_irpf(100000)
    45
    >>> calcular_irpf(350000)
    47
    """
    if salario <= 12450:
        return 19
    elif salario <= 20200:
        return 50
    elif salario <= 20200:
        return 24
    elif salario <= 35200:
        return 30
    elif salario <= 60000:
        return 37
    elif salario <= 300000:
        return 45
    else:
        return 47
