
import streamlit as st
from PIL import Image
import pytesseract
from data import rules # This pulls in the big list automatically

st.title("🛒 Margaret's Scanner")
pic = st.camera_input("Scan / Escanear")

if pic:
    txt pytesseract.image_to_string(Image.open(pic), lang='spa+eng').lower()
    
    for level in ["RED", "ORANGE", "YELLOW"]:
        hits = [i for i in rules[level] if i in txt]
        if hits:
            res, found = level, hits
            break

    colors = {"RED": "#FF4B4B", "ORANGE": "#FFA500", "YELLOW": "#FFFF00", "GREEN": "#28A745"}
    msg = {"RED": "🔴 STOP", "ORANGE": "🟠 CAUTION", "YELLOW": "🟡 WARNING", "GREEN": "🟢 SAFE"}
    
    st.markdown(f'<div style="background:{colors[res]};padding:40px;border-radius:15px;text-align:center;border:5px solid black;"><h1 style="color:black;font-size:50px">{msg[res]}</h1><p style="color:black;font-weight:bold;">{", ".join(found).upper()}</p></div>', unsafe_allow_html=True)
