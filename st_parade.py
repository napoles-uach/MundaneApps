import streamlit as st
from streamlit_player import st_player
import streamlit.components.v1 as components
from streamlit_tags import st_tags, st_tags_sidebar
import urllib.request
st.set_page_config(layout="wide")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title('Streamlit Parade')

list1=[]
list2=[]
maxtags =6 



url = "https://raw.githubusercontent.com/napoles-uach/MundaneApps/main/links.txt"
file = urllib.request.urlopen(url)

urls=[]
for line in file:
	decoded_line = line.decode("utf-8")
	urls.append(decoded_line)

sel_url=st.selectbox('Select url', urls)
components.iframe(sel_url,height=800,scrolling=True)
