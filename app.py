import os
from flask import Flask, render_template

# نحدد للسيرفر أن المجلد الحالي هو مكان العمل
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
        return str(e) # هذا سيظهر لنا الخطأ بالتفصيل على الشاشة إذا فشل مرة أخرى

if __name__ == '__main__':
    app.run()
