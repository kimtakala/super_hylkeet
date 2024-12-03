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