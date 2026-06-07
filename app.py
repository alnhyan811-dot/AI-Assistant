import os
from flask import Flask, render_template

# نحدد للسيرفر أن مجلد القوالب هو templates
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
