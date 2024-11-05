import streamlit as st
import pandas as pd
from prophet import Prophet
from PIL import Image
import plotly.graph_objects as go
import random

# Importamos los datasets
df = pd.read_csv("Data.app\df_PBI.csv")
df2 = pd.read_csv("Data.app\df_poblacion.csv")

# Icono de la página 
img = Image.open("Imagenes\olimpo.png")

# Título de la página 
st.set_page_config(page_title = "Olimpo de los Datos", page_icon = img)

# Navegador de páginas 
menu = ["Inicio", "Predición Población", "Predioción PBI", "Analisis Deportivo JJOO"]
elecion = st.sidebar.selectbox("Navegación", menu)

# Personalización de colores
st.markdown("""
    <style>
    .stApp {
        background-image: url('https://i.postimg.cc/8CqVrSpG/Fondo.jpg');
        background-size: cover;
        background-position: center;
    }
    </style>
    """, unsafe_allow_html=True)


st.write("""
    <style>
    .stSidebar div {
        color: #F2AB27;
    }
    </style>
    """, unsafe_allow_html=True)

st.write("""
    <style>
    .stSelectbox div {
        color: #C2FFF7;
    }
    </style>
    """, unsafe_allow_html=True)

st.write("""
<style>
.stMultiSelect div {
color: #C2FFF7
}
</style>
""", unsafe_allow_html=True)


st.write("""
<style>
.stSlider div {
color: #F2AB27
}
</style>
""", unsafe_allow_html=True)


def predic_uno(pais, anos_a_predecir, df, columna):

        # Filtrar los datos por país
        data = df[df['Country Name'] == pais]
        data.dropna(inplace = True)
            
        # Crear un DataFrame para Prophet
        df_prophet = pd.DataFrame({'ds': data['Year'], 'y': data[columna]})

        # Crear y ajustar el modelo Prophet
        model = Prophet()
        model.fit(df_prophet)

        # Obtener los años existentes en el dataset
        anos_existentes = sorted(data['Year'].unique())

        # Crear un DataFrame con los años a predecir (solo los que no existen)
        anos_a_predecir_unicos = [ano for ano in range(anos_existentes[0], anos_existentes[-1]+anos_a_predecir+1)]
        future = pd.DataFrame({'ds': anos_a_predecir_unicos})

        # Realizar la predicción
        forecast = model.predict(future)

        # Seleccionar solo las columnas de interés
        forecast = forecast[['ds', 'yhat']]
        forecast['ds'] = forecast['ds'].dt.year

        # Graficar la predicción
        df_real = df[df['Country Name'] == pais]
        df_real.dropna(inplace = True)
        
        # Crea una figura
        fig = go.Figure()

    
        # Agrego las variables
        fig.add_trace(go.Scatter(x = df_real['Year'], y = df_real[columna], name = "Real", line = dict(color = "blue")))
        fig.add_trace(go.Scatter(x = forecast['ds'], y = forecast['yhat'], name = columna, line = dict(color = "red")))
        fig.update_layout(xaxis_title="Años", yaxis_title = columna, plot_bgcolor='#F2E8C9')
        fig.update_layout(
        xaxis=dict(
        gridcolor='#F2AB27',  # Color de las líneas de la cuadrícula del eje x
        showgrid=True,          # Mostrar/ocultar la cuadrícula
        ),
        yaxis=dict(
        gridcolor='#F2AB27',
        showgrid=True,
        ))
        st.plotly_chart(fig)

        return None


def predic_multiple(pais, anos_a_predecir, df, columna):

    # Filtrar los datos por país
    data = df[df['Country Name'] == pais]
    data.dropna(inplace = True)
            
    # Crear un DataFrame para Prophet
    df_prophet = pd.DataFrame({'ds': data['Year'], 'y': data[columna]})

    # Crear y ajustar el modelo Prophet
    model = Prophet()
    model.fit(df_prophet)

    # Obtener los años existentes en el dataset
    anos_existentes = sorted(data['Year'].unique())

    # Crear un DataFrame con los años a predecir (solo los que no existen)
    anos_a_predecir_unicos = [ano for ano in range(anos_existentes[0], anos_existentes[-1]+anos_a_predecir+1)]
    future = pd.DataFrame({'ds': anos_a_predecir_unicos})

    # Realizar la predicción
    forecast = model.predict(future)

    # Seleccionar solo las columnas de interés
    forecast = forecast[['ds', 'yhat']]
    forecast['ds'] = forecast['ds'].dt.year

    # Retorno la predicción 
    return forecast


