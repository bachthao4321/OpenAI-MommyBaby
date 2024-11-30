from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai

# Cấu hình OpenAI API
openai.api_key = "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"

SYSTEM_PROMPT = """
Bạn là một chatbot tư vấn dinh dưỡng MommyBaby dành riêng cho bà bầu và trẻ sơ sinh. 
Cung cấp thông tin đáng tin cậy dựa trên kiến thức khoa học hiện tại. 
Câu trả lời của bạn phải rõ ràng, dễ hiểu và thân thiện, tập trung vào sức khỏe của mẹ và bé. 
Nếu không chắc chắn, hãy khuyên người dùng tham khảo ý kiến chuyên gia y tế.
"""

# Khởi tạo ứng dụng FastAPI
app = FastAPI()

# Định nghĩa mô hình dữ liệu đầu vàoa
class Message(BaseModel):
    message: str

# Tạo endpoint chatbot
@app.get('/')
def hello():
    return 'hello word'
@app.post("/chat")
async def chat(message: Message):
    try:
        # Gửi yêu cầu tới OpenAI GPT API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.message}
            ]
        )
        # Trích xuất câu trả lời từ API
        reply = response['choices'][0]['message']['content']
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

