# ============================================
# Código para calcular la media (promedio)
# ============================================


def calcular_media(datos):
    suma_total = sum(datos)

    cantidad = len(datos) #uso len() para contar cuántos elementos tiene la lista
    media = suma_total / cantidad # Aquí calculo la media dividiendo la suma total entre la cantidad de elementos que tiene la lista.
    return media
