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

def main():
    load_dotenv()

    st.set_page_config(page_title="Inoice Extraction Bot")
    st.subheader("I'll help you in extracting invoice data...")

    pdf = st.file_uploader(
        "Upload your invoices here, only PDF files allowed",
        type=["pdf"],
        accept_multiple_files=True,
    )

    submit = st.button("Extract Data")

    if submit:
        with st.spinner("Wait for it ..."):
            st.write("response")
        st.success("Hope you liked the response 🚀")


if __name__ == "__main__":
    main()
