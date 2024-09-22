# FastAPI RAG (Retrieval-Augmented Generation) Project

## Overview

This project is a **FastAPI-based Retrieval-Augmented Generation (RAG) system** where users can upload documents, ask queries, and receive answers generated based on the document's contents. It demonstrates how advanced **NLP techniques** can be used to create interactive, document-driven question-answering systems. 

This project is perfect for use cases such as:
- **Customer support**, where agents can retrieve answers from internal documents.
- **Legal, healthcare, or academic research**, where documents are rich in domain-specific information and need fast, precise answers.

## Features

- **Document Upload**: Allows users to upload text-based documents (e.g., PDF, DOCX).
- **Question Answering**: Queries are answered based on the content of the uploaded document.
- **FastAPI Backend**: A high-performance API framework that ensures quick responses and efficient handling of requests.
- **Interactive API Documentation**: Automatically generated, user-friendly API documentation available via `/docs`.
- **Dockerized**: Easy to set up and run using Docker Compose for containerized environments.

## Setup and Deployment
- clone the git repository ``` git clone https://github.com/Rag-using-Pinecone-and-Cohere.git ```  and navigate to the project path
- Build and Run with Docker Compose: Ensure Docker and Docker Compose are installed on your machine. Then, run the following command: ```docker-compose up --build```

## How It Works

1. **Upload Documents:**
   - Allows users to upload documents. The backend processes these documents, extracting text and storing them for future queries.
2. **Ask a Question:**
   - Once a document is uploaded, users can ask questions, and the system will return answers based on the document's content.

## Future Enhancements

- **User Authentication:** Add authentication for different users uploading and querying their documents.
- **Multi-format Support:** Expand support for non-text formats, such as images using OCR for text extraction.
- **Cloud Deployment:** Extend scalability by deploying the system on platforms like AWS, GCP, or Azure.

