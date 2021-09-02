import streamlit as st
from streamlit_player import st_player
import streamlit.components.v1 as components
from streamlit_tags import st_tags, st_tags_sidebar
st.set_page_config(layout="wide")
st.title('Update from github.dev')
list1=[]
list2=[]
maxtags =6 
keywords = st_tags_sidebar(
    label='# Enter URLs to work:',
    text='Press enter to add more',
    maxtags=maxtags,
    key="aljnf")


col1, col2, col3 = st.beta_columns([6,1,2])
with col1:
  sel_url=st.selectbox('Select url', keywords)
  components.iframe(sel_url,height=800,scrolling=True)


with col3:
  url_youtube=st.text_input('Enter youtube URL','https://www.youtube.com/watch?v=_daTfgc4u3k')
  st_player(url_youtube)

