import streamlit as st
from streamlit_player import st_player
import streamlit.components.v1 as components
st.set_page_config(layout="wide")
col1, col2, col3 = st.beta_columns([6,1,2])
with col1:
  url=st.text_input('Enter working URL',"https://docs.streamlit.io/en/stable/")
  components.iframe(url,height=800,scrolling=True)


with col3:
  url_youtube=st.text_input('Enter youtube URL')
  # Embed a youtube video
  st_player(url_youtube)
