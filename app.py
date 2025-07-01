import streamlit as st
import fitz  # PyMuPDF
from transformers import pipeline
import os
os.environ["TRANSFORMERS_CACHE"] = "/mount/cache"

# Load summarization model
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6", device=-1)


def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

def summarize_text(text):
    text = text[:1000]  # keep it short for demo
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    return summary

def generate_explanation(summary):
    return f"""📘 **Explanation**:\n
This summary captures the core ideas of the original document.

🔹 **Main Points**:  
{summary}

✅ Helps you understand the key content quickly.
"""

# Streamlit UI
st.title("📄 PDF to AI Explanation")
st.markdown("Upload a PDF and get a smart explanation with AI.")

pdf_file = st.file_uploader("Upload a PDF", type=["pdf"])

if pdf_file:
    with st.spinner("🔍 Extracting and summarizing..."):
        raw_text = extract_text_from_pdf(pdf_file)
        summary = summarize_text(raw_text)
        explanation = generate_explanation(summary)

    st.subheader("📌 Summary")
    st.write(summary)

    st.subheader("💡 Explanation")
    st.write(explanation)

    st.markdown("---")
    st.markdown("🎥 Paste the above explanation into [D-ID](https://studio.d-id.com/) or [HeyGen](https://www.heygen.com/) to generate an avatar video.")
