Acerca del conjunto de datos
Contexto
Este es un conjunto de datos históricos sobre los Juegos Olímpicos modernos, que incluye todos los Juegos desde Atenas 1896 hasta Río 2016. Extraje estos datos de www.sports-reference.com en mayo de 2018. El código R que utilicé para extraer y ordenar los datos está en GitHub. Recomiendo verificar mi kernel antes de comenzar su propio análisis.

Cabe señalar que los Juegos de Invierno y de Verano se celebraron el mismo año hasta 1992. Después de eso, los escalonaron de modo que los Juegos de Invierno se celebren en un ciclo de cuatro años a partir de 1994, luego los de Verano en 1996, luego los de Invierno en 1998, y así sucesivamente. Un error común que se comete al analizar estos datos es suponer que los Juegos de Verano y de Invierno siempre se han escalonado.

Contenido
El archivo athlete_events.csv contiene 271116 filas y 15 columnas. Cada fila corresponde a un atleta individual que compite en un evento olímpico individual (athlete-events). Las columnas son:

ID - Número único para cada deportista
Nombre - Nombre del atleta
Sexo - M o F
Edad - Entero
Altura - En centímetros
Peso - En kilogramos
Equipo - Nombre del equipo
CON - Comité Olímpico Nacional Código de 3 letras
Juegos - Año y temporada
Año - Entero
Temporada - Verano o Invierno
Ciudad - Ciudad anfitriona
Deporte - Deporte
Evento - Evento
Medalla : Oro, Plata, Bronce o NA
Expresiones de gratitud
Los datos olímpicos de www.sports-reference.com son el resultado de una increíble cantidad de investigación realizada por un grupo de entusiastas de la historia olímpica y autoproclamados "estadísticos". Visite su blog para obtener más información. Todo lo que hice fue consolidar sus décadas de trabajo en un formato conveniente para el análisis de datos.

Inspiración
Este conjunto de datos brinda la oportunidad de plantear preguntas sobre cómo han evolucionado los Juegos Olímpicos a lo largo del tiempo, incluidas preguntas sobre la participación y el desempeño de las mujeres, las diferentes naciones y los diferentes deportes y eventos.