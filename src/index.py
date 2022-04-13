from flask import Flask, render_template

app = Flask(__name__)

# rutas simples
@app.route('/test')
def test():
    return "Home Page 1 "

@app.route('/test/about/')
def about_test():
    return "About Page 1"

# Rutas
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

# para que se mantenga corriendo
if __name__ == '__main__':
    app.run(debug=True)
