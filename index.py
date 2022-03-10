from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc123@567$#'
    
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()