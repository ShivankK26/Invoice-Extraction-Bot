import streamlit as st
from dotenv import load_dotenv


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
