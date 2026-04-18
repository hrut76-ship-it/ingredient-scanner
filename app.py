import streamlit as st
from PIL import Image
import pytesseract

# THE MASTER LIST
rules = {
    "RED": ["oat", "potato", "wheat", "cashew", "almond", "yuca", "spelt", "plum", "kidney bean", "white haricot"],
    "ORANGE": ["parsley", "liquorice", "peach", "cow's milk", "spinach", "tomato", "mussel", "octopus", "pistachio"],
    "YELLOW": ["banana", "avocado", "curry", "sage", "tarragon", "honey", "raspberry", "date", "tangerine"]
}

st.title("🛒 Margaret's Scanner")
pic = st.camera_input("Scan Ingredients")

if pic:
    txt = pytesseract.image_to_string(Image.open(pic)).lower()
    res = next((c for c, ingredients in rules.items() if any(i in txt for i in ingredients)), "GREEN")
    
    colors = {"RED": "#FF4B4B", "ORANGE": "#FFA500", "YELLOW": "#FFFF00", "GREEN": "#28A745"}
    msg = {"RED": "🔴 STOP", "ORANGE": "🟠 CAUTION", "YELLOW": "🟡 WARNING", "GREEN": "🟢 SAFE"}
    
    st.markdown(f'<div style="background:{colors[res]};padding:50px;border-radius:10px;text-align:center"><h1 style="color:black;font-size:80px">{msg[res]}</h1></div>', unsafe_allow_html=True)
