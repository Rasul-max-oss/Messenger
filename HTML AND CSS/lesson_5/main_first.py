from flask import Flask

app = Flask(__name__)


#@app.route('/')
#def index():
#   return"hello"

@app.route('/')

@app.route('/<name>')
def hello_user(name=None):
    if name is None:
        return "no"
    else:
        return  f"hello,{str(name).upper()}"



if __name__ == "__main__":
    app.run()