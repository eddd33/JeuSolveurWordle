let longueur = 5;
let tentatives = 5;


function initJeu(longueur,tentatives) {
    let tableau = document.getElementById("wordle");

    for (let i = 0; i < tentatives; i++) {
        let rang = document.createElement("div")
        rang.className = "rang"
        rang.id = "ligne-" + i
        
        for (let j = 0; j < longueur; j++) {
            let box = document.createElement("span")
            box.className = "case"
            box.id = "ligne-" + i + "-key-" + j
            rang.appendChild(box)
            box.textContent = '.';
        }

        tableau.appendChild(rang)
    }
}

initJeu(longueur,tentatives)

let elt1 = document.getElementById('long');
elt1.addEventListener('change', function () {
    longueur = Number(this.value);

    let tableau = document.getElementById("wordle");
    let i=0;
    while (tableau.firstChild) {
        id = "ligne-" + i
        let rang = document.getElementById(id)
        while (rang.firstChild) {
            rang.removeChild(rang.firstChild);
        }
        i++;
        tableau.removeChild(tableau.firstChild);
    }
    lettreAct = 0
    rangAct = 0
    initJeu(longueur,tentatives)
    
})

let elt2 = document.getElementById('tryNB');
elt2.addEventListener('change', function () {
    tentatives = Number(this.value);

    let tableau = document.getElementById("wordle");
    let i=0;
    while (tableau.firstChild) {
        id = "ligne-" + i
        let rang = document.getElementById(id)
        while (rang.firstChild) {
            rang.removeChild(rang.firstChild);
        }
        i++;
        tableau.removeChild(tableau.firstChild);
    }
    lettreAct = 0
    rangAct = 0
    initJeu(longueur,tentatives)
    
})

let lettreAct = 0;

let rangAct = 0;

document.addEventListener("keyup",(e) => {


    let key = document.getElementById("key");

    if (tryNB === 0){
        return
    }
    
    let pressKey = String(e.key);

    console.log(pressKey);

    if (pressKey === "Backspace" && lettreAct !== 0){
        supprLettre()
        return
    }

    let guess = pressKey.match(/^[A-Za-z]$/)
    if (!guess || guess.length > 1){
        return
    } else{
        insertLettre(pressKey)
    }

    let Enter = document.getElementById("Enter")
    Enter.addEventListener('click', () => handleClick(Enter.textContent))


})

function handleClick(key){
    if (key === "Entrer" && lettreAct === longueur){
        checkGuess()
    }
}

function insertLettre(key){
    if (lettreAct < longueur && rangAct < tentatives ){
        const boite = document.getElementById('ligne-' + rangAct + '-key-' + lettreAct)
        boite.textContent = key

        boite.setAttribute('data', key)
        lettreAct++

    }

}

function supprLettre(){
    if (lettreAct > 0) {
        lettreAct--
        const boite = document.getElementById('ligne-' + rangAct + '-key-' + lettreAct)
        boite.textContent = '.'
        
        boite.setAttribute('data', '')
    }

}

function checkGuess(){
    rangAct++
    lettreAct = 0
}