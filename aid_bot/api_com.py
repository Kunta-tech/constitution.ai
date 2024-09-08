import google.generativeai as genai
import os
import markdown

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def get_api_response(query: str):
    ans = ''
    response = chat.send_message(query, stream=True)

    for part in response:
        ans += part.text
    
    return markdown.markdown(ans)