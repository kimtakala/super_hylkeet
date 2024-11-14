def verify_author(author):
    if len(author) < 2:
        return "Author field must include more than one character"
    
    if len(author) > 200:
        return "Author field must include less than 200 characters"
    
def verify_title(title):
    if len(title) < 2:
        return "Title must be longer than 1 character"
    
    if len(title) > 200:
        return "Title must be shorter than 200 characters"
    
def verify_year(year):
    if not isinstance(year, int):
        return "Year must be an integer"
    
    if year < 0:
        return "Year must be positive"
    
    if year > 2100:
        return "Year must be below 2100"
    
def verify_booktitle(title):
    if len(title) < 2:
        return "Booktitle must be longer than 1 character"
    
    if len(title) > 200:
        return "Booktitle must be shorter than 200 characters"
    
def verify_journal(journal):
    if len(journal) < 2:
        return "Journal name must be longer than 1 character"
    
    if len(journal) > 200:
        return "Journal name must be shorter than 200 characters"
    
def verify_volume(volume):
    if not isinstance(volume, int):
        return "Volume must be an integer"
    
    if volume < 1:
        return "Volume must be a positive integer"
    
def verify_pages(pages):
    if len(pages) > 50:
        return "Pages field must include less than 50 characters"
    
def verify_publisher(publisher):
    if len(publisher) < 2:
        return "Publisher field must include more than 1 character"
    
    if len(publisher) > 200:
        return "Publisher field must include less than 200 characters"