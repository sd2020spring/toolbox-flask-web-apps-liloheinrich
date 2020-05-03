""" Flask webapp for a simple form.
"""

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('questions.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_age = request.form['user_age']
        user_ninja = request.form['user_ninja']
        if len(user_name) > 0 and len(user_age) > 0 and len(user_ninja) > 0:
            return redirect(url_for('success',name = user_name, age = user_age))
        else:
            return redirect(url_for('error'))
    else:
        return 'Something went wrong'

@app.route('/success/<name>?<age>')
def success(name, age):
   return render_template('response.html', name=name, age=age)

@app.route('/error')
def error():
    return render_template('error.html')

@app.route('/restart',methods = ['POST', 'GET'])
def restart():
    if request.method == 'POST':
        return redirect(url_for('index'))
    else:
        return 'Something went wrong'

if __name__ == '__main__':
    app.run()
