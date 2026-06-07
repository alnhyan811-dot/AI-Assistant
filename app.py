from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "مرحباً بكم في تطبيق المهندس أبو زايد آل نهيان - مساعدكم الذكي!"

if __name__ == '__main__':
    app.run()
