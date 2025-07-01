import fitz  # PyMuPDF

def extract_text_from_pdf():
    pdf_name = input("Enter the PDF file name (with .pdf): ")
    doc = fitz.open(pdf_name)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()

    with open("explanation.txt", "w", encoding="utf-8") as file:
        file.write(text)

    print("✅ Text extracted to explanation.txt")

if __name__ == "__main__":
    extract_text_from_pdf()
