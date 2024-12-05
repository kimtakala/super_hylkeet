function hideAll() {
    document.getElementById("bookFields").style.display = "none";
    document.getElementById("articleFields").style.display = "none";
    document.getElementById("inproceedingsFields").style.display = "none";
    document.getElementById("miscFields").style.display = "none";
}

function showForm() {
    var content = document.getElementsByClassName("input_form")[0];

    var scrolled = false;
    if (window.scrollY) {
        window.scrollTo(0,0);
        scrolled = true;
    }
    
    if (content.style.display == "block") {
        if (scrolled == false) {
            content.style.display = "none";
        }
    } else {
        hideAll();
        document.getElementById('type').value = "";
        content.style.display = "block";
    }
}

function showArticleType() {
    hideAll();
    var content = document.getElementById("type");
    switch (content.value) {
        case "book":
            document.getElementById("bookFields").style.display = "block";
            break;
        case "article":
            document.getElementById("articleFields").style.display = "block";
            break;
        case "inproceedings":
            document.getElementById("inproceedingsFields").style.display = "block";
            break;
        case "misc":
            document.getElementById("miscFields").style.display = "block";
            break;
    }
}

function editArticleType(citation) {
    hideAll();
    var selector = document.getElementById("type");
    selector.value = citation.type;
    switch (citation.type) {
        case "book":
            document.getElementById("bookFields").style.display = "block";
            break;
        case "article":
            document.getElementById("articleFields").style.display = "block";
            break;
        case "inproceedings":
            document.getElementById("inproceedingsFields").style.display = "block";
            break;
        case "misc":
            document.getElementById("miscFields").style.display = "block";
            break;
    }

    // Fill fields with edit material
    for (const field_name in citation) {
        for (const field in document.getElementsByName(toString(field_name))) {
            field.placeholder = citation[field_name]
        }
    }
}