# Importo las funciones que ya hice en otros archivos

from media import calcular_media
from moda import calcular_moda
from mediana import calcular_mediana
from libreria_bokeh import graficar_estadisticas

print("ANALISIS DE CONSUMO DE AGUA")
print("=" * 60)

anios = list(range(2010, 2027)) # Creo una lista con los años del 2010 al 2026

consumo_litros = [
    480, 465, 470, 455, 460,
    470, 480, 475, 370,
    460, 355, 460, 470,
    475, 370, 465, 460
] # Aquí guardo el consumo de agua en millones de litros

print("\nConsumo anual:") 
for a, c in zip(anios, consumo_litros):
    print(f"Anio {a}: {c} millones de litros") # Muestro el consumo año por año

media_val = calcular_media(consumo_litros) # Calculo las medidas estadísticas usando mis funciones
mediana_val = calcular_mediana(consumo_litros)
moda_val = calcular_moda(consumo_litros)

print("\nRESULTADOS ESTADISTICOS")
print(f"Media: {media_val:.2f} Millones de litros")
print(f"Mediana: {mediana_val} Millones de litros")
print(f"Moda: {moda_val}")

print("\nGenerando grafica...") # Finalmente genero la gráfica
graficar_estadisticas(anios, consumo_litros, media_val, moda_val, mediana_val)
