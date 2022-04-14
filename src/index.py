from flask import Flask, render_template

app = Flask(__name__)

# Rutas
@app.route('/')
def home():
    return render_template("home.html")


# para que se mantenga corriendo
if __name__ == '__main__':
    app.run(debug=True)
