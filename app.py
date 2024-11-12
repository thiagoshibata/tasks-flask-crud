from flask import Flask

# manual: __name = "__main__"
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

@app.route("/about")
def about():  
  return "<h1>Página sobre</h1>"

if __name__ == "__main__":
  app.run(debug=True)