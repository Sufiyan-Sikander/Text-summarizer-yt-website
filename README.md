AI Content Summarizer

An AI-powered web application that summarizes content from YouTube videos and websites using LangChain, Groq LLMs, and Flask.

The application extracts content from a YouTube URL or webpage URL, processes the text using LangChain's Map-Reduce summarization chain, and generates:

Detailed English Summary
Key Points
Urdu Translation
Timestamps (for YouTube videos when available)
Features
Website Summarization

Extracts and summarizes content from blogs, articles, documentation pages, and websites.

YouTube Video Summarization

Fetches transcripts from YouTube videos and generates concise summaries.

AI-Powered Summaries

Uses Groq-hosted LLMs through LangChain for fast and accurate summarization.

Multilingual Output

Provides:

English Summary
Key Takeaways
Urdu Summary
Modern User Interface
Responsive Design
Glassmorphism UI
Loading Indicators
Markdown Rendering
Tech Stack
Backend
Flask
LangChain
Groq API
YouTube Transcript API
Unstructured Loader
Frontend
HTML5
CSS3
JavaScript
Marked.js
AI Model
Llama 3.1 8B Instant
Project Structure
project/
│
├── app.py
├── requirements.txt
├── .env
│
├── templates/
│   └── index.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   │
│   └── js/
│       └── script.js
│
└── README.md
Installation
Clone Repository
git clone https://github.com/yourusername/ai-content-summarizer.git

cd ai-content-summarizer
Create Virtual Environment

Windows

python -m venv venv

venv\Scripts\activate

Linux / macOS

python3 -m venv venv

source venv/bin/activate
Install Dependencies
pip install -r requirements.txt
Environment Variables

Create a .env file in the root directory.

GROQ_API_KEY=your_groq_api_key

You can obtain a free API key from Groq.

Running the Application

Start the Flask server:

python app.py

Application will be available at:

http://127.0.0.1:5000
Usage
Step 1

Open the application in your browser.

Step 2

Enter your Groq API Key.

Step 3

Paste either:

YouTube Video URL
Website URL
Step 4

Click:

Generate Summary
Step 5

View:

Detailed English Summary
Key Points
Urdu Translation
Video Timestamps (if available)
