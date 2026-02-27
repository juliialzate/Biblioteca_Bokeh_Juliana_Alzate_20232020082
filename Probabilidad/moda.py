# ============================================
# Código para calcular la moda
# ============================================

from collections import Counter

def calcular_moda(datos):
    contador = Counter(datos)   # Aquí cuento cuántas veces aparece cada número

    max_veces = max(contador.values())   # Busco el valor que más se repite

    # Si todos aparecen solo una vez, digo que no hay moda
    if max_veces == 1:
        return []

    modas = [k for k, v in contador.items() if v == max_veces]    # Aquí guardo los números que se repiten más veces
    return modas
