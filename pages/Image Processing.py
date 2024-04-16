import streamlit as st
import numpy as np
import cv2

st.title("Image Processing App")
st.write("Please select an image file from your local files:")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:  
    st.header("Image Uploaded")
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    

    st.image(image, caption="Uploaded Image", channels="BGR", use_column_width=True)

    st.header('Resizing Image')
    resized_image = cv2.resize(image, (300, 300))
    st.image(resized_image, caption='Resized Image', channels="BGR", use_column_width=True)

    st.header('Grayscale image')
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    st.image(grayscale_image, caption='Grayscale Image', use_column_width=True)

    st.header('Cropped image')
    cropped_image = image[50:300, 50:300]
    st.image(cropped_image, caption='Cropped Image', channels="BGR", use_column_width=True)

    st.header('Rotated image')
    rotation_angle = 45
    rows, cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols / 2, rows / 2), rotation_angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (cols, rows))
    st.image(rotated_image, caption='Rotated Image', channels="BGR", use_column_width=True)
