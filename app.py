import validators
import streamlit as st
from langchain_classic.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_classic.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Streamlit config
st.set_page_config(
    page_title="LangChain: Summarize Text From YT or Website",
    page_icon="🦜"
)
st.title("🦜 LangChain: Summarize Text From YT or Website")
st.subheader("Summarize URL")

# Sidebar
with st.sidebar:
    groq_api_key = st.text_input("Groq API Key", type="password")

generic_url = st.text_input("URL", label_visibility="collapsed")

# LLM
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    groq_api_key=groq_api_key
)

# MAP prompt
map_prompt = PromptTemplate(
    template="""
Summarize the following content clearly and concisely:

{text}
""",
    input_variables=["text"]
)

# COMBINE prompt
combine_prompt = PromptTemplate(
    template="""
Using the summaries below, generate the following:

1. A detailed English summary of approximately 500 words.
2. A bullet-point list of key points (in English).
3. An Urdu translated summary written in simple, easy language.
4. If the content is from a YouTube video, include approximate timestamps in English only.

Format EXACTLY like this:

### English Summary
<English paragraph summary>

### Key Points
- Point 1
- Point 2
- Point 3

### اردو خلاصہ
<Urdu translated summary>

### Timestamps (if applicable)
- 00:00 – Introduction
- 02:15 – Main topic explained
- 05:40 – Conclusion

{text}
""",
    input_variables=["text"]
)


if st.button("Summarize the Content from YT or Website"):

    if not groq_api_key.strip() or not generic_url.strip():
        st.error("Please provide the information to get started")

    elif not validators.url(generic_url):
        st.error("Please enter a valid URL")

    else:
        try:
            with st.spinner("Fetching & summarizing content..."):

                # Loader selection
                if "youtube.com" in generic_url or "youtu.be" in generic_url:
                    loader = YoutubeLoader.from_youtube_url(
                    generic_url,
                    add_video_info=False,
                    language=["en", "hi"]
                    )
                else:
                    loader = UnstructuredURLLoader(
                        urls=[generic_url],
                        ssl_verify=False,
                        headers={"User-Agent": "Mozilla/5.0"}
                    )

                # Load docs
                docs = loader.load()

                # Split docs
                text_splitter = RecursiveCharacterTextSplitter(
                    chunk_size=1200,
                    chunk_overlap=200
                )
                docs = text_splitter.split_documents(docs)

                # Summarization chain
                chain = load_summarize_chain(
                    llm,
                    chain_type="map_reduce",
                    map_prompt=map_prompt,
                    combine_prompt=combine_prompt
                )

                summary = chain.run(docs)
                st.markdown("## 📝 Summary")
                st.markdown(summary)


        except Exception as e:
            st.exception(e)
