from flask import Flask, render_template, session, request
app = Flask(__name__)
app.secret_key = 'Secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    print("Got Post info")
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return render_template('result.html')

if __name__=='__main__':
    app.run(debug=True)