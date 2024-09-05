import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="port")

def insertform(html_file):
    with open(html_file) as f:
        return f.read()
    

st.title("contactme")

contact_form = insertform('g.htm')
components.html(contact_form,height=700)