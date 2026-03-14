# 🎬 Script Analyzer

A professional AI-driven application designed to analyze movie scripts, detect emotional sentiment, and generate automated reviews. This project showcases multi-agent orchestration using **LangGraph** for logic routing and **Streamlit** for the user interface.

## ✨ Features
- **Sentiment Detection**: Uses LLMs to classify scripts into 'Positive' or 'Negative' categories.
- **Automated Routing**: Implements conditional edges to send scripts to specialized review nodes.
- **Instant Feedback**: Provides a clean and interactive dashboard for real-time script analysis.

## 🛠️ Tech Stack
- **Orchestration**: LangGraph & LangChain
- **Model**: Llama-3.3-70B (via Groq Cloud)
- **Frontend**: Streamlit
- **Environment**: Python 3.10+

## 🚀 Installation & Setup
1. Clone the repository:
   ```bash
   git clone [https://github.com/PrinceNaroliya/script_analyzer.git](https://github.com/PrinceNaroliya/script_analyzer.git)
2. Create a .env file and add your Groq API Key:
   ```bash
   GROQ_API_KEY=your_api_key_here
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
4. Launch the application:
   ```bash
   streamlit run script.py
