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
