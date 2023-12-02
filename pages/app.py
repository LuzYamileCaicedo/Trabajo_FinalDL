import streamlit as st
import pandas as pd
import matplotlib as plt


st.set_page_config(page_title="Entrega Final Deep Learning Avanzado - LYCCH",page_icon="-")

st.title("Lectura Inicial Conjunto de Datos")
file = st.file_uploader("File uploader", type=["csv","xlsx"])

if file is not None:
  df = pd.read_csv(file)
  st.write("Datos del archivo:")
  st.dataframe(df)

name_clases={0:"DB", 1:"SS", 2:"SW", 3:"A", 4:"I", 5:"B"}
df['FlowPattern']= df['FlowPattern'].replace(name_clases)

st.subheader("Descripción de los datos")

st.dataframe(df.describe())

st.markdown("---")

def plot_histogram(Column): 
  plt.figure(figsize=(6,4))
  plt.hist(df[Column], bins=20, color='skyblue',edgecolor='black')
  plt.title(titulo)
  plt.title(Column)
  plt.xlabel(Column)
  plt.ylabel('Frequency')
  return plt


st.markdown("---")

col1, col2 = st.columns(2)

with col1:
  st.write("Histograma")
  selected_column = st.selectbox("Seleccione una columna",df.columns)
  st.pyplot(plot_histogram(selected_column,f"Histograma de {selected_column}"))

with col2:
  st.write("Boxplot")
  selected_column_box = st.selectbox("Seleccione otra columna",df.columns)
  st.pyplot(box_plot(selected_column,f"Histograma de {selected_column_box}"))

st.markdown("---")
# Correlación entre variables
st.subheader("Correlación entre Variables:")
correlation_matrix = df.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=.5)
st.pyplot()

st.markdown("---")

def pagina_principal():
      st.title("Página Principal")
      st.write("Bienvenido a la página principal")
      # Agregar un botón para ir a la siguiente página
      if st.button("Ir a la Página Siguiente"):
            #Redirigir a la siguiente página
            st.experimental_rerun()

def pagina_1():
      st.title("Página 1")
      st.write("Estas en la página LD")
      
           
def pagina_2(): 
    st.title("Página 2")
    st.write("Estas en la página EDA")
    
def pagina_3(): 
    st.title("Página 3")
    st.write("Estas en la página EDA-2")
    
# Definir un diccionario con las páginas y sus funciones asociadas
paginas ={
  "Página Principal": pagina_principal,
  "Lectura de Datos LD": pagina_1,
  "EDA ": pagina_2,  
  "EDA-2": pagina_3
  
}
  
      
# Crear una barra lateral con enlaces a las páginas
st.sidebar.title("Opciones de Presentación")
seleccion_pagina = st.sidebar.selectbox("Selecciona una página", list(paginas.keys()))

#Llamar a la función asociada a la página seleccionada
paginas[seleccion_pagina]()


