import streamlit as st
from PIL import Image
from multipage import MultiPage
from utilisateur import Utilisateur
import sqlite3
import streamlit as st
import pandas as pd
from pages import decision 
from pages import monprofil
from pages import uploadfiles
from pages import app1
from pages import visualisationPM1

from hydralit import HydraApp
import hydralit as hy
import hashlib



app = MultiPage()

nav = hy.HydraApp(title='Simple Multi-Page App',hide_streamlit_markers=True,use_navbar=True, navbar_sticky=True)

image = Image.open("Image1.png")
st.image(image,width=1400)

def make_hashes(password):
      return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed_text):
      if make_hashes(password) == hashed_text:
            return hashed_text
      return False

conn = sqlite3.connect('data.db',check_same_thread=False)
c = conn.cursor()

def create_usertable():
      c.execute('CREATE TABLE IF NOT EXISTS userstable(username TEXT,password TEXT)')

def add_userdata(username,password):
      c.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
      conn.commit()

def login_user(username,password):
      c.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
      data = c.fetchall()
      return data

def view_all_users():
      c.execute('SELECT * FROM userstable')
      data = c.fetchall()
      return data

def main():
      """Login"""
      menu = ["Login","SignUp"]
      choice = st.sidebar.selectbox("Login / SignUp",menu)

      if choice == "Login":
            username = st.sidebar.text_input("User Name")
            password = st.sidebar.text_input("Password",type='password')
            if st.sidebar.checkbox("Login"):
                create_usertable()
                hashed_pswd = make_hashes(password)
                result = login_user(username,check_hashes(password,hashed_pswd))
                if result:
                  @nav.addapp(is_home=True)
                  def mon_profil():
                        app.add_page("Mon profil", monprofil.app)
                        app.run()

                  @nav.addapp(title='Upload Data')
                  def upload_data():
                        app.add_page("Upload Data", uploadfiles.app)
                        app.run()

                  @nav.addapp(title='Visualisation csv files')
                  def visualisation_csv_files():
                        app.add_page("Visualisation csv files", app1.app)
                        app.run()

                  @nav.addapp(title='Visualisation Access Database')
                  def visualisation_access_database():
                        app.add_page("Visualisation Access Database", visualisationPM1.app)
                        app.run()

                  @nav.addapp(title='Decision')
                  def decision_app():
                        app.add_page("Decision", decision.app)
                        app.run()
            
                  nav.run()
                  st.sidebar.success("Connecté sur le profil : {}".format(username))
                              
                else:
                    st.warning("Incorrect Username/Password")


      elif choice == "SignUp":
            st.subheader("Create New Account")
            new_user = st.text_input("Username")
            new_password = st.text_input("Password",type='password')
            first_name = st.text_input("First Name")
            last_name = st.text_input("Last Name")
            expertise = st.radio(
                "How would you rate your level of expertise between 0 and 5?",
                ('0', '1', '2','3','4','5'))
            accessibility = st.radio(
                "What is your level of accessibility?", 
                ('0', '1', '2','3','4','5'))

            if st.button("Signup"):
                create_usertable()
                add_userdata(new_user,make_hashes(new_password))
               
                st.success("You have successfully created a valid Account")
                st.info("Go to Login Menu to login")

if __name__ == "__main__":
      main()
