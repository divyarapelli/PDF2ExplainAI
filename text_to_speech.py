import pyttsx3

def read_explanation(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  # Speech rate
    engine.setProperty('volume', 1)  # Volume: 0.0 to 1.0
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    explanation = read_explanation("explanation.txt")
    speak_text(explanation)
