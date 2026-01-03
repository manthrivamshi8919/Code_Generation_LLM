# 🤖 Groq Code Generator

AI-powered code generation web application using Streamlit and Groq LLMs.

## 📋 Description

Generate production-ready code from natural language descriptions. Select your programming language, describe what you need, and get instant, downloadable, and syntax-highlighted code. This document contains everything you need to set up and run the application from scratch.

## ✨ Features

-   **Multi-language Support**: Generate code for Python, JavaScript, TypeScript, Java, C++, C#, Go, Rust, PHP, Ruby, Swift, Kotlin, HTML, CSS, SQL, Bash, and more.
-   **Secure API Key Input**: Your Groq API key is input securely in the sidebar and is not stored.
-   **Clean, Syntax-Highlighted Output**: The generated code is displayed with professional syntax highlighting for better readability.
-   **Instant Code Download**: Download your generated code as a file with a single click.
-   **Fast Generation**: Powered by the ultra-fast Groq LLMs for near-instant results.
-   **End-to-End Documentation**: This single file contains all the code and instructions you need.

## 🛠️ Technologies Used

-   **Streamlit**: For the fast and interactive web interface.
-   **Groq API**: The large language model powering the code generation.
-   **Python 3.8+**: The core backend language.
-   **Pygments**: Used by Streamlit for syntax highlighting.

---

## 🚀 Quick Start (For Experienced Users)

1.  **Clone and Navigate**
    ```bash
    git clone https://github.com/your-username/groq-code-generator.git
    cd groq-code-generator
    ```
2.  **Create and Activate Virtual Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the App**
    ```bash
    streamlit run app.py
    ```
5.  Open your browser at `http://localhost:8501` and enter your Groq API key in the sidebar.

---

## 📁 Project Files & Source Code

To build this application, create a new project folder and add the following three files by copying the code provided below.

### 1. `requirements.txt`

This file lists all the Python libraries required for the project.

**File Path:** `groq-code-generator/requirements.txt`

```txt
streamlit>=1.40.0
groq>=1.0.0
pygments==2.17.2
