//let longueur = document.getElementById(long).value;

//let tentatives = document.getElementById(tryNB).value;


function initJeu() {
    let tableau = document.getElementById("wordle");

    for (let i = 0; i < 5; i++) {
        let rang = document.createElement("div")
        rang.className = "rang"
        
        for (let j = 0; j < 5; j++) {
            let box = document.createElement("div")
            box.className = "case"
            rang.appendChild(box)
            box.textContent = '.';
        }

        tableau.appendChild(rang)
    }
}

initJeu()


let lettreSuiv = 0;

document.addEventListener("keyup",(e) => {
    if (tryNB === 0){
        return
    }

    key.textContent = e.key;

    if (key === "Backspace" && lettreSuiv !== 0){
        supprLettre()
        return
    }
})

function insertLettre(key){
    if (lettreSuiv == longueur){
        return
    }

    let rang = document.getElementsByClassName("rang")[6 - tryNB];
    let box = rang.children[lettreSuiv - 1];
    box.textContent = key
    box.classList.add("box-pleine")
}

function supprLettre(){
    let rang = document.getElementsByClassName("rang")[6 - tryNB];
    let box = rang.children[lettreSuiv - 1];
    box.textContent = ""
    box.classList.remove("box-pleine")
    currentGuess.pop()
    lettreSuiv = lettreSuiv -1
}