# Invoice Extraction Bot

This project features an Invoice Extraction Bot that leverages Gemini, a large language model developed by Google, to extract information from multiple images of invoices. The bot is implemented in Python and integrates with Streamlit for the frontend interface.

## Features

- **Invoice Information Extraction**: The bot utilizes Gemini to analyze and extract relevant information from images of invoices.

- **Multiple Image Support**: Users can upload multiple images of invoices, and the bot processes each image to extract necessary details.

- **Question-Answering System**: The bot provides answers to questions related to the invoices, such as total amount, due date, vendor details, etc.

- **Streamlit Frontend**: The frontend interface is built using Streamlit, offering a user-friendly experience for uploading images and viewing extracted information.

## Installation

To run the Invoice Extraction Bot locally, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/ShivankK26/Invoice-Extraction-Bot.git
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Streamlit server by running the following command:

   ```bash
   streamlit run app.py
   ```

2. Open your web browser and navigate to the provided URL to access the Streamlit interface.

3. Upload one or multiple images of invoices using the provided interface.

4. Once the images are uploaded, the bot will process them using Gemini and display the extracted information.

5. Users can ask questions related to the invoices in the provided text box, and the bot will provide answers based on the extracted data.
