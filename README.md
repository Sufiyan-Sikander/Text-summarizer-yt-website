# 🦜 Text Summarizer – YouTube & Website

A Streamlit web app that summarizes content from YouTube videos and websites using LangChain and Groq's LLaMA 3.1 model. It provides an English summary, key points, an Urdu translation, and timestamps (for YouTube videos).

## Features

- Summarize any YouTube video or website URL
- Detailed ~500 word English summary
- Bullet-point key highlights
- Urdu translated summary (اردو خلاصہ)
- Approximate timestamps for YouTube videos
- Powered by Groq LLaMA 3.1 8B Instant

## Tech Stack

- **Frontend:** Streamlit
- **LLM:** Groq (LLaMA 3.1 8B Instant)
- **Framework:** LangChain (map-reduce summarization chain)
- **Loaders:** YouTube Transcript API, Unstructured URL Loader

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/text-summarizer-yt-website.git
   cd text-summarizer-yt-website
   ```

2. **Create a virtual environment and activate it**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**
   ```bash
   streamlit run app.py
   ```

5. **Enter your Groq API key** in the sidebar and paste a YouTube or website URL to get a summary.

## Getting a Groq API Key

Sign up at [console.groq.com](https://console.groq.com) and generate a free API key.

## Screenshot

<!-- Add a screenshot of the app here -->

## License

This project is open source and available under the [MIT License](LICENSE).
