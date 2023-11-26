import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("Portfolio/images/luck.jpg")

with col2:
    st.title("Lucky Uyi")
    content = """ 
    A highly skilled Network IT professional with 3 years of professional 
experience, and proficiencies in Microsoft Azure, Cisco Networking devices 
and a Certified Microsoft IT Professional. I have a strong background in 
designing, implementing and managing complex network infrastructures. 
Adept at troubleshooting and resolving network issues to ensure optimal 
performance and security. Seeking a challenging role to contribute my 
technical expertise in network architecture, administration, and security
    """
    st.info(content)


content1 = """
    Below you can find some of the apps I have built in Python. Feel free to contact me!
    """
st.write(content1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pd.read_csv('Portfolio/data.csv', sep=';')


with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('Portfolio/images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')




with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image('Portfolio/images/' + row['image'])
        st.write(f'[Source Code]({row["url"]})')


