import streamlit as st
from PIL import Image
import pytesseract
from data import rules

st.set_page_config(page_title="Margaret Food Guard", layout="centered")

st.title("🛒 Margaret's Scanner")
st.write("English & Español")

pic = st.camera_input("Scan / Escanear")

if pic:
    img = Image.open(pic)
    # Using 'spa+eng' helps the app read Spanish accents correctly
    txt = pytesseract.image_to_string(img, lang='spa+eng').lower()
    
    res = "GREEN"
    found = []
    
    # This checks Red first, then Orange, then Yellow
    for level in ["RED", "ORANGE", "YELLOW"]:
        hits = [i for i in rules[level] if i in txt]
        if hits:
            res, found = level, hits
            break

    colors = {"RED": "#FF4B4B", "ORANGE": "#FFA500", "YELLOW": "#FFFF00", "GREEN": "#28A745"}
    msg = {
        "RED": "🔴 ALTO / STOP", 
        "ORANGE": "🟠 PRECAUCIÓN", 
        "YELLOW": "🟡 AVISO / WARNING", 
        "GREEN": "🟢 SEGURO / SAFE"
    }
    
    st.markdown(f'''
        <div style="background-color:{colors[res]}; padding:40px; border-radius:15px; text-align:center; border: 5px solid black;">
            <h1 style="color:black; font-size:50px; margin:0;">{msg[res]}</h1>
            <p style="color:black; font-size:20px; font-weight:bold;">{", ".join(found).upper()}</p>
        </div>
    ''', unsafe_allow_html=True)
