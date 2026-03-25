from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Віддаємо фронтенд сторінку
    return render_template('index.html')

@app.route('/api/data')
def get_data():
    # Просте API для перевірки бекенду
    return {"status": "success", "message": "Привіт від бекенду на Python!"}

if __name__ == '__main__':
    app.run(debug=True)