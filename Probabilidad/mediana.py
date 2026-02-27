# ============================================
# Código para calcular la mediana
# ============================================

def calcular_mediana(datos):
    datos_ordenados = sorted(datos) # Primero ordeno los datos porque la mediana necesita los valores en orden.
    n = len(datos_ordenados)     # Aquí obtengo la cantidad de datos
    mitad = n // 2   # Calculo la posición central usando división entera

    if n % 2 == 0:
        mediana = (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2   # Si la cantidad es par, saco el promedio de los dos valores centrales
    else:
        mediana = datos_ordenados[mitad]  # Si es impar, tomo el valor del centro

    return mediana
