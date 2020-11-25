import pandas as pd
from pathlib import Path
from datafiles import TrackElan
import numpy as np


pd.set_option('display.max_columns', 500)

filename = Path('./ENTRADAS/marcha_347.txt')
destino = './SALIDAS/marcha_347.csv'
# carga track de Elan
t = TrackElan(filename)
df = t.data_frame  # obtiene los datos en Pandas DataFrame
fps = 24  # frames por segundo del video
# print(df)

# print(df)

# convertir a frame-by-frame
# Frame | Time | Categ

# Busca el tiempo final
index_final = len(df) -1
tiempo_final = df['end'][index_final]

# Arma vectores de Frames, Tiempo y Categ (vec de Nones)
rango = round(tiempo_final * fps)
frames = np.arange(0,rango+1)
vec_time = []
for samp in range(rango+1):
    vec_time.append(round(samp / fps, 3))
categ = ['Nada'] * (rango+1)

arreglo_inicial = [frames, vec_time, categ]
new_df = pd.DataFrame(arreglo_inicial, index=['Frames', 'Time', 'Categ']).transpose()


for i in range(len(df)):
    star = df['start'][i]
    fin = df['end'][i]
    cat = df['categ'][i]

    for j in range(len(new_df)):

        if star <= new_df['Time'][j] < fin:

            new_df['Categ'][j] == cat


new_df.to_csv(destino)




# imprimir nuevo DataFrame (ver ejemplo en target)


# grabar a archivo .csv
