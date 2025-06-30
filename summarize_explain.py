from transformers import pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def summarize_text(text):
    text = text[:1000]  # Use only first 1000 chars for speed
    summary = summarizer(text, max_length=150, min_length=50, do_sample=False)[0]['summary_text']
    return summary

def generate_explanation(summary):
    explanation = (
        "📘 Explanation:\n"
        "This summary captures the core ideas of the original document.\n"
        "The document discusses the following key points:\n"
        f"{summary}\n\n"
        "This helps in understanding the main ideas quickly without reading the full document."
    )
    return explanation

if __name__ == "__main__":
    raw_text = read_text_file("output_text.txt")
    summary = summarize_text(raw_text)
    explanation = generate_explanation(summary)

    with open("explanation.txt", "w", encoding="utf-8") as f:
        f.write("🔹 Summary:\n" + summary + "\n\n" + explanation)

    print("✅ Summary and explanation saved to explanation.txt")