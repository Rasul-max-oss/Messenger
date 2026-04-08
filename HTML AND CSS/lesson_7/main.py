from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/second/")
def second_html():
    html = """
    <h1>Привет, меня зовут Александр!</h1>
    <p>Это мой первый HTML-фрагмент</p>
    <p>Это мой второй HTML-фрагмент</p>
    <a href="/">На главную</a>"
    """
    return html


@app.route('/second_img/')
def second_img():
    return render_template('index_2.html')

@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
