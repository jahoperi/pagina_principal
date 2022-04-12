# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 16:13:50 2022

@author: jahop_fz60h0
"""
import json
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie  # pip install streamlit-lottie
import streamlit.components.v1 as components
import requests  # pip install requests

from PIL import Image

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
    



lottie_hello = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_ipvphpwo.json")




st_lottie(lottie_hello, key = "hello")



#1 as sidebar menu

#with st.sidebar:
#      selected = option_menu(
#          menu_title = "Main Menu", #requerid
#          options = ["Home", "Projects", "Contact"], #required
#          icons = ["house","book", "envelope"], #optional
#          menu_icon = "cast", #optional
#          default_index = 0,
#      )

#1 vertical menu
selected = option_menu(
    menu_title = "Menú principal -------------------------->  jahoperi", #required
    options = ["Inicio", "Mi canal de Youtube Chusconoticias", "La noticia del día", "Ciencia y tecnología", "Buscamos empleo", "CV", "Contacto"], #required
    icons = ["house", "book", "envelope"], #optional
    menu_icon = "cast", #optional
    default_index = 0, #optional
    
    ) 

 

#2 horizontal menu
#selected = option_menu(
#    menu_title = "Menú principal ------------------------------------------->  jahoperi", #required
#    options = ["Inicio", "Proyecto1", "Proyecto2", "CV", "Contacto"], #required
#    icons = ["house", "book", "envelope"], #optional
#    menu_icon = "cast", #optional
#    default_index = 0, #optional
#    orientation = "horizontal",
#)    



                    
if selected == "Inicio":
   st.title(f"Has seleccionado {selected}")
   st.header("Un poco de comentarios")
   st.subheader("")
   st.subheader("En mi página web se trata de pasarla bien, relax y contribuir en algo con los que estamos desempleados; creando una base de datos por si algún ofertante de alguna vacante quisiera dar un vistazo y tener opciones de candidatos.")
   st.subheader("")
   
   
if selected == "Mi canal de Youtube Chusconoticias":
   st.title(f"Has seleccionado {selected}") 
   st.subheader("Aquí pegaré los link conforme vaya subiendo mis videos")
   st.subheader("")
   st.subheader("03/04/2022")
   st.subheader("")
   st.subheader("https://www.youtube.com/watch?v=1o9LDCbL8_U")
   st.subheader("")
   st.subheader("12/04/2022")
   st.subheader("")
   st.subheader("https://www.youtube.com/watch?v=NAFDPzwhEyw") 
   

if selected == "La noticia del día":
      st.title(f"Has seleccionado {selected}") 
      st.subheader("Para que estes bien informado")
      st.subheader("11/04/2022")
      st.subheader("Revocación de mandato")
      image = Image.open('imagen1.jpg')
      st.image(image, caption='Ayer fui a votar, por ya sabes quien')  
      

if selected == "Ciencia y tecnología":
      st.title(f"Has seleccionado {selected}") 
      st.subheader("Los últimos avances en cuanto a conocimientos científicos y tecnológicos")
      st.subheader("11/04/2022")
      image = Image.open('imagen2.jpg')
      st.image(image, caption='Historia del almacenamiento de datos')       


if selected == "Buscamos empleo":
      st.title(f"Has seleccionado {selected}")
      st.subheader("Aquí el link de la página web para que puedas dejar tus datos.")
      st.subheader("Si eres de Recursos Humanos puedes realizar una búsqueda de algún candidato.")
      st.subheader("En ambos casos, se les solicita una cuenta de google para que puedan acceder; se envían a tu móvil unos códigos de seguridad")
      st.subheader("https://script.google.com/macros/s/AKfycbzl-x0R01nl9JmNM5lZHd9LR-qtGmuEHwMY0sWARwzGrsvLmN802O8b7_LO7LFbzN70yA/exec")
      st.subheader("")
      st.subheader("")
      st.subheader("Aquí el link de la base de datos")
      st.subheader("https://obscure-anchorage-34419.herokuapp.com/")

if selected == "CV":
      st.title(f"Has seleccionado {selected}") 
      st.subheader("Aqui puedes ver o descargar mi CV")
      st.subheader("https://tranquil-springs-16213.herokuapp.com/")
      
      
      
if selected == "Contacto":
   st.title(f"Has seleccionado {selected}") 
   st.subheader("Les dejo mi correo electrónico puedes escribir con toda confianza y respeto")
   st.subheader("jahoperi@gmail.com")


                
                
