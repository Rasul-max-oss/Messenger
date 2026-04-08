from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return  render_template("Home.html")

@app.route('/history')
def history():
    return render_template("history.html")

@app.route('/call')
def call():
    return render_template("call.html")

@app.route('/prices')
def prices():
    return render_template("prices.html")

@app.route('/people')
def people():
    return render_template("people.html")







if __name__ == '__main__':
    app.run(debug=True)