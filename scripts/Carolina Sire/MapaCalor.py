import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Definir los datos en formato multi-línea
datos = """
VALPARAISO A VALPARAISO 130157
VALPARAISO A ARICA 32183
VALPARAISO A ATACAMA 289576
VALPARAISO A ANTOFAGASTA 425467
VALPARAISO A COQUIMBO 477043
VALPARAISO A BIOBIO 941579
VALPARAISO A LOS LAGOS 70409
VALPARAISO A MAGALLANES 2000
VALPARAISO A AYSEN 56330
ARICA A ATACAMA 2162
ARICA A VALPARAISO 5033
ARICA A BIOBIO 25
TARAPACA A BIOBIO 206795
TARAPACA ANTOFAGASTA 12878
TARAPACA A ATACAMA 5338
TARAPACA A COQUIMBO 75869
TARAPACA A VALPARAISO 6431
ANTOFAGASTA A VALPARAISO 28501 
ANTOFAGASTA A BIOBIO 13901
ANTOFAGASTA A ATACAMA 27449
ANTOFAGASTA A LOS LAGOS 27449
ANTOFAGASTA A ANTOFAGASTA 105500
ANTOFAGASTA A COQUIMBO 14483
ANTOFAGASTA A ARICA 1200
ATACAMA A ANTOFAGASTA 22700
ATACAMA A ATACAMA 52751
ATACAMA A COQUIMBO 209663
ATACAMA A BIOBIO 940320
COQUIMBO A ATACAMA 92016
COQUIMBO A BIOBIO 4500
BIOBIO A VALPARAISO 211286
BIOBIO A BIOBIO 1325763
BIOBIO A AYSEN 29700
BIOBIO A MAGALLANES 9291
BIOBIO A ANTOFAGASTA 240308
BIOBIO A ATACAMA 53129
BIOBIO A COQUIMBO 145858
BIOBIO A LOS LAGOS 979190
LOS LAGOS A LOS LAGOS 503698
LOS LAGOS A AYSEN 1267
LOS LAGOS A VALPARAISO 25516
LOS LAGOS A MAGALLANES 73166
LOS LAGOS A BIOBIO 54020
LOS LAGOS A LOS RIOS 57
AYSEN A LOS LAGOS 128150
AYSEN A COQUIMBO 20000
AYSEN A VALPARAISO 2444
AYSEN A BIOBIO 26714
AYSEN A AYSEN 3089
AYSEN A MAGALLANES 10301
MAGALLANES A BIOBIO 814042
MAGALLANES A VALPARAISO 5455
MAGALLANES A LOS LAGOS 60024
MAGALLANES A AYSEN 21499
MAGALLANES A MAGALLANES 177252
"""

# Procesar los datos y crear una lista de diccionarios
registros = []
for linea in datos.strip().split("\n"):
    partes = linea.split()
    # Si se encuentra la letra "A", separamos usando su posición
    if "A" in partes:
        idx = partes.index("A")
        origen = " ".join(partes[:idx])
        destino = " ".join(partes[idx+1:-1])
        tonelaje = int(partes[-1])
    else:
        # Caso particular: no se encuentra la "A"
        origen = partes[0]
        destino = " ".join(partes[1:-1])
        tonelaje = int(partes[-1])
    registros.append({"Origen": origen, "Destino": destino, "Tonelaje": tonelaje})

# Crear un DataFrame a partir de los registros
df = pd.DataFrame(registros)

# Crear una tabla pivote: filas = Región de Origen, columnas = Región de Destino y valores = Tonelaje
tabla_pivote = df.pivot(index="Origen", columns="Destino", values="Tonelaje").fillna(0)


# Generar el mapa de calor usando seaborn
plt.figure(figsize=(12, 8))
sns.heatmap(tabla_pivote, annot=True, fmt=".0f", cmap="Greens")
plt.title("Mapa de Calor del Tonelaje entre Regiones")
plt.xlabel("Región de Destino")
plt.ylabel("Región de Origen")
plt.tight_layout()
plt.show()
