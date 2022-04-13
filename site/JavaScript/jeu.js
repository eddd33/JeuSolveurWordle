//let longueur = document.getElementById(long).value;

//let tentatives = document.getElementById(tryNB).value;


function initJeu() {
    let tableau = document.getElementById("wordle");

    for (let i = 0; i < 5; i++) {
        let rang = document.createElement("div")
        rang.className = "rang"
        rang.id = "ligne-" + i
        
        for (let j = 0; j < 5; j++) {
            let box = document.createElement("span")
            box.className = "case"
            box.id = "ligne-" + i + "-key-" + j
            rang.appendChild(box)
            box.textContent = '.';
        }

        tableau.appendChild(rang)
    }
}

initJeu()

let lettreAct = 0;

let rangAct = 0;

document.addEventListener("keyup",(e) => {


    let key = document.getElementById("key");
    //key.textContent = e.key;
    //console.log(e.key);

    if (tryNB === 0){
        return
    }
    
    let pressKey = String(e.key);

    console.log(pressKey);

    if (pressKey === "Backspace" && lettreSuiv !== 0){
        supprLettre()
        return
    }

    let guess = pressKey.match(/[A-Z]/gi)
    if (!guess || guess.length > 1){
        return
    } else{
        insertLettre(pressKey)
    }

})

function insertLettre(key){
    if (lettreAct < 5 && rangAct < 5 ){
        const boite = document.getElementById('ligne-' + rangAct + '-key-' + lettreAct)
        boite.textContent = key

        boite.setAttribute('data', key)
        lettreAct++
    }

    //key = key.toLowerCase()

    //let rang = document.getElementById("ligne")[5 - 5];
    //let box = rang.children[lettreSuiv];
    //box.textContent = key
    //box.classList.add("box-pleine")
    //lettreSuiv = lettreSuiv +1
}

function supprLettre(){
    let rang = document.getElementsByClassName("rang")[6 - tryNB];
    let box = rang.children[lettreSuiv - 1];
    box.textContent = ""
    box.classList.remove("box-pleine")
    currentGuess.pop()
    lettreSuiv = lettreSuiv -1
}