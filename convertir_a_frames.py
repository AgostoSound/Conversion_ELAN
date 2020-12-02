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

def asigna_categ(new_df, df, fps):

    for i in range(len(df)):
        c = df['categ'][i]
        s = df['start'][i]
        e = df['end'][i]

        s_fps = round(s * fps)
        e_fps = round(e * fps)

        print(str(s_fps) + ' ' + str(e_fps) + ' ' + c)

        new_df.loc[s_fps:e_fps, 'Categ'] = c

        # for j in range(len(new_df)):
        #     if s_fps <= new_df['Frames'][j] < e_fps:
        #         new_df['Categ'][j] == c


    return new_df

# convertir a frame-by-frame
# Frame | Time | Categ

# Busca el tiempo final
index_final = len(df) -1
tiempo_final = df['end'].max()

# Arma vectores de Frames, Tiempo y Categ (vec de Nones)
rango = int(np.ceil(tiempo_final * fps))
frames = np.arange(0,rango)
vec_time = []
for samp in range(rango):
    vec_time.append(round(samp / fps, 3))
categ = ['Nada'] * (rango)

arreglo_inicial = [frames, vec_time, categ]
new_df = pd.DataFrame(arreglo_inicial, index=['Frames', 'Time', 'Categ']).transpose()

df_ready = asigna_categ(new_df, df, fps)
df_ready.to_csv(destino)


# imprimir nuevo DataFrame (ver ejemplo en target)


# grabar a archivo .csv
