from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'

port = os.environ.get("PORT", 5000)
app.run(debug=False, host="0.0.0.0", port=port)
    
