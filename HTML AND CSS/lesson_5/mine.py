from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
   return render_template('lesson_5/temp/lesson_5.html')




if __name__ =='__main__':
    app.run()