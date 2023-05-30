# app.py

# Importamos las bibliotecas necesarias
import streamlit as st
import pandas as pd
import requests
import json

st.title('Stream-lit 💯💯')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

# Formulario para introducir datos para la API
with st.form(key='my_form'):
    name_input = st.text_input('Nombre del producto')
    price_input = st.number_input('Precio del producto', min_value=0.00)
    is_offer = st.checkbox('¿En oferta?')

    submit_button = st.form_submit_button(label='Enviar')

# Si el botón ha sido pulsado, hacemos la petición a la API
if submit_button:
    item = {"name": name_input, "price": price_input, "is_offer": is_offer}
    response = requests.post('http://localhost:8000/items/', data=json.dumps(item))
    resp = st.write(response.json())
    print("")
