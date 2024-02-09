import streamlit as st 
import cv2 
import numpy as np 
import plotly.express as px 

st.set_page_config(page_title='Image')
st.title("RGB Calculator")

image_option = st.selectbox(
    'Select a option to upload the image',
    ['Take a snap','Upload an existing image'],
    index=None,
    placeholder="Select a way...."
    )

if image_option == "Take a snap":
    ins_im = st.camera_input('Take a image to proceed...')
    if ins_im:
        bytes_data = ins_im.getvalue()
        image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        fig = px.imshow(image)
        st.plotly_chart(fig)
elif  image_option == "Upload an existing image":
    upl_image = st.file_uploader("Upload a image in png, jpg, jpeg format ", type=['png', 'jpg', 'jpeg'],accept_multiple_files=False)
    if upl_image:
        image = cv2.imdecode(np.fromstring(upl_image.read(), np.uint8), cv2.IMREAD_COLOR)
        fig = px.imshow(image)
        st.plotly_chart(fig)



# st.write(uploaded_files)