import os
import validators
from dotenv import load_dotenv

from flask import Flask, render_template, request, jsonify

from langchain_groq import ChatGroq
from langchain_classic.prompts import PromptTemplate
from langchain_classic.chains.summarize import load_summarize_chain

from langchain_community.document_loaders import (
    YoutubeLoader,
    UnstructuredURLLoader
)

from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

app = Flask(__name__)

# -------------------------
# Prompt Templates
# -------------------------

map_prompt = PromptTemplate(
    template="""
Summarize the following content clearly and concisely:

{text}
""",
    input_variables=["text"]
)

combine_prompt = PromptTemplate(
    template="""
Using the summaries below, generate the following:

1. A detailed English summary of approximately 500 words.
2. A bullet-point list of key points.
3. A simple Urdu translated summary.
4. If the content is from YouTube, include timestamps.

Format EXACTLY like this:

### English Summary
<summary>

### Key Points
- point

### اردو خلاصہ
<urdu summary>

### Timestamps (if applicable)
- 00:00 Topic

{text}
""",
    input_variables=["text"]
)

# -------------------------
# Routes
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/summarize", methods=["POST"])
def summarize():

    try:
        data = request.get_json()

        url = data.get("url")
        api_key = data.get("groq_api_key")

        if not url:
            return jsonify({"error": "URL is required"}), 400

        if not api_key:
            return jsonify({"error": "Groq API Key is required"}), 400

        if not validators.url(url):
            return jsonify({"error": "Invalid URL"}), 400

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            groq_api_key=api_key
        )

        # -------------------------
        # Select Loader
        # -------------------------

        if "youtube.com" in url or "youtu.be" in url:
            loader = YoutubeLoader.from_youtube_url(
                url,
                add_video_info=False,
                language=["en", "hi"]
            )
        else:
            loader = UnstructuredURLLoader(
                urls=[url],
                ssl_verify=False,
                headers={
                    "User-Agent": "Mozilla/5.0"
                }
            )

        docs = loader.load()

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1200,
            chunk_overlap=200
        )

        docs = splitter.split_documents(docs)

        chain = load_summarize_chain(
            llm,
            chain_type="map_reduce",
            map_prompt=map_prompt,
            combine_prompt=combine_prompt
        )

        summary = chain.run(docs)

        return jsonify({
            "success": True,
            "summary": summary
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)
