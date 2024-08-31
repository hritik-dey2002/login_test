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
    original_title1 ='<p style="font-family:Arial Nova; font-size: 25px;"><b>Welcome to User Side</b></p>'
    st.markdown(original_title1, unsafe_allow_html=True)


    pdf_file = st.file_uploader("Choose your Resume", type=["pdf"])
    if st.button("Submit Resume", type="primary"):
        if pdf_file is not None:
            # save_image_path = './Uploaded_Resumes/' + pdf_file.name
            # with open(save_image_path, "wb") as f:
            #     f.write(pdf_file.getbuffer())
            resume_data = ResumeParser(pdf_file).get_extracted_data()
            # data2 = resumeparse.read_file(save_image_path)
            # text = extract_text(save_image_path)
            # st.text(text)
            if resume_data:
                with st.spinner('Uploading Your Resume...'):
                    time.sleep(2)
                st.header("**Resume Analysis**")
                st.success("Congratulations " + resume_data['name'] +' . your resume has been submitted')
                st.subheader("**Candidates Basic info**")
                try:
                    st.text('Name: ' + resume_data['name'])
                    st.text('Email: ' + resume_data['email'])
                    # st.text('Resume pages: ' + str(resume_data['no_of_pages']))
                    st.text('Experience: ' + str(resume_data['total_experience']))
                except:
                    pass

                ts = time.time()
                cur_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                cur_time = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                timestamp = str(cur_date + '_' + cur_time)

                st.balloons()

                delete_data(resume_data['email'])

                insert_data(resume_data['name'], resume_data['email'], timestamp,
                    str(resume_data['total_experience']), str(resume_data['skills']),0)

                connection.commit()

            else:
                st.error(":red[Somethings went wrong.....]")
        else:
            st.warning(':red[Warning message]')
            st.error(":red[Upload the resume]")