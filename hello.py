from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

# @app.route('/hello')
# def hello():
#     return 'Hello World'

@app.route('/hello')
def hello():
    return render_template('index.html')

@app.route('/hello/<name>')
def helloTemplate(name=None):
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run()
