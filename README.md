# IRONHACK_Visualización

<div style="text-align:center">
    <img src="./images/portada.jpg" alt="portada">
</div>

## Indice:
1.[📜 Descripción](#descripcion)\
2.[⏳ Desarrollo](#desarrollo)\
3.[📊 Visulización](#visualizacion)\
4.[✍️ Storytelling](#story)\
5.[📁 Estructura](#Estructura)

## Descripción:<a name="descripcion"/>

Cuarto proyecto en Ironhack, donde se realizaran distintas visualizaciones sobre distintos festivales de música que se desarrollarán a lo largo de 2023, y los artistas que en ellos participan. Para ello se hará uso de la información obtenida en el anterior proyecto de Ironhack ([Ironhack_ETL](https://github.com/gusavato/3_IRONHACK_ETL)). 

Esta información se enriquecerá con información obtenida de las API's de Spotify y Google Maps. Una vez realizado el proceso de ETL, se procederá a la visualización de los mismos.


## Desarrollo:<a name="desarrollo"/>

Realizaremos el proceso siguiendo los siguientes pasos:

1- En el notebook [ETL_Fest](https://github.com/gusavato/4_IRONHACK_Visualization/blob/main/Jupyter/ETL_fest.ipynb) partimos de el dataframe de [festivales](https://github.com/gusavato/3_IRONHACK_ETL/blob/main/data/df_fest_clean.parquet) obtenido en el proyecto de la semana anterior. En este proceso formatearemos la fecha de inicio y final de cada festival, así como añadiremos las coordenadas de longitud y latitud a cada festival

2- En el notebook [ETL_Tracks](https://github.com/gusavato/4_IRONHACK_Visualization/blob/main/Jupyter/ETL_Tracks.ipynb) partimos de el dataframe de [grupos](https://github.com/gusavato/3_IRONHACK_ETL/blob/main/data/grupos_spotify_clean.parquet) obtenido en el proyecto de la semana anterior. En este proceso crearemos un datframe con el top 10 de canciones de cada artista, así como métricas propias de Spotify


## Visualización:<a name="visualizacion"/>

La información obtenida en los dos procesos de extracción se ha cargado a una base de datos de Mongo. El proceso de visualización lo realizaremos en Tableau, para poder usar los datos, debemos [exportarlos](https://github.com/gusavato/4_IRONHACK_Visualization/tree/main/data/db_mongo) en formato .json

En este [enlace](https://public.tableau.com/app/profile/augusto.abad/viz/Festivales_16841034848740/ArtistasVsFestivales) se puede ver las distintas tablas y gráficos que se han realizado. En el siguiente apartado se analizará la información que se observa en cada página.


## Storytelling:<a name="story"/>

<details>
<summary>Festivales y Artistas</summary>
<br>

 ![pag1](./images/pag1.png)

</details>

<br>

En la primera página de nuestra historia podemos ver 2 gráficos de barras que relacionan los aritistas y con los festivales, y un mapa donde se muestran los festivales que tienen lugar en 2023. Esto nos permite tener una primera aproximación a como están estos dos campos relacionados

En el gráfico podemos ver por cada artista el número de festivales en los que participa, así como una medida de su popularidad. Esta popularidad es la media de la populardidad del top 10 de canciones del artista en Spotify.

Tanto el mapa como el gráfico es interactivo y podemos ir explorando tanto artistas como festivales

<br>

<details>
<summary>Popularidad por artista</summary>
<br>

 ![pag2](./images/pag2.png)

</details>

<br>

En la segunda página de nuestra historia podemos ver 2 gráficos de barras donde se ve la media de popularidad de cada artista. En el gráfico de la izquierda podemos observar la popularidad de aquellos artistas que actúan en 4 festivales o menos, y a la derecha igual pero sólo los artistas que actúan en 8 festivales o más.

En ambos gráficos podemos observar una línea horizontal que indica la mediana de popularidad para cada grupo. Vemos que hay una diferencia significativa entre la mediana de ambos grupos. 

¿Afectará la popularidad a que tenga una presencia menor o mayor en festivales?

¿Aparte de la popularidad, habrá otra métrica que pueda afectar a la presencia de un artista en mas o menos festivales?

<br>

<details>
<summary>Popularidad por artista</summary>
<br>

 ![pag3](./images/pag3.gif)

</details>

<br>

En la tercera página de nuestra historia analizaremos el impacto de tres métricas distintas, que otorga [Spotify](https://developer.spotify.com/documentation/web-api/reference/get-several-audio-features) a las canciones, a la hora de aparecer en uno o más festivales.

Las métricas que vamos a analizar son:

* Danceability: Métrica que clasfica una canción por s"u predisposición a ser "bailable"
    > Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.

    * Danceability: Métrica que clasfica una canción por s"u predisposición a ser "bailable"
    > Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.