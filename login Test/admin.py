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
import mysql.connector
import plotly.express as px
from plotly import optional_imports

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
def app():
    original_title1 ='<p style="font-family:Arial Nova; font-size: 25px;"><b>Welcome Admin</b></p>'
    st.markdown(original_title1, unsafe_allow_html=True)
    admin_user=st.text_input("Username")
    admin_password=st.text_input("Password",type='password')
    if st.button('login'):
        with st.spinner(':blue[Wait for it...]'):
            time.sleep(2)
        if admin_user=='admin' and admin_password=='admin123':
            st.success(":blue[Welcome Admin]")
            cursor.execute('''SELECT*FROM user_data11''')
            data = cursor.fetchall()
            st.header("**User's Data**")
            df = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'Timestamp', 'Experience', 'Actual Skills','Count'])
            df_filtered = df.drop(columns=['Count'])
            st.dataframe(df_filtered)
            st.balloons()

        else:
            st.error(":red[Wrong ID & Password Provided]")