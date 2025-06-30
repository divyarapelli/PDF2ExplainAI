import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

if __name__ == "__main__":
    pdf_file = "input.pdf"  # Your PDF file
    extracted_text = extract_text_from_pdf(pdf_file)

    with open("output_text.txt", "w", encoding="utf-8") as f:
        f.write(extracted_text)

    print("✅ Text extracted and saved to output_text.txt")
