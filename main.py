from flask import Flask, request, render_template, flash, url_for, redirect
from unscrambler import unscramble, getAllKombos
from pprint import pprint


app = Flask(__name__)
app.secret_key="my secret"


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=["POST"])
def index_post():
    error = None
    text = request.form["letters"]
    
    # Unscrabble the text received
    unscrabbled_dict = unscramble(getAllKombos(text))
    # Join the letters with a comma delimiter
    
    words_list = [", ".join(word) for word in unscrabbled_dict.values()]
    result = dict(zip(unscrabbled_dict.keys(), words_list))
    
    if unscrabbled_dict == {}:
        flash("No words are available")
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)