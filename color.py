import streamlit as st 
import numpy as np 
import plotly.express as px 
from PIL import Image

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
        img = Image.open(ins_im)
        image = np.array(img)
        fig = px.imshow(image)
        st.plotly_chart(fig)
elif  image_option == "Upload an existing image":
    upl_image = st.file_uploader("Upload a image in png, jpg, jpeg format ", type=['png', 'jpg', 'jpeg'],accept_multiple_files=False)
    if upl_image:
        img = Image.open(upl_image)
        image = np.array(img)
        fig = px.imshow(image)
        st.plotly_chart(fig)



# st.write(uploaded_files)
