from flask import redirect, render_template, jsonify, request
from db_helper import reset_db
from config import app, test_env
from repositories.citation_repository import add_citation, get_citations
from form_verification import validate_citations


@app.route("/")
def index():
    citations = get_citations()
    return render_template("index.html", listed_citations=citations)


@app.route("/add_citation", methods=["POST"])
def add_citation_route():
    citation = request.form
    """
    DATA VERIFICATION STILL IN PROGRESS
    errors = validate_citations(citation)
    if errors:
        return render_template("index.html", errors=errors)
    """
    add_citation(citation)
    return redirect("/")


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
