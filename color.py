import streamlit as st 
import numpy as np 
import plotly.express as px 
from PIL import Image
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Function to display colored box
def display_color_box(rgb_values):
    red, green, blue = rgb_values
    color_code = f"rgb({red}, {green}, {blue})"
    st.write(f'<div style="width: 100px; height: 100px; background-color: {color_code}"></div>', unsafe_allow_html=True)


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
        # bytes_data = ins_im.getvalue()
        # image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        img = Image.open(ins_im)
        image = np.array(img)
        fig = px.imshow(image)
        st.plotly_chart(fig)
elif  image_option == "Upload an existing image":
    upl_image = st.file_uploader("Upload a image in png, jpg, jpeg format ", type=['png', 'jpg', 'jpeg'],accept_multiple_files=False)
    if upl_image:
        # image = cv2.imdecode(np.fromstring(upl_image.read(), np.uint8), cv2.IMREAD_COLOR)
        img = Image.open(upl_image)
        image = np.array(img)
        fig = px.imshow(image)
        st.plotly_chart(fig)

    
data = pd.read_csv('colors.csv')

x = data[['R','G','B']]
y = data[['color_name','hex']]

knn_model = KNeighborsClassifier(n_neighbors = 3)
knn_model.fit(x,y)

r = st.number_input('Enter the Red value',max_value = 255)
g = st.number_input('Enter the Green value',max_value = 255)
b = st.number_input('Enter the Blue value',max_value = 255)

pred = knn_model.predict([[r,g,b]])
st.write(pred)
display_color_box([r,g,b])


# st.write(uploaded_files)
