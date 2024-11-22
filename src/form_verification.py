#   Verifying functions return value if verification:
#   - Succeeds:
#       Nothing
#   - Fails:
#       Appropriate message

#   Fields author, title & year are mandatory


def verify_author(authors):
    if len(authors) > 200:
        return "Authors field must include less than 200 characters"
    
    authors = authors.split(',')

    for author in authors:
        names = author.split(' ')
        if len(names) < 2:
            return "Authors must be given in <FirstName LastName, FirstName LastName, ...> format"


def verify_title(title):
    if len(title) > 200:
        return "Title must be shorter than 200 characters"


def verify_year(year):
    if len(year) == 0:
        return "Year field is mandatory"

    year = int(year)

    if year < 0:
        return "Year must be a positive integer"

    if year > 2050:
        return "Year must be smaller than 2050"


def verify_booktitle(title):
    if len(title) > 200:
        return "Booktitle must be shorter than 200 characters"


def verify_journal(journal):
    if len(journal) > 200:
        return "Journal name must be shorter than 200 characters"


def verify_volume(volume):
    if len(volume) > 50:
        return "Volume field must include less than 50 characters"


def verify_pages(pages):
    if len(pages) > 50:
        return "Pages field must include less than 50 characters"


def verify_publisher(publisher):
    if len(publisher) > 200:
        return "Publisher field must include less than 200 characters"


def validate_citations(citation):
    errors = {}

    author_error = verify_author(citation["authors"])
    title_error = verify_title(citation["title"])
    year_error = verify_year(citation["year"])
    booktitle_error = verify_booktitle(citation.get("booktitle", ""))
    journal_error = verify_journal(citation.get("journal", ""))
    volume_error = verify_volume(citation.get("volume", ""))
    pages_error = verify_pages(citation.get("pages", ""))
    publisher_error = verify_publisher(citation["publisher"])

    if author_error:
        errors["authors"] = author_error
    if title_error:
        errors["title"] = title_error
    if year_error:
        errors["year"] = year_error
    if booktitle_error:
        errors["booktitle"] = booktitle_error
    if journal_error:
        errors["journal"] = journal_error
    if volume_error:
        errors["volume"] = volume_error
    if pages_error:
        errors["pages"] = pages_error
    if publisher_error:
        errors["publisher"] = publisher_error

    return errors
