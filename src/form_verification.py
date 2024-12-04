#   Verifying functions return value if verification:
#   - Succeeds:
#       Nothing
#   - Fails:
#       Appropriate message

#   Fields author, title & year are mandatory


def verify_author(authors):
    if authors == "":
        return "Authors is a required field"
    if len(authors) > 200:
        return "Authors field must include less than 200 characters"

    authors = authors.split(', ')

    for author in authors:
        names = author.split(' ')
        if len(names) < 2:
            return "Authors must be given in <FirstName LastName,"\
                " FirstName LastName, ...> format"

    return None


def verify_title(title):
    if title == "":
        return "Title is a required field"
    if len(title) > 200:
        return "Title must be shorter than 200 characters"

    return None


def verify_year(year):
    if year == "":
        return "Year is a required field"
    if year != "":
        year = int(year)

        if year < 0:
            return "Year must be a positive integer"

        if year > 2050:
            return "Year must be smaller than 2050"

    return None


def verify_booktitle(title):
    if title == "":
        return "Booktitle is a required field"
    if len(title) > 200:
        return "Booktitle must be shorter than 200 characters"

    return None


def verify_journal(journal):
    if journal == "":
        return "Journal is a required field"
    if len(journal) > 200:
        return "Journal name must be shorter than 200 characters"

    return None


def verify_volume(volume):
    if len(volume) > 50:
        return "Volume field must include less than 50 characters"

    return None


def verify_pages(pages):
    if len(pages) > 50:
        return "Pages field must include less than 50 characters"

    return None


def verify_publisher(publisher):
    if publisher == "":
        return "Publisher is a required field"
    if len(publisher) > 200:
        return "Publisher field must include less than 200 characters"

    return None


def validate_citations(citation):
    checks = {}

    checks["authors"] = verify_author(citation["authors"])
    checks["title"] = verify_title(citation["title"])
    checks["year"] = verify_year(citation["year"])
    checks["booktitle"] = verify_booktitle(citation.get("booktitle", ""))
    checks["journal"] = verify_journal(citation.get("journal", ""))
    checks["volume"] = verify_volume(citation.get("volume", ""))
    checks["pages"] = verify_pages(citation.get("pages", ""))
    checks["publisher"] = verify_publisher(citation["publisher"])

    required_fields = {"article": ["authors", "title", "journal", "year"],
                       "book": ["authors", "title", "publisher", "year"],
                       "inproceedings": ["authors", "title", "booktitle", "year"],
                       "misc": []
                       }

    errors = {}

    # Move all the required field for this datatype from checks to errors.
    for field in required_fields[citation["type"]]:
        if checks[field]:
            errors[field] = checks[field]

    # Move all not empty not required field from checks to errors.
    for k, v in citation.items():
        if v != "" and k not in required_fields[citation["type"]]\
                and k in checks and checks[k]:
            errors[k] = checks[k]

    return errors
