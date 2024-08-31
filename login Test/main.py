import time
import streamlit as st
from streamlit_option_menu import option_menu
import spacy
spacy.load('en_core_web_sm')

import pandas as pd
import time, datetime
from pyresparser import ResumeParser
from resume_parser import resumeparse
from streamlit_tags import st_tags
from PIL import Image
# import pymysql
import mysql.connector
import plotly.express as px
from plotly import optional_imports
import admin, company, user

connection = mysql.connector.connect(host='localhost', user='root', password='',database='sra3')
cursor = connection.cursor()


def insert_data(name, email, timestamp, exp, skills,count):
    DB_table_name = 'user_data11'
    insert_sql = "insert into " + DB_table_name + """
    values (0,%s,%s,%s,%s,%s,%s)"""
    rec_values = (name, email, timestamp, str(exp), skills,count)
    cursor.execute(insert_sql, rec_values)
    connection.commit()

def delete_data(email):
    DB_table_name = 'user_data11'
    delete_sql = f"DELETE FROM {DB_table_name} WHERE email_id = %s"
    cursor.execute(delete_sql, (email,))
    connection.commit()

def run():

    original_title ='<p style="font-family:Cooper Black; font-size: 50px;"><b>Smart Resume Screening</b></p>'
    st.markdown(original_title, unsafe_allow_html=True)
    with st.sidebar:        
        choice = option_menu(
            menu_title='Choose Mode ',
            options=['User','Admin','Company'],
            icons=['person-circle','info-circle-fill','house-fill'],
            menu_icon='chat-text-fill',
            default_index=0,
            styles={
                "container": {"padding": "5!important","background-color":'black'},
    "icon": {"color": "white", "font-size": "23px"}, 
    "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
    "nav-link-selected": {"background-color": "#02ab21"},}
            )
    # st.title(":green[Smart Resume Screening]")
    # st.sidebar.markdown("Choose User")
    # activities = ["User 🧑🏻‍💻", "Admin 👤","Company 🏢"]
    # choice = st.sidebar.selectbox("Choose among the given options:", activities)

    # Create the DB
    # db_sql = """CREATE DATABASE IF NOT EXISTS SRA3;"""
    # cursor.execute(db_sql)
    # connection.select_db("sra4")

    # Create table
    DB_table_name = 'user_data11'
    table_sql = "CREATE TABLE IF NOT EXISTS " + DB_table_name + """
                    (ID INT NOT NULL AUTO_INCREMENT,
                     Name varchar(100) NOT NULL,
                     Email_ID VARCHAR(50) NOT NULL,
                     Timestamp VARCHAR(50) NOT NULL,
                     Experience VARCHAR(10) NOT NULL,
                     Actual_skills VARCHAR(300) NOT NULL,
                     Count INT(5) NOT NULL,
                     PRIMARY KEY (ID));
                    """
    cursor.execute(table_sql)

    if choice == 'User':
        user.app()
    elif choice == 'Admin':
        admin.app()
    else:
        company.app()

run()