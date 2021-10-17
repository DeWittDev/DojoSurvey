from flask import Flask, render_template, redirect, request, session
app = Flask(__name__)
app.secret_key = "Standing Man"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['fav'] = request.form['fav']
    session['textbox'] = request.form['textbox']
    return redirect('/result')

@app.route('/result')
def results():
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)