def multiples(año_multiple, paises, data, columna_P):

    try:
        # Creó una figura y guardo los colores usados
        fig = go.Figure()
        colores_usados = []

        # Recorro los países y hago sus predicciones 
        for i in paises:
            predic = predic_multiple( i, año_multiple, data, columna_P)
                
            color_aleatorio = None
            # seleccionar colores random    
            while color_aleatorio is None or color_aleatorio in colores_usados:
                color_aleatorio = f'rgb({random.randint(0, 255)}, {random.randint(0, 255)}, {random.randint(0, 255)})'

            # Guardo los colores usados 
            colores_usados.append(color_aleatorio)
            
            # Agrego la linea de la predicción 
            fig.add_trace(go.Scatter(x=predic['ds'], y=predic['yhat'],name=f"Predicción {i}",line=dict(color=color_aleatorio)))
        
        # Gráfico final
        fig.update_layout(xaxis_title="Años", yaxis_title = columna_P, plot_bgcolor='#F2E8C9')
        fig.update_layout(
        xaxis=dict(
        gridcolor='#F2AB27',  # Color de las líneas de la cuadrícula del eje x
        showgrid=True,          # Mostrar/ocultar la cuadrícula
        ),
        yaxis=dict(
        gridcolor='#F2AB27',
        showgrid=True,
        ))    
        st.plotly_chart(fig)

    except:
        return st.write("Ingrese paises (Maximo 5).") 

    return None



# Página 1
if elecion == "Predición Población":

    st.markdown("# <center><font color='#F2AB27'>Predicciones Población</font></center>", unsafe_allow_html=True)
    st.markdown("## <font color='#F2AB27'>¡Descubre el futuro de la población mundial!</font>", unsafe_allow_html=True)
    
    st.markdown("## <font color='#F2AB27'>Función Comparación Historica:</font>", unsafe_allow_html=True)
    st.markdown(" <font color='#F2E8C9'>La siguiente función muestra los datos historicos del pais eleguido y los compara con la predicion de los años pasados y futuro.</font>", unsafe_allow_html=True)


    lista_pais = []

    for pais in df["Country Name"].unique():
        lista_pais.append(str(pais))

    opcion_pais_2 = st.selectbox("Seleccione el Pais deseado:", lista_pais)


    año_pais_2 = st.slider("Años a predecir:", min_value = 1, max_value = 20, value = 5, step = 1)

    predic_uno(opcion_pais_2, año_pais_2, df2, "Population")

    st.markdown("## <font color='#F2AB27'>Función Comparación Multiple de la población:</font>", unsafe_allow_html=True)
    st.markdown("<font color='#F2E8C9'>En esta funcion eleguimos los paises que queremos para comparar sus prediciones y de esta forma tener un contexto mas amplio.</font>", unsafe_allow_html=True)

    opcion_multiple_2 = st.multiselect("Elija paises para comparar (Min: 1, Max: 5):",lista_pais, max_selections = 5)

    año_multiple_2 = st.slider("Años a predecir:", min_value = 1, max_value = 15, value = 5, step = 1)


    multiples(año_multiple_2, opcion_multiple_2, df2, "Population")


