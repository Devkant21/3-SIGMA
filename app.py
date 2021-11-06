from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/About")
def About():
    return render_template('about.html')

@app.route("/BYTES_OF_SIGMA")
def BYTES_OF_SIGMA():
    return render_template('BYTES_OF_SIGMA.html')

if __name__=='__main__':
    app.run()