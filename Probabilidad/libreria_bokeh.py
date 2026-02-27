# ============================================
# libreria_bokeh.py
# ============================================

# Importo las herramientas necesarias de Bokeh
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, HoverTool


def graficar_estadisticas(anios, consumo, media, moda, mediana):

    # ------------------------------------------------
    # 1. Fuente de datos principal
    # Aquí creo la fuente de datos principal con los años y el consumo. ColumnDataSource es la estructura que usa Bokeh para manejar datos.
    # ------------------------------------------------
    
    datos = ColumnDataSource(data={
        'anio': anios,
        'consumo': consumo
    })

    # ------------------------------------------------
    # 2. Fuentes para estadísticas
    # Aquí creo una fuente para la media. Repito el mismo valor en todos los años para dibujar una línea horizontal.
    # ------------------------------------------------
    
    fuente_media = ColumnDataSource(data={
        'anio': anios,
        'valor': [media] * len(anios),
        'etiqueta': [f"Media: {media:.2f} Millones de litros"] * len(anios)
    })

    # Hago lo mismo para la mediana.
    fuente_mediana = ColumnDataSource(data={
        'anio': anios,
        'valor': [mediana] * len(anios),
        'etiqueta': [f"Mediana: {mediana} Millones de litros"] * len(anios)
    })


    # Aquí verifico si existe moda. Si hay, también creo su fuente de datos.
    fuente_moda = None
    if moda:
        moda_valor = moda[0]
        fuente_moda = ColumnDataSource(data={
            'anio': anios,
            'valor': [moda_valor] * len(anios),
            'etiqueta': [f"Moda: {moda_valor} Millones de litros"] * len(anios)
        })

    # ------------------------------------------------
    # 3. Crear figura
    # Aquí creo la figura principal y configuro título, ejes y herramientas.
    # ------------------------------------------------
    p = figure(
        title="Consumo anual de agua",
        x_axis_label="Año",
        y_axis_label="Consumo (Millones de litros)",
        width=900,
        height=450,
        tools="pan,wheel_zoom,box_zoom,reset,save"
    )

    p.xaxis.ticker = anios

    # ------------------------------------------------
    # 4. Glyphs de datos reales
    # ------------------------------------------------
    linea_consumo = p.line(
        'anio', 'consumo',
        source=datos,
        line_width=2,
        legend_label="Consumo"
    )

    # Agrego puntos sobre la línea para marcar los valores exactos.
    puntos = p.circle(
        'anio', 'consumo',
        source=datos,
        size=8,
        legend_label="Datos reales"
    )

    # ------------------------------------------------
    # 5. Líneas estadísticas
    # Aquí dibujo la línea de la media (verde y punteada).
    # ------------------------------------------------
    linea_media = p.line(
        'anio', 'valor',
        source=fuente_media,
        line_dash="dashed",
        line_width=2,
        color="green",
        legend_label="Media"
    )

    linea_mediana = p.line(
        'anio', 'valor',
        source=fuente_mediana,
        line_dash="dotdash",
        line_width=2,
        color="orange",
        legend_label="Mediana"
    )

    if fuente_moda:
        linea_moda = p.line(
            'anio', 'valor',
            source=fuente_moda,
            line_dash="dotted",
            line_width=2,
            color="red",
            legend_label="Moda"
        )

    # ------------------------------------------------
    # 6. HoverTools
    # Aquí agrego información emergente para los puntos reales.
    # ------------------------------------------------
    # Hover para puntos
    p.add_tools(HoverTool(
        renderers=[puntos],
        tooltips=[
            ("Año", "@anio"),
            ("Consumo", "@consumo millones de litros")
        ]
    ))

    # Hover para media
    p.add_tools(HoverTool(
        renderers=[linea_media],
        tooltips=[("Media", "@etiqueta")]
    ))

    # Hover para mediana
    p.add_tools(HoverTool(
        renderers=[linea_mediana],
        tooltips=[("Mediana", "@etiqueta")]
    ))

    # Hover para moda
    if fuente_moda:
        p.add_tools(HoverTool(
            renderers=[linea_moda],
            tooltips=[("Moda", "@etiqueta")]
        ))

    # ------------------------------------------------
    # 7. Configuración visual
    # ------------------------------------------------
    p.legend.location = "top_left"
    p.legend.click_policy = "hide"  # Permito ocultar líneas haciendo clic

    show(p)
