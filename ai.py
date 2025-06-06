import fitz  
import requests

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def summarize_with_gemma3(text):
    prompt = f"این یک متن علمی است. آن را به صورت ساده و خلاصه برای عموم مردم توضیح بده\n{text}"
    response = requests.post('http://localhost:11434/api/generate', 
                            json={"model": "gemma3", "prompt": prompt, "stream": False})
    return response.json()['response']




pdf_path = "text.pdf" 
full_text = extract_text_from_pdf(pdf_path)


summary = summarize_with_gemma3(full_text)
print("\n📝 خلاصه تولید شده توسط Gemma 3:")
print(summary)
