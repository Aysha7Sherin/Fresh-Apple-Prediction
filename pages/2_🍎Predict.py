import pandas as pd
import streamlit as st
import os
import sys
from io import BytesIO,StringIO
from keras.models import load_model
from PIL import Image
import numpy as np
st.set_page_config(page_title='Fresh Apple',page_icon='🍎',layout='wide')
def main():
    model=load_model('FreshOrRotten.h5')
    file=st.file_uploader('Upload file',type=['png','jpg','jpeg'])
    show_file=st.empty()
    if not file:
        show_file.info('Please upload a file'.format(''.join(['png','jpg','jpeg'])))
        return
    content=file.getvalue()
    if isinstance(file,BytesIO):
        show_file.image(file)
        # Preprocess the image
        img = Image.open(file)  # Open the image using PIL
        img = img.resize((150, 150))  # Resize to (150, 150)
        img_array = np.array(img)  # Convert the image to a NumPy array

        # Ensure the image has 3 channels (RGB)
        if img_array.shape[-1] != 3:
            img_array = np.stack([img_array] * 3, axis=-1)  # Convert grayscale to RGB if needed

        # Normalize the image and reshape it to match the model input (1, 150, 150, 3)
        img_array = img_array / 255.0  # Normalize the image to [0, 1]
        img_array = img_array.reshape(1, 150, 150, 3)  # Add the batch dimension
        names=['Rotten apple', 'Fresh Apple']
        pred = st.button('Predict')
        if pred:
            y_new = model.predict(img_array)
            if y_new>0.5:
                st.write('#',names[1])
            else:
                st.write('#',names[0])

    else:
        df=pd.read_csv(file)
        st.dataframe(df.head(2))
    file.close()
main()