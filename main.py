from flask import Flask

# create an instance of the Flask class you just imported
app = Flask(__name__)


@app.route("/")
def main():
    # display a string in the home page
    return "Welcome to my Flask Anpp"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
