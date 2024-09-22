import streamlit as st
from PyPDF2 import PdfReader 
import requests
import tempfile
import os

# Get the server host from environment variables or default to 'http://server:8000'
API_URL = os.getenv("SERVER_HOST", "http://server:8000")  

st.title('RAG with Cohere - Client Interface')

uploaded_file = st.file_uploader("Upload a PDF file (Optional)", type=['pdf'])
text = ""

if uploaded_file is not None:
    try:
        # Save the uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.write(uploaded_file.read()) 
            temp_file_path = temp_file.name

        # Read PDF content
        with open(temp_file_path, 'rb') as f:
            pdf = PdfReader(f)
            text = ''.join([page.extract_text() for page in pdf.pages if page.extract_text() is not None])

        if not text.strip():
            st.error("Failed to extract text from the PDF file.")
        else:
            # Send the extracted text to the FastAPI server
            response = requests.post(f"{API_URL}/uploadfile", json={"text": text})

            if response.status_code == 200:
                result = response.json()
                if "message" in result:
                    st.success(result["message"])
                elif "error" in result:
                    st.error(result["error"])
                else:
                    st.write(result)
            else:
                st.error(f"Text upload failed with status code {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Query input and sending query to the FastAPI server
query = st.text_input("Enter your question or start chatting:")

if query:
    try:
        # Send the query to the FastAPI server
        response = requests.post(f"{API_URL}/query", json={"query": query})

        if response.status_code == 200:
            result = response.json()
            if "result" in result:
                st.write(f"Segments: {result['segments']}")
                st.write(f"Generated Answer: {result['result']}")
            else:
                st.error(result)
        else:
            st.error(f"Query failed with status code {response.status_code}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
