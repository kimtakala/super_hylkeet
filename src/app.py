from flask import render_template, jsonify, request, redirect, url_for, flash
from form_verification import validate_citations
from services.citations_service import citation_service
from db_helper import reset_db
from config import app
import bibtex_ref_gen


@app.route("/", methods=["GET", "POST"])
def index():
    search = "" if request.method == "GET" else request.form["search"]
    citations = citation_service.fetch_citations(search_key=search)
    return render_template("index.html", listed_citations=citations)


@app.route("/add_citation", methods=["POST"])
def add_citation_route():
    citation = request.form

    data = citation_service.fill_data_with_nones(citation)

    errors = validate_citations(data)

    if errors:
        return render_template("index.html", errors=errors)

    citation_service.add_citation(data)
    flash("Citation added successfully!", "success")
    return redirect(url_for("index"))


@app.route("/generate_bibtex", methods=["POST"])
def generate_bibtex_route():
    selected_citation_ids = request.form.getlist("citations")
    citations = citation_service.get_citations_for_bibtex(selected_citation_ids)

    bibtex_entries = bibtex_ref_gen.generate_references(citations)

    bibtex_output = "\n\n".join(bibtex_entries)
    return redirect(url_for("index", bibtex=bibtex_output))


@app.route("/delete_citation/<int:id>", methods=["POST"])
def delete_citation(id):
    citation_service.delete_citation_by_id(id)
    citations = citation_service.fetch_citations()
    citation_service.fetch_citations()

    return redirect(url_for("index", listed_citations=citations))


@app.route("/sort_citations", methods=["POST"])
def sort_citations_route():
    sorting_key = request.form["sorting_key"]
    sorting_order = request.form["sorting_order"]
    citations = citation_service.fetch_citations(
        sorting_key=sorting_key, sorting_order=sorting_order
    )
    return render_template("index.html", listed_citations=citations)


# testausta varten oleva reitti
@app.route("/reset_db")
def reset_database():
    reset_db()
    return jsonify({"message": "db reset"})
