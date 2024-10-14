# Rendimiento Olímpico y Políticas Públicas Comparadas 

## Introducción: 
El objetivo de este estudio es analizar la historia de los Juegos Olímpicos y compararla con datos de población y Producto Bruto Interno (PBI) de cada país. A partir de esta información, se pretende identificar qué países comparten características socioeconómicas similares a las de Argentina y evaluar su desempeño en los Juegos Olímpicos.

Posteriormente, se investigará si estos países implementan políticas públicas similares en relación con el deporte, así como las diferencias que puedan existir. Se realizará un análisis de los países mejor posicionados en los Juegos Olímpicos, explorando qué políticas públicas aplican para fomentar el deporte.

Además, se evaluará cómo el nivel socioeconómico influye en la implementación de estas políticas deportivas y en qué medida impacta en el rendimiento olímpico. La finalidad es comprender las  relaciones entre las políticas públicas, el fomento del deporte y los resultados obtenidos en competiciones internacionales, considerando el contexto socioeconómico de cada nación

## Índice
1. [Introducción](#introducción)
2. [Descripción de los Datasets](#descripción-de-los-datasets)
3. [Extracción, Carga y Transformación de los Datos (ETL)](#extracción-carga-y-transformación-de-los-datos-etl)
4. [Análisis Exploratorio de los Datos (EDA)](#análisis-exploratorio-de-los-datos-eda)
5. [Producción del Dashboard](#producción-del-dashboard)
6. [Conclusión](#conclusión)

## Descripción de los Datasets

Para este proyecto, se trabajó con los siguientes conjuntos de datos:

- **athlete_events**: Este es un conjunto de datos históricos sobre los Juegos Olímpicos modernos, que incluye todos los Juegos desde Atenas 1896 hasta Río 2016. Los datos fueron extraídos de [www.sports-reference.com](https://www.sports-reference.com) en mayo de 2018.

- **Población Mundial y PBI**: Los datos sobre la población mundial y el Producto Bruto Interno (PBI) fueron extraídos de la página del **Banco Mundial** ([www.worldbank.org](https://www.worldbank.org)).


## Extracción, Carga y Transformación de Datos (ETL)

Para este proyecto, se utilizó la librería **Pandas** como herramienta principal para llevar a cabo el proceso de ETL. A continuación, se detallan las transformaciones realizadas en los datos:

1. **Filtrado de Datos**: Se eliminó del conjunto de datos `df_JJOO` toda información anterior al año **1960**, ya que los datos disponibles del Banco Mundial comienzan en esa fecha. Además, se excluyeron los Juegos Olímpicos de invierno, ya que el análisis se centrará únicamente en los Juegos de verano.

2. **División del DataFrame**: Se separó el DataFrame original `df_JJOO` en dos conjuntos: `df_JJOO` (para eventos) y `df_sportsman` (para deportistas).

3. **Limpieza de Datos**: Se eliminaron todas las filas que no correspondían a países en todos los conjuntos de datos, garantizando así la calidad de la información.

4. **Eliminación de Columnas Irrelevantes**: Se quitaron las columnas que no eran necesarias para el análisis, simplificando así el conjunto de datos.

5. **Transformación de Años**: Las columnas correspondientes a los años (1960 a 2020) se consolidaron en una nueva columna denominada **Years**.

6. **Creación de una Columna de Década**: Se añadió una columna de **decade** en los DataFrames `df_poblacion` y `df_PBI` para facilitar futuros análisis sobre tendencias temporales.

7. **Reinicio de Índices**: Finalmente, se reiniciaron los índices de todos los DataFrames para asegurar una mejor organización y accesibilidad a los datos.

