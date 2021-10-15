import streamlit as st
from streamlit_player import st_player
import streamlit.components.v1 as components
from streamlit_tags import st_tags, st_tags_sidebar
import urllib.request
#st.set_page_config(layout="wide")

BACKGROUND_COLOR = 'white'
COLOR = 'black'

def set_page_container_style(
        max_width: int = 2100, max_width_100_percent: bool = False,
        padding_top: int = 0, padding_right: int = 1, padding_left: int = 1, padding_bottom: int = 10,
        color: str = COLOR, background_color: str = BACKGROUND_COLOR,
    ):
        if max_width_100_percent:
            max_width_str = f'max-width: 100%;'
        else:
            max_width_str = f'max-width: {max_width}px;'
        st.markdown(
            f'''
            <style>
                .reportview-container .sidebar-content {{
                    padding-top: {padding_top}rem;
                }}
                .reportview-container .main .block-container {{
                    {max_width_str}
                    padding-top: {padding_top}rem;
                    padding-right: {padding_right}rem;
                    padding-left: {padding_left}rem;
                    padding-bottom: {padding_bottom}rem;
                }}
                .reportview-container .main {{
                    color: {color};
                    background-color: {background_color};
                }}
            </style>
            ''',
            unsafe_allow_html=True,
        )

set_page_container_style()

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

#st.title('Streamlit Parade')

list1=[]
list2=[]
maxtags =6 



url = "https://raw.githubusercontent.com/napoles-uach/MundaneApps/main/links.txt"
file = urllib.request.urlopen(url)

urls=[]
for line in file:
	decoded_line = line.decode("utf-8")
	urls.append(decoded_line)

sel_url=st.selectbox('', urls)
components.iframe(sel_url,height=800,scrolling=True)
