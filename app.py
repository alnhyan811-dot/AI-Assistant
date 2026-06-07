import os
import openai
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# نضع المفتاح في إعدادات Render (Environment Variables) وليس داخل الكود
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_question = request.json.get("question")
    # إرسال السؤال للذكاء الاصطناعي
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_question}]
    )
    answer = response.choices[0].message.content
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run()
