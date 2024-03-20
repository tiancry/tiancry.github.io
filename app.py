from flask import Flask, render_template
from photos import photos   # 导入photos.py中的数据

app = Flask(__name__, static_folder='static')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/life')
def life():
    return render_template('life.html', photos=photos)  # 将photos列表传递给life.html模板

if __name__ == "__main__":
    app.run(debug=True)