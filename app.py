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
 

#2 horizontal menu
selected = option_menu(
    menu_title = "Menú principal ------------------------------------------->  jahoperi", #required
    options = ["Inicio", "Proyecto1", "Proyecto2", "CV", "Contacto"], #required
    icons = ["house", "book", "envelope"], #optional
    menu_icon = "cast", #optional
    default_index = 0, #optional
    orientation = "horizontal",
)    



                    
if selected == "Inicio":
   st.title(f"Has seleccionado {selected}")
   st.header("Un poco de comentarios")
   st.subheader("")
   st.subheader("En mi página web se trata de pasarla bien, relax y contribuir en algo con quines están buscando empleo; creando una base de datos por si algún ofertante de alguna vacante quisiera dar un vistazo y tener opciones de candidatos.")
   st.subheader("")
   st.subheader("Son dos los proyectos, ideas, como quieran llamarlos")
   st.subheader("")
   st.subheader("Proyecto1")
   st.subheader("jahoperi Chusconoticias")
   st.subheader("")
   st.subheader("He creado un canal en Youtube")
   st.subheader("Si es de tu agrado el canal, te invito a suscribirte, dejar tus comentarios y compartir")
   st.subheader("")
   st.subheader("")
   st.subheader("Proyecto2") 
   st.subheader("He creado una página web, donde todo aquel o aquella que este buscando empleo, puede dejar sus datos")
   
   
if selected == "Proyecto1":
   st.title(f"Has seleccionado {selected}") 
   st.subheader("Aquí pegaré los link conforme vaya subiendo mis videos")
   st.subheader("")
   st.subheader("3/04/2022")
   st.subheader("")
   st.subheader("https://www.youtube.com/watch?v=1o9LDCbL8_U")
if selected == "Proyecto2":
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
      st.subheader("Gracias a Dios, ya tengo empleo")
      
      
if selected == "Contacto":
   st.title(f"Has seleccionado {selected}") 
   st.subheader("Les dejo mi correo electrónico")
   st.subheader("jahoperi@gmail.com")


                