# Página 2
elif elecion == "Predioción PBI":

    st.markdown("# <center><font color='#F2AB27'>Predicciones PBI</font></center>", unsafe_allow_html=True)
    st.markdown("## <font color='#F2AB27'>¡Descubre el futuro de la economía mundial!</font>", unsafe_allow_html=True)
    st.markdown("### <font color='#Fe0000'>¡Atención!: Devido al comportamiento erratico de los datos, o la carencia de los mismos, las prediciones puden ser menos presisa o incoerentes.</font>", unsafe_allow_html=True)

    st.markdown("## <font color='#F2AB27'>Función Comparación Historica:</font>", unsafe_allow_html=True)
    st.markdown(" <font color='#F2E8C9'>La siguiente función muestra los datos historicos del pais eleguido y los compara con la predicion de los años pasados y futuro.</font>", unsafe_allow_html=True)

    lista_PBI = []

    for pais in df["Country Name"].unique():
        lista_PBI.append(str(pais))

    opcion_PBI = st.selectbox("Seleccione el Pais deseado:", lista_PBI)


    año_PBI = st.slider("Años a predecir:", min_value = 1, max_value = 20, value = 5, step = 1)


    predic_uno(opcion_PBI, año_PBI, df, "PBI")

    st.markdown("## <font color='#F2AB27'>Función Comparación Multiple:</font>", unsafe_allow_html=True)
    st.markdown("<font color='#F2E8C9'>En esta funcion eleguimos los paises que queremos para comparar sus prediciones y de esta forma tener un contexto mas amplio.</font>", unsafe_allow_html=True)
    
    opcion_multiple = st.multiselect("Elija paises para comparar (Min: 1, Max: 5):",lista_PBI, max_selections = 5)

    año_multiple = st.slider("Años a predecir:", min_value = 1, max_value = 15, value = 5, step = 1)


    multiples(año_multiple, opcion_multiple, df, "PBI")


# Página 3
elif elecion == "Analisis Deportivo JJOO":
    st.markdown("# <center><font color='#F2AB27'>Analisís Deportivo JJOO</font></center>", unsafe_allow_html=True)

    # Dashboard
    st.components.v1.iframe(
        src="https://app.powerbi.com/view?r=eyJrIjoiNzI0MjkzNGQtMDgyMS00OTliLWEyYTYtMzM3YmJmNTQ2NzMxIiwidCI6IjcxOWU4ZTRkLWZkZDMtNDQxZC05NDcyLTM0MDAxNGJiMTM1NyIsImMiOjR9",
        width=800,  # Ancho del iframe
        height=500,  # Alto del iframe
        scrolling=True  # Habilitar el scrolling si el contenido es grande
    )




# Página de inicio
else:
    st.markdown("# <center><font color='#F2AB27'>Olimpo de los Datos</font></center>", unsafe_allow_html=True)
    
    st.markdown("## <center><font color='#F2E8C9'>¡Bienvenido Usuario!</font></center>", unsafe_allow_html=True)
    
    # Centrar la imagen
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("Imagenes\Robot.png", width = 300)

    st.markdown("### <center><font color='#F2AB27'>Permitime contarte un poco sobre nuestra aplicación web:</font></center>", unsafe_allow_html=True)
    st.markdown(""" #### <center><font color='#F2E8C9'> **¡Descubre el futuro hoy!** En el Olimpo de los Datos encontrarás las herramientas que necesitas para proyectar el crecimiento económico y demográfico de cualquier país. ¿Quieres saber cómo será el PIB de tu país en 5 años? ¿O cuál será la población mundial en 2030? Explora nuestras secciones de Predicción del PIB y Predicción de Población y descubre las tendencias que darán forma al mundo.</font></center>""", unsafe_allow_html=True)
    
    st.markdown(""" #### <center><font color='#F2E8C9'>Para las prediciones de Poblacion y PBI, la aplicación utiliza Machine Learning, empleando el algoritmo Prophet de Facebook para generar predicciones precisas. Basándose en datos históricos, identifica patrones y tendencias, permitiendo anticipar futuros comportamientos y tomar decisiones más informadas.</font></center>""", unsafe_allow_html=True)
    
    st.markdown(""" #### <center><font color='#F2E8C9'>Esta aplicación web fue creada con el objetivo de analizar y encontrar si existe una correlación entre los resultados obtenidos de los países en los juegos Olímpicos, su PBI y población. Este análisis se puede encontrar en la última página (Analisis Deportivo JJOO) junto con un dashboard interactivo y sus conclusiones.</font></center>""", unsafe_allow_html=True)

    st.markdown(""" ### <center><font color='#F2AB27'>Conoce a mis creadores:</font></center>""", unsafe_allow_html=True)

    st.markdown(""" ##### <font color='#F2E8C9'> Eugenia Memolli | Roll: Data Scientist | Tareas: ETL, EDA, Creación del Dashboard.</font>""", unsafe_allow_html=True)
    st.markdown(""" ##### <font color='#F2E8C9'>Matías Sosa | Roll: Data Scientist | Tareas: Creación de funciones con Machine Learning y desarrollo de aplicación web </font>""", unsafe_allow_html=True)

    # Centrar la imagen
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image("Imagenes\olimpo.png", width = 300)


    