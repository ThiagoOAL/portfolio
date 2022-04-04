from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("estrutura.html")

@app.route('/sobre')
def sobre():
    return render_template("sobre.html")

@app.route('/projetos')
def projeto():
    return render_template('projetos.html')

@app.route('/paixao')
def paixao():
    return render_template('paixao.html')


if __name__ == '__main__':
    app.run(debug=False)
