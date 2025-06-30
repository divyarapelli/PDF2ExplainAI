# 📄 PDF2ExplainAI — PDF to AI Avatar Explainer App

PDF2ExplainAI is an AI-powered project that extracts text from any PDF, summarizes it using a large language model, generates a voice explanation, and finally produces a video of an AI avatar speaking the content.

---

## 🚀 Features

- 🧾 Extracts text from PDF using PyMuPDF
- 🧠 Summarizes and explains using Hugging Face Transformers
- 🗣️ Converts explanation to voice (TTS)
- 👩‍🏫 Generates a talking avatar video using D-ID / HeyGen
- 🎥 Final video explains the content as if it's a digital teacher!

---

## 🛠️ Technologies Used

- Python
- PyMuPDF (PDF parser)
- Hugging Face Transformers (DistilBART)
- pyttsx3 (Offline TTS)
- D-ID / HeyGen (Avatar video generation)

---

## 🧪 How to Use

1. Place your PDF as `input.pdf`
2. Run the scripts step by step:
   ```bash
   python extract_text.py
   python summarize_explain.py
   python text_to_speech.py
