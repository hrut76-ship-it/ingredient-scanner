
    import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import pytesseract
from data import rules

st.title("🛒 Margaret's Scanner")

# Added an option to upload so she can use her phone's better camera app
mode = st.radio("Choose source:", ["Live Camera", "Upload Photo"])

if mode == "Live Camera":
    pic = st.camera_input("Scan / Escanear")
else:
    pic = st.file_uploader("Upload label photo", type=['jpg', 'png', 'jpeg'])

if pic:
    # --- SUPER VISION ---
    img = Image.open(pic).convert('L')
    img = ImageEnhance.Contrast(img).enhance(2.5) # Made contrast even stronger
    
    txt = pytesseract.image_to_string(img, lang='spa+eng').lower()
    
    # ... (the rest of the logic remains the same)
    # 1. Turn to Black & White (makes text pop)
    img = img.convert('L') 
    
    # 2. Boost Contrast
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2.0)
    
    # 3. Make it bigger (Digital Zoom)
    width, height = img.size
    img = img.resize((width*2, height*2), resample=Image.LANCZOS)
    
    # 4. READ THE TEXT
    txt = pytesseract.image_to_string(img, lang='spa+eng').lower()
    
    # --- LOGIC ---
    res = "GREEN"
    found = []
    
    for level in ["RED", "ORANGE", "YELLOW"]:
        hits = [i for i in rules[level] if i in txt]
        if hits:
            res, found = level, hits
            break

    # --- DISPLAY ---
    colors = {"RED": "#FF4B4B", "ORANGE": "#FFA500", "YELLOW": "#FFFF00", "GREEN": "#28A745"}
    msg = {"RED": "🔴 STOP", "ORANGE": "🟠 PRECAUCIÓN", "YELLOW": "🟡 AVISO", "GREEN": "🟢 SAFE"}
    
    st.markdown(f'''
        <div style="background-color:{colors[res]}; padding:40px; border-radius:15px; text-align:center; border: 5px solid black;">
            <h1 style="color:black; font-size:50px; margin:0;">{msg[res]}</h1>
            <p style="color:black; font-size:20px; font-weight:bold;">{", ".join(found).upper()}</p>
        </div>
    ''', unsafe_allow_html=True)
    
    # This helps us see if the "Super Vision" is working!
    with st.expander("DEBUG: View Scanned Text"):
        st.text(txt)
