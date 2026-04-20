txt = pytesseract.image_to_string(image.open(pic), lang='spa+eng').lower()
