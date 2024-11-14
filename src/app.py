from flask import redirect, render_template, jsonify
from db_helper import reset_db
from config import app, test_env
from references import add_reference


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add_reference", methods=["POST"])
def add_reference_route():
    # validaatiofunktio tähän
    add_reference()
    return redirect("/")


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
