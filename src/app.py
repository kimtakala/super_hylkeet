from form_verification import validate_citations
from services.citations_service import citation_service
from flask import render_template, jsonify, request
from db_helper import reset_db
from config import app, test_env


@app.route("/")
def index():
    citations = citation_service.get_citations()
    return render_template("index.html", listed_citations=citations)


@app.route("/add_citation", methods=["POST"])
def add_citation_route():
    citation = request.form

    errors = validate_citations(citation)
    if errors:
        return render_template("index.html", errors=errors)

    citation_service.add_citation(citation)
    success = "Citation added successfully"
    citations = citation_service.get_citations()
    return render_template("index.html", success=success, listed_citations=citations)


# testausta varten oleva reitti
if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({"message": "db reset"})
