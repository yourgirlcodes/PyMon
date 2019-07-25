var filters = document.getElementsByClassName("filter");
var games = document.getElementsByClassName("game");

for(let i=0; i<filters.length; i++) {
    filters[i].addEventListener("click", applyFilter);
}

function applyFilter(e) {
    filter = e.target.innerText.toLowerCase();
    if(filter == "all") {
        for(let m=0; m<games.length; m++) {
            games[m].classList.remove("hidden")
        }
    }
    else{
        for(let n=0; n<games.length; n++) {
            games[n].classList.remove("hidden");
            if (!games[n].classList.contains(filter)){
                games[n].classList.add("hidden")
            }
        }
    }
}