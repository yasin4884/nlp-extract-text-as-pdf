import requests

def get_gemma_response(question):
    try:
        response = requests.post('http://localhost:11434/api/chat',
                                json={'model': 'gemma3', 'prompt': question,'system':'اسم تو paul هستش و یک چت بات هستی که به فارسی صحبت میکنی', 'stream': False},
                                timeout=10)
        response.raise_for_status()
        return response.json().get('response', 'جوابی دریافت نشد!')
    except requests.ConnectionError:
        return "خطا: سرور Ollama اجرا نیست! دستور 'ollama serve' رو بزنید."
    except requests.Timeout:
        return "خطا: درخواست Timeout شد. سرور Ollama رو چک کنید."
    except requests.RequestException as e:
        return f"خطا: {e}"

while True:
    try:
        user_input = input("سوالت چیه؟ (برای خروج بنویس exit): ")
        if user_input.lower() == 'exit':
            break
        if not user_input.strip():
            print("لطفاً یه سوال بنویس!")
            continue
        answer = get_gemma_response(user_input)
        print("چت‌بات:", answer)
    except KeyboardInterrupt:
        print("\nخروج...")
        break
    except Exception as e:
        print(f"خطا: {e}")