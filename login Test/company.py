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



    original_title1 ='<p style="font-family:Arial Nova; font-size: 25px;"><b>Welcome to Company Side</b></p>'
    st.markdown(original_title1, unsafe_allow_html=True)

        # st.header(":blue[Welcome to Company Side]")
    company_user=st.text_input("Username")
    company_password=st.text_input("Password",type='password')
    load=st.button('login')
        #initialize session state
    if "load_state" not in st.session_state:
        st.session_state.load_state= False
    if load or st.session_state.load_state:
        st.session_state.load_state=True
        if company_user=='company' and company_password=='company123':
            st.success(":blue[Welcome Company]")
                        
            # activities = ["Web Development", "Python Development", "Java Development", "Data Scientist", "Full Stack Development","Android Development"]
            # choice1 = st.selectbox("Choose required domain:", activities)
            # st.write("You selected:", choice1)
            choice1 = option_menu(
                menu_title="Choose Required Domain", 
                options=["Web Development", "Python Development", "Java Development", "Data Scientist", "Full Stack Development","Android Development"],     
                menu_icon="chat-text-fill",  
                default_index=0, 
                styles={
                    "container": {"padding": "5!important", "background-color": "black"},
                    "nav-link": {
                        "color": "white",
                        "font-size": "10px",
                        "text-align": "left",
                        "margin": "0px",
                        "--hover-color": "blue",
                    },
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )
            st.write(f"You selected: {choice1}")
            cursor.execute('''SELECT Actual_skills FROM user_data11''')
            data = cursor.fetchall()
            cursor.execute('''SELECT Email_ID FROM user_data11''')
            data2 = cursor.fetchall()
            if choice1=="Web Development":
                options = st.multiselect(
                    "Choose the required fields",
                    ["java script", "HTML", "CSS","React","PHP"],
                    ["HTML"],
                )
                li=options
                l=[]
                for x in data:
                    # print(x)
                    for y in x:
                        converted_list = eval(y)
                        c=0
                        lowercase_list = [item.lower() for item in converted_list]
                        # print("list: ",lowercase_list)
                        for i in range(len(li)):
                            # print(li[i].lower())
                            if li[i].lower() in lowercase_list:
                                c=c+1
                        
                        l.append(c)
                emails_list = [email[0] for email in data2]
                result = dict(zip(emails_list, l))
                for email, value in result.items():
                    # cursor.execute("UPDATE user_data11 SET Count = %s WHERE Email_ID = ?", (value, email))
                    delete_sql = f"UPDATE {DB_table_name} SET Count = %s WHERE Email_ID = %s"
                    cursor.execute(delete_sql, (value,email,))
                    connection.commit()
                # print("You selected:", options)

            elif choice1=="Python Development":
                options = st.multiselect(
                    "Choose the required fields",
                    ["python", "Django", "Flask","Tkinter"],
                    ["python"],
                )
                li=options
                l=[]
                for x in data:
                    # print(x)
                    for y in x:
                        converted_list = eval(y)
                        c=0
                        lowercase_list = [item.lower() for item in converted_list]
                        # print("list: ",lowercase_list)
                        for i in range(len(li)):
                            # print(li[i].lower())
                            if li[i].lower() in lowercase_list:
                                c=c+1
                        l.append(c)
                emails_list = [email[0] for email in data2]
                result = dict(zip(emails_list, l))
                for email, value in result.items():
                    # cursor.execute("UPDATE user_data11 SET Count = ? WHERE Email_ID = ?", (value, email))
                    delete_sql = f"UPDATE {DB_table_name} SET Count = %s WHERE Email_ID = %s"
                    cursor.execute(delete_sql, (value,email,))
                    connection.commit()
                # st.write("You selected:", options)

            elif choice1=="Java Development":
                options = st.multiselect(
                    "Choose the required fields",
                    ["core java", "JSP", "Servlet","Spring boot"],
                    ["core java"],
                )
                li=options
                l=[]
                for x in data:
                    # print(x)
                    for y in x:
                        converted_list = eval(y)
                        c=0
                        lowercase_list = [item.lower() for item in converted_list]
                        # print("list: ",lowercase_list)
                        for i in range(len(li)):
                            # print(li[i].lower())
                            if li[i].lower() in lowercase_list:
                                c=c+1
                        l.append(c)
                emails_list = [email[0] for email in data2]
                result = dict(zip(emails_list, l))
                for email, value in result.items():
                    # cursor.execute("UPDATE user_data11 SET Count = ? WHERE Email_ID = ?", (value, email))
                    delete_sql = f"UPDATE {DB_table_name} SET Count = %s WHERE Email_ID = %s"
                    cursor.execute(delete_sql, (value,email,))
                    connection.commit()
                # st.write("You selected:", options)
            
            elif choice1=="Data Scientist":
                options = st.multiselect(
                    "Choose the required fields",
                    ["Mechine Learning", "Python", "AI","NLP","Deep Learning"],
                    ["AI"],
                )
                li=options
                l=[]
                for x in data:
                    # print(x)
                    for y in x:
                        converted_list = eval(y)
                        c=0
                        lowercase_list = [item.lower() for item in converted_list]
                        # print("list: ",lowercase_list)
                        for i in range(len(li)):
                            # print(li[i].lower())
                            if li[i].lower() in lowercase_list:
                                c=c+1
                        l.append(c)

                emails_list = [email[0] for email in data2]
                result = dict(zip(emails_list, l))
                for email, value in result.items():
                    # cursor.execute("UPDATE user_data11 SET Count = ? WHERE Email_ID = ?", (value, email))
                    delete_sql = f"UPDATE {DB_table_name} SET Count = %s WHERE Email_ID = %s"
                    cursor.execute(delete_sql, (value,email,))
                    connection.commit()
                # st.write("You selected:", options)

            elif choice1=="Full Stack Development":
                options = st.multiselect(
                    "Choose the required fields",
                    ["Python", "Java", "R", "Ruby", "Node.js", "PHP", "React", "Angular", "ExpressJS"],
                    ["PHP"],
                )
                li=options
                l=[]
                for x in data:
                    # print(x)
                    for y in x:
                        converted_list = eval(y)
                        c=0
                        lowercase_list = [item.lower() for item in converted_list]
                        # print("list: ",lowercase_list)
                        for i in range(len(li)):
                            # print(li[i].lower())
                            if li[i].lower() in lowercase_list:
                                c=c+1
                        l.append(c)
                emails_list = [email[0] for email in data2]
                result = dict(zip(emails_list, l))
                for email, value in result.items():
                    # cursor.execute("UPDATE user_data11 SET Count = ? WHERE Email_ID = ?", (value, email))
                    delete_sql = f"UPDATE {DB_table_name} SET Count = %s WHERE Email_ID = %s"
                    cursor.execute(delete_sql, (value,email,))
                    connection.commit()

            elif choice1=="Android Development":
                options = st.multiselect(
                    "Choose the required fields",
                    ["Java","Kotlin","Android UI","C++","Python"],
                    ["Java"],
                )
                li=options
                l=[]
                for x in data:
                    # print(x)
                    for y in x:
                        converted_list = eval(y)
                        c=0
                        lowercase_list = [item.lower() for item in converted_list]
                        # print("list: ",lowercase_list)
                        for i in range(len(li)):
                            # print(li[i].lower())
                            if li[i].lower() in lowercase_list:
                                c=c+1
                        l.append(c)

                emails_list = [email[0] for email in data2]
                result = dict(zip(emails_list, l))
                for email, value in result.items():
                    # cursor.execute("UPDATE user_data11 SET Count = ? WHERE Email_ID = ?", (value, email))
                    delete_sql = f"UPDATE {DB_table_name} SET Count = %s WHERE Email_ID = %s"
                    cursor.execute(delete_sql, (value,email,))
                    connection.commit()

            # st.balloons()
            age = st.slider("select required experience year?", 0, 40, 5)
            st.write("Experience level set to: ", age, " years")

            if st.button("Submit", type="primary"):
                with st.spinner(':blue[Please wait for sometimes...]'):
                    time.sleep(2)
                cursor.execute(f"SELECT*FROM {DB_table_name} WHERE Experience>=%s ORDER BY Count DESC", (age,))
                data = cursor.fetchall()
                st.header("**User's Data**")
                df = pd.DataFrame(data, columns=['ID', 'Name', 'Email', 'Timestamp', 'Experience', 'Actual Skills','Count'])
                st.dataframe(df)



                st.balloons()

        else:
            st.error(":red[Wrong ID & Password Provided]")