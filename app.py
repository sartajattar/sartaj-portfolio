from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # हा कोड 'templates/index.html' ला लोड करतो
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)