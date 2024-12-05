function toggleDetails(detailsId, arrowId) {
    var details = document.getElementById(detailsId);
    var arrow = document.getElementById(arrowId);
    if (details.style.display === "none") {
        details.style.display = "block";
        arrow.innerHTML = "&#x25BC;";
    } else {
        details.style.display = "none";
        arrow.innerHTML = "&#x25B6;";
    }
}

function toggleCheckboxes(checked) {
    var checkboxes = document.querySelectorAll('input[name="citations"]');
    checkboxes.forEach(function (checkbox) {
        checkbox.checked = checked;
    });
}


function toggleBibtex() {
    var bibtexTextarea = document.getElementById("bibtexTextarea");
    if (bibtexTextarea.style.display === "none") {
        bibtexTextarea.style.display = "block";
    } else {
        bibtexTextarea.style.display = "none";
    }
}

function deleteCitation(citationId) {
    fetch(`/delete_citation/${citationId}`, {
        method: 'POST'
    })
        .then(response => {
            if (response.ok) {
                location.reload();
            }
        })

}

function editCitation(citation) {
    window.scrollTo(0,0);
    
    // Change submit button
    const btns = document.getElementsByClassName("submit-btn");
    for (button of btns) {
        button.classList.remove("submit-btn");
        button.classList.add("submit-edit-btn");
    }
    
    const content = document.getElementsByClassName("input_form")[0];
    content.style.display = "block";
    
    document.getElementById("exitEditMode").style.display = "inline-block";
    editArticleType(citation);
}

// ----------------- citations.js -----------------------

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
    for (const form of document.getElementsByClassName("form")) {
        const url = "/edit_citation/".concat(citation.title);
        form.action = url;
    }
    
    // Show form to edit
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
        fields = document.getElementsByName(field_name);
        for (const field of fields) {
            field.value = citation[field_name];
        }
    }
}

function exit_editing_mode() {
    // Change submit button
    const btns = document.getElementsByClassName("submit-edit-btn");
    for (button of btns) {
        button.classList.remove("submit-edit-btn");
        button.classList.add("submit-btn");
    }

    for (const form of document.getElementsByClassName("form")) {
        form.action = "/add_citation/";
    }

    document.getElementById("exitEditMode").style.display = "none";
}