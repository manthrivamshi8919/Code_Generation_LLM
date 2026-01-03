import streamlit as st
from groq import Groq

st.set_page_config(
    page_title="Groq Code Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🤖 Groq Code Generator")
st.markdown("Generate code using Groq AI with a beautiful, interactive interface")

def call_groq_api(prompt, api_key, model="llama-3.3-70b-versatile"):
    """Call Groq API to generate code"""
    try:
        client = Groq(api_key=api_key)
        
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful code generation assistant. Generate clean, well-commented, and functional code based on the user's requirements. Always provide the complete code solution."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            max_tokens=4000,
            temperature=0.7
        )
        
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling Groq API: {str(e)}"

def main():
    # Sidebar for API configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        api_key = st.text_input(
            "Groq API Key",
            type="password",
            help="Enter your Groq API key from groq.com",
            value=st.session_state.get("api_key", "")
        )
        
        # Store API key in session state
        if api_key:
            st.session_state.api_key = api_key
        
        st.markdown("---")
        st.markdown("### 📝 How to use:")
        st.markdown("1. Enter your Groq API key")
        st.markdown("2. Describe the code you want to generate")
        st.markdown("3. Select programming language")
        st.markdown("4. Click 'Generate Code'")
        
        st.markdown("---")
        st.markdown("### 🔑 Get API Key:")
        st.markdown("Visit [groq.com](https://groq.com) to get your API key")
    
    # Main content area
    st.header("📝 Input")
    
    # Language selection
    language = st.selectbox(
        "Programming Language",
        ["Python", "JavaScript", "Java", "C++", "C#", "Go", "Rust", "TypeScript", "HTML", "CSS", "SQL", "Other"],
        index=0,
        help="Select the programming language for code generation"
    )
    
    # Code description
    prompt = st.text_area(
        "Describe the code you want to generate:",
        placeholder="Example: Create a function that sorts a list of numbers using bubble sort and returns the sorted list...",
        height=200,
        help="Be specific about what you want the code to do"
    )
    
    # Generate button
    generate_button = st.button(
        "🚀 Generate Code",
        type="primary",
        use_container_width=True,
        disabled=not st.session_state.get("api_key") or not prompt.strip()
    )
    
    # Output section
    st.header("📄 Output")
    
    if generate_button:
        api_key = st.session_state.get("api_key")
        if not api_key:
            st.error("Please enter your Groq API key in the sidebar")
        elif not prompt.strip():
            st.error("Please describe the code you want to generate")
        else:
            # Construct enhanced prompt
            enhanced_prompt = f"Generate {language} code for the following requirement:\n\n{prompt}\n\nProvide only the complete code solution without explanations."
            
            with st.spinner("🤖 Groq is generating your code..."):
                generated_code = call_groq_api(enhanced_prompt, api_key)
            
            if generated_code.startswith("Error"):
                st.error(generated_code)
            else:
                st.success("✅ Code generated successfully!")
                st.code(generated_code, language=language.lower())
                st.download_button(
                    label="📥 Download Code",
                    data=generated_code,
                    file_name=f"generated_code.{get_file_extension(language)}",
                    mime="text/plain"
                )
    else:
        st.info("👈 Enter your requirements and click 'Generate Code' to see the output here")

def get_file_extension(language):
    """Get file extension for programming language"""
    extensions = {
        "Python": "py",
        "JavaScript": "js",
        "Java": "java",
        "C++": "cpp",
        "C#": "cs",
        "Go": "go",
        "Rust": "rs",
        "TypeScript": "ts",
        "HTML": "html",
        "CSS": "css",
        "SQL": "sql"
    }
    return extensions.get(language, "txt")

if __name__ == "__main__":
    main()
