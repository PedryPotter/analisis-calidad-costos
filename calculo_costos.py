# PROYECTO: MINIMIZACIÓN DE COSTOS
# Este código tiene errores intencionales para demostrar la potencia de SonarQube

def calcular_impuesto_peru(monto):
    # ERROR 1: Variable duplicada (genera confusión y gasto de tiempo en revisión)
    igv = 0.18
    igv = 0.18 
    
    # ERROR 2: Hardcoded value (si el IGV cambia, hay que buscar esto en mil archivos)
    # Minimizar costos implica usar constantes, no números sueltos.
    total = monto * 1.18 
    
    print("Calculando...")
    return total

def funcion_olvidada():
    # ERROR 3: Código muerto (Dead Code)
    # El código que no se usa aumenta los costos de mantenimiento y análisis.
    pass

def proceso_complejo(a, b):
    # ERROR 4: Bug potencial (división por cero no controlada)
    # Un error en producción es 10 veces más caro que en desarrollo.
    resultado = a / b
    return resultado
