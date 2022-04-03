function initJeu() {
    let tableau = document.getElementById("wordle");

    for (let i = 0; i < 7; i++) {
        let rang = document.createElement("div")
        rang.className = "rang-lettre"
        
        for (let j = 0; j < 5; j++) {
            let box = document.createElement("div")
            box.className = "case-lettre"
            rang.appendChild(box)
            box.textContent = '.';
        }

        tableau.appendChild(rang)
    }
}

initJeu()