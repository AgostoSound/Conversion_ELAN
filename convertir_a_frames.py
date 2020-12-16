# LIBRERIAS
import pandas as pd
from pathlib import Path
from datafiles import TrackElan
import numpy as np
import os
#-----------------------------------------------------------------------------
pd.set_option('display.max_columns', 500)
#-----------------------------------------------------------------------------

# FUNCIONES
def asigna_categ(new_df, df, fps):

    for i in range(len(df)):
        c = df['categ'][i]
        s = df['start'][i]
        e = df['end'][i]

        s_fps = round(s * fps)
        e_fps = round(e * fps)

        new_df.loc[s_fps:e_fps, 'Categ'] = c

    return new_df

def main():

    # Direcciones
    fuente = './ENTRADAS'
    destino = './SALIDAS'
    directorios = os.listdir(fuente)

    for arch in directorios:
        filename = Path(fuente + '/' + arch)
        nom_salida = destino + '/' + arch + '.csv'

        # Carga track de Elan
        t = TrackElan(filename)
        df = t.data_frame  # obtiene los datos en Pandas DataFrame
        fps = 24  # frames por segundo del video

        # Busca el tiempo final
        index_final = len(df) - 1
        tiempo_final = df['end'].max()

        # Arma vectores de Frames, Tiempo y Categ (vec de Nones)
        rango = int(np.ceil(tiempo_final * fps))
        frames = np.arange(0, rango)
        vec_time = []
        for samp in range(rango):
            vec_time.append(round(samp / fps, 3))
        categ = ['Nada'] * (rango)

        arreglo_inicial = [frames, vec_time, categ]
        new_df = pd.DataFrame(arreglo_inicial, index=['Frames', 'Time', 'Categ']).transpose()

        df_ready = asigna_categ(new_df, df, fps)
        df_ready.to_csv(nom_salida)

#-----------------------------------------------------------------------------

main()