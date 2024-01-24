import streamlit as st
from Home import load_data
import datetime

grd_villes = ['Paris', 'Avignon', 'Bordeaux', 'Lille', 'Lyon', 'Marseille',
              'Montpellier', 'Nantes', 'Nice', 'Toulouse']

depart = st.selectbox('Départ', grd_villes, index=grd_villes.index('Paris'))
arrivee = st.selectbox('Arrivée', grd_villes + ['Toutes'])
date_depart = st.date_input('Date de départ', min_value=datetime.date.today())

df = load_data()

tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8, tab9, tab10 = st.tabs(grd_villes)