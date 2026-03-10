import cv2
import numpy as np
import streamlit as st
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    preprocess_input,
    decode_predictions
)
from PIL import Image

def load_model():
    model = MobileNetV2(weights='imagenet')
    return model

def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (224,224)) #ove spec prihvata mobilenet
    img = preprocess_input(img)
    img = np.expand_dims(img, axis=0)

    return img

def classify_image(model, image):
    try:
        processed_image = preprocess_image(image)
        predictions = model.predict(processed_image)
        decoded_predictions = decode_predictions(predictions, top=3)[0]

        return decoded_predictions
    
    except Exception as e:
        st.error(f'error: {str(e)}')
        return None

def main():
    st.set_page_config(page_title='image classifier', layout = 'centered')
    st.title('ai image classifier')
    st.write('upload an image and let python tell u wats in it')

    @st.cache_resource #da se ne bi program pozivao iz pocetka svaki put kad pozivamo load_model

    def load_cached_model():
        return load_model()
    
    model = load_cached_model()
    uploaded_file = st.file_uploader('choose an image...', type=['jpg', 'png'])

    if uploaded_file:
        image = st.image(
            uploaded_file, caption='ur image', use_container_width=True
        )
        btn = st.button('classify image')
        if btn:
            with st.spinner('analyzing...'):
                image = Image.open(uploaded_file)
                predictions = classify_image(model, image)

                if predictions:
                    st.subheader('predictions')
                    for _,label,score in predictions:   
                        st.write(f'**{label}**: {score:.2%}')

if __name__ == '__main__':
    main()
