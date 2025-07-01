from transformers import pipeline
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


def read_text_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def summarize_text(text):
    max_chunk_size = 800
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]
    
    summaries = []
    for chunk in chunks:
        summary = summarizer(chunk, max_length=150, min_length=40, do_sample=False)[0]['summary_text']
        summaries.append(summary)
    
    return " ".join(summaries)

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