from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create/review', methods=['POST'])
def create_review():
    if Dojo.validate_dojo(request.form):
        Dojo.save(request.form)
        return redirect('/result')
    return redirect('/')

@app.route('/result')
def show_result():
    return render_template('result.html', dojo=Dojo.get_survey())
