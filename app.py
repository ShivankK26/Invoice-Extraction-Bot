import os
import streamlit as st
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)


def initialize_model(model_name="gemini-pro-vision"):
    model = genai.GenerativeModel(model_name)
    return model

def get_response(model, model_behavior, image, prompt):
    response = model.generate_content([model_behavior, image[0], prompt])
    return response.text

def get_image_bytes(uploaded_image):
    if uploaded_image is not None:
        image_bytes = uploaded_image.getvalue()

        image_info = [
            {
                "mime_type": uploaded_image.type,
                "data": image_bytes
            }
        ]

        return image_info

    else:
        raise FileNotFoundError("Image not found")



def show_response():
    model = initialize_model()

    st.set_page_config(page_title="Inoice Extraction Bot")
    st.subheader("I'll help you in extracting invoice data...")

    prompt = st.text_input("Enter the prompt", key="prompt")

    uploaded_image = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Your image", use_column_width=True)

    submit = st.button("Extract Data")

    model_behaviour = """
    You are a senior Accountant who has a very deep knowledge in understanding invoices and finances related to it. You'll receive an invoice and you'll have to answer the questions based upon the information present in invoice.
    """

    if submit or prompt:
        if len(prompt) > 0:
            image_info = get_image_bytes(uploaded_image)
            response = get_response(model, model_behaviour, image_info, prompt)
            st.write(response)
        else:
            raise ValueError("Wrong Prompt!")

if __name__ == "__main__":
    show_response()
