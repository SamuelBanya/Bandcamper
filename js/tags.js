function genreSelect() {
    var genreDropdownMenu = document.getElementById("genre-select");
    genreTag = genreDropdownMenu.value;
    window.open(genreTag, "_blank");
}

document.getElementById("genreGoButton").addEventListener("click", genreSelect);

function locationSelect() {
    var locationDropdownMenu = document.getElementById("location-select");
    locationTag = locationDropdownMenu.value;
    window.open(locationTag, "_blank");
}

document.getElementById("locationGoButton").addEventListener("click", locationSelect);
