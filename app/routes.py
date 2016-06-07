from flask import Flask, render_template

app = Flask(__name__)


# render home page
@app.route('/')
def home():
    return render_template('home.html')


# rendering the about page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
