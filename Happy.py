import streamlit as st
import streamlit.components.v1 as components
from streamlit_lottie import st_lottie
import requests
#from streamlit.hashing import _CodeHasher
st.balloons()

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


links={
  "bot":"https://assets7.lottiefiles.com/packages/lf20_zh0yCH.json",
  "face" : "https://assets3.lottiefiles.com/packages/lf20_fnjH1K.json",
  "process" : "https://assets3.lottiefiles.com/packages/lf20_LmfDtl.json",
  "DS" : "https://assets7.lottiefiles.com/private_files/lf30_8z6ubjgk.json",
  "net":"https://assets5.lottiefiles.com/private_files/lf30_smtnx4ug.json",
  "bot-DS":"https://assets10.lottiefiles.com/packages/lf20_6aYlBl.json",
  "dash":"https://assets2.lottiefiles.com/packages/lf20_d6YcaL.json",
  "chem":"https://assets3.lottiefiles.com/temp/lf20_IAVB8U.json"

}


c1,c2,c3,c4 = st.columns(4)

with c1:
  st.header("Happy")
  st_lottie(load_lottieurl(links["bot"]),key="1")
  st_lottie(load_lottieurl(links["process"]),key="2")

with c2:
  st.header("Birthday")
  st_lottie(load_lottieurl(links["face"]),key="3")
  st_lottie(load_lottieurl(links["bot-DS"]),key="4")

with c3:
  st.header("Charly")
  st_lottie(load_lottieurl(links["DS"]),key="5")
  st_lottie(load_lottieurl(links["dash"]),key="6")

with c4:
  st.header("@DataChaz")
  st.button('@DataChaz')
  st_lottie(load_lottieurl(links["net"]),key="7")
  st_lottie(load_lottieurl(links["chem"]),key="8")
