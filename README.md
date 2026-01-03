🤖 Groq Code Generator
AI-powered code generation web application using Streamlit and Groq LLMs.

📋 Description
Generate production-ready code from natural language descriptions. Select your programming language, describe what you need, and get instant, downloadable code.

✨ Features

Multi-language support (Python, JavaScript, Java, C++, Go, Rust, etc.)
Secure API key input
Clean, syntax-highlighted output
Instant code download
Fast generation with Groq LLMs


🛠️ Technologies Used

Streamlit - Web interface
Groq API - LLM for code generation
Python 3.8+ - Backend language
Pygments - Syntax highlighting


📦 Installation
1. Clone Repository
bashgit clone https://github.com/your-username/groq-code-generator.git
cd groq-code-generator
2. Create Virtual Environment
bashpython -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install Dependencies
bashpip install -r requirements.txt

🚀 How to Run
bashstreamlit run app.py
Open your browser at http://localhost:8501

📁 Project Structure
groq-code-generator/
├── app.py              # Main Streamlit application
├── groq_client.py      # Groq API wrapper
├── requirements.txt    # Dependencies
└── README.md          # Documentation

📚 Dependencies
txtstreamlit>=1.40.0
numpy>=2.0.0
groq>=1.0.0
pygments==2.17.2

🔑 Setup API Key

Visit https://groq.com
Create account and generate API key
Enter key in the application sidebar


💡 Usage Example
Input:

Language: Python
Description: "Create a function to check if a number is prime"

Output:

Complete Python function with comments
Download as .py file


🎯 Supported Languages
Python • JavaScript • TypeScript • Java • C++ • C# • Go • Rust • PHP • Ruby • Swift • Kotlin • HTML • CSS • SQL • Bash

📄 License
MIT License - Free for educational and commercial use

🤝 Contributing
Pull requests welcome! For major changes, please open an issue first.

📧 Contact
For questions or suggestions, open an issue on GitHub.

Built with ❤️ using Streamlit and Groq
