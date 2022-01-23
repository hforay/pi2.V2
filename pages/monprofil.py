import streamlit as st

def app():
      menu = st.selectbox("Mon profil",["Mes commentaires","Mes notes"])
      if menu == "Mes commentaires":
            st.subheader("Mes commentaires")

      elif menu == "Mes notes":
            st.subheader("Mes notes")