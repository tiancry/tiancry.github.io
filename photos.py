from flask import Flask, render_template

app = Flask(__name__)

# 定义照片信息列表
photos = [
    {'filename': '20240213145110.jpg', 'title': '20240213145110', 'description': '给小狗洗澡'},
    {'filename': '20240214145205.jpg', 'title': '20240214145205', 'description': '放烟花'},
    {'filename': '20240309144914.jpg', 'title': '20240309144914', 'description': '周末的晚餐'}
]

@app.route('/life')
def life():
    return render_template('life.html', photos=photos)

if __name__ == '__main__':
    app.run(debug=True)