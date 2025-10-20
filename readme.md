# 💬 Gemini Chat Assistant

A lightweight conversational AI app built using **LangChain** and **Streamlit**, powered by **Google's Gemini 2.5 Flash** model.  
This project turns your terminal-based conversation into a sleek, memory-enabled **ChatGPT-style web interface**.

---

## 🚀 Features

✅ Real-time AI chat using Gemini 2.5 Flash  
✅ Conversational memory (multi-turn context)  
✅ Modern Streamlit UI with chat bubbles  
✅ Minimal setup — just plug in your API key and run  
✅ Extensible design for custom system roles, themes, or data sources

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Streamlit** – UI layer  
- **LangChain** – model orchestration  
- **Google Generative AI (Gemini)** – large language model  
- **dotenv** – for environment variable management

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/gemini-chat-assistant.git
cd gemini-chat-assistant
```
### 2️⃣ Create a virtual environment (recommended)

```python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install dependencies

```bash 
pip install -r requirements.txt
```

If you don’t have a requirements.txt yet, here’s what it should contain:

streamlit
python-dotenv
langchain-google-genai
langchain-core

### 🔑 API Key Setup

Go to your Google AI Studio
Generate a Gemini API key
Create a .env file in your project root and add:

```bash
GEMINI_API_KEY=your_actual_api_key_here
```
🧠 How to Run
```bash
streamlit run app.py
```

Then open the URL shown in your terminal - usually:
```bash
http://localhost:8501
```

💬 Usage

Type your message in the input box
The assistant replies instantly
It remembers previous messages within the session