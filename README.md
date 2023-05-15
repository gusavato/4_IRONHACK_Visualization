# IRONHACK_Visualización

<div style="text-align:center">
    <img src="./images/portada.jpg" alt="portada">
</div>

## Indice:
1.[📜 Descripción](#descripcion)\
2.[⏳ Desarrollo](#desarrollo)\
3.[📊 Visulización](#visualizacion)\
4.[✍️ Storytelling](#database)\
5.[📁 Estructura](#Estructura)

## Descripción:<a name="descripcion"/>

Cuarto proyecto en Ironhack, donde se realizaran distintas visualizaciones sobre distintos festivales de música que se desarrollarán a lo largo de 2023. Para ello se hará uso de la información obtenida en el anterior proyecto de Ironhack ([Ironhack_ETL](https://github.com/gusavato/3_IRONHACK_ETL)). 

Esta información se enriquecerá con información obtenida de las API's de Spotify y Google Maps. Una vez realizado el proceso de ETL, se procederá a la visualización de los mismos.


## Desarrollo:<a name="desarrollo"/>

Realizaremos el proceso siguiendo los siguientes pasos:

1- En el notebook [ETL_Fest](https://github.com/gusavato/4_IRONHACK_Visualization/blob/main/Jupyter/ETL_fest.ipynb) partimos de el dataframe de [festivales](https://github.com/gusavato/3_IRONHACK_ETL/blob/main/data/df_fest_clean.parquet) obtenido en el proyecto de la semana anterior. En este proceso formatearemos la fecha de inicio y final de cada festival, así como añadiremos las coordenadas de longitud y latitud a cada festival

2- En el notebook [ETL_Tracks](https://github.com/gusavato/4_IRONHACK_Visualization/blob/main/Jupyter/ETL_Tracks.ipynb) partimos de el dataframe de [grupos](https://github.com/gusavato/3_IRONHACK_ETL/blob/main/data/grupos_spotify_clean.parquet) obtenido en el proyecto de la semana anterior. En este proceso crearemos un datframe con el top 10 de canciones de cada artista, así como métricas propias de Spotify


## Visualización:<a name="visualizacion"/>

La información obtenida en los dos procesos de extracción 