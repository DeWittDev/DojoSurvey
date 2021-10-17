from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Standing Man"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results')
def results():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)