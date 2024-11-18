from flask import Flask

app = Flask(__name__)  # Initializes the Flask application with the current module name

@app.route('/')
def home():
    return "<div>Hello There</div>"

if __name__ == '__main__':
    app.run(debug=True)