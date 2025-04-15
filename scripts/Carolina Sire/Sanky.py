import plotly.graph_objects as go

# Datos: Región → Tipo de Accidente con sus cantidades
flujos = [
    ("ARI", "Hundimiento", 3),
    ("ARI", "Volcamiento", 1),

    ("IQU", "Hundimiento", 1),
    ("IQU", "Falla Máquina", 8),
    ("IQU", "Varamiento", 1),
    ("IQU", "Incendio o Amague de Incendio", 1),
    ("IQU", "A la Deriva", 3),
    ("IQU", "Colisión", 1),
    ("IQU", "Tocar Fondo", 1),
    ("IQU", "Acorbatamiento", 2),
    ("IQU", "Volcamiento", 2),
    ("IQU", "Desaparecimiento de nave", 3),
    ("IQU", "Tripulante al Mar", 1),

    ("ANT", "Falla Máquina", 6),
    ("ANT", "Tocar Fondo", 1),
    ("ANT", "A la Deriva", 2),
    ("ANT", "Hundimiento", 1),
    ("ANT", "Varamiento", 4),
    ("ANT", "Desaparecimiento de nave", 1),
    ("ANT", "Otro tipo", 2),

    ("COQ", "Falla máquina", 1),
    ("COQ", "Hundimiento", 1),
    ("COQ", "Varamiento", 1),

    ("SNO", "Volcamiento", 1),

    ("TAL", "Hundimiento", 3),
    ("TAL", "Incendio o Amague de Incendio", 1),

    ("VLD", "Varamiento", 1),
    ("VLD", "Tocar Fondo", 3),
    ("VLD", "Hundimiento", 2),

    ("PMO", "Varamiento", 1),
    ("PMO", "Incendio o Amague de Incendio", 3),
    ("PMO", "Volcamiento", 2),
    ("PMO", "Desaparecimiento de nave", 1),
    ("PMO", "Colisión", 1),
    
    ("CAS", "Tocar Fondo", 2),
    ("CAS", "Falla Máquina", 3),
    ("CAS", "Varamiento", 3),
    ("CAS", "Incendio o Amague de Incendio", 1),
    ("CAS", "Otro tipo", 1),
    ("CAS", "Falla Eléctrica", 1),
    ("CAS", "Colisión", 1),
    ("CAS", "Tripulante al mar", 1),
    
    ("PMO", "Hundimiento", 2),
    ("PMO", "Varamiento", 1),
    ("PMO", "Tocar Fondo", 1),
    
    ("AYS", "Falla Máquina", 3),
    ("AYS", "Tocar Fondo", 2),
    ("AYS", "Acorbatamiento", 2),
    ("AYS", "A la Deriva", 2),
    ("AYS", "Hundimiento", 3),
    ("AYS", "Varamiento", 3),
    ("AYS", "Incendio o Amague de Incendio", 4),
    ("AYS", "Volcamiento", 1),
    ("AYS", "Desaparecimiento de nave", 1),
    ("AYS", "Tripulante al Mar", 1),
    ("AYS", "Colisión", 4),
    
    ("PAR", "Hundimiento", 1),
    
    ("WIL", "Hundimiento", 1),
]

# Nodos únicos
regiones = sorted(set(r for r, _, _ in flujos))
accidentes = sorted(set(a for _, a, _ in flujos))
etiquetas = regiones + accidentes
indices = {label: i for i, label in enumerate(etiquetas)}

# Asignar colores a regiones
colores_regiones = {
    "ARI": "rgba(31,119,180,0.5)",
    "IQU": "rgba(255,127,14,0.5)",
    "ANT": "rgba(44,160,44,0.5)",
    "COQ": "rgba(214,39,40,0.5)",
    "SNO": "rgba(148,103,189,0.5)",
    "TAL": "rgba(140,86,75,0.5)",
    "VLD": "rgba(227,119,194,0.5)",
    "PMO": "rgba(127,127,127,0.5)",
    "CAS": "rgba(188,189,34,0.5)",
    "AYS": "rgba(23,190,207,0.5)",
    "PAR": "rgba(255,152,150,0.5)",
    "WIL": "rgba(197,176,213,0.5)"
}

# Enlaces y colores
fuente = [indices[r] for (r, a, _) in flujos]
objetivo = [indices[a] for (_, a, _) in flujos]
valores = [v for (_, _, v) in flujos]
colores = [colores_regiones[r] for (r, _, _) in flujos]

# Asignar color a cada nodo (regiones con color propio, accidentes gris claro)
colores_nodos = [colores_regiones.get(label, "#DDDDDD") if label in regiones else "#DDDDDD" for label in etiquetas]

# Crear gráfico Sankey
fig = go.Figure(data=[go.Sankey(
    arrangement="snap",
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="black", width=0.5),
        label=etiquetas,
        color= colores_nodos
    ),
    link=dict(
        source=fuente,
        target=objetivo,
        value=valores,
        color=colores
    )
)])


fig.update_layout(title_text="Flujo de Siniestros Marítimos: Región → Tipo de Accidente", font_size=10)
fig.write_html("siniestros_sankey.html")
fig.show()
