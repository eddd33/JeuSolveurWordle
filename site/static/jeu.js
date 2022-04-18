//let longueur = document.getElementById(long).value;

//let tentatives = document.getElementById(tryNB).value;


function initJeu() {
    let tableau = document.getElementById("wordle");

    for (let i = 0; i < 4; i++) {
        let rang = document.createElement("div")
        rang.className = "rang"
        rang.id = "ligne-" + i
        
        for (let j = 0; j < 8; j++) {
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
    if (key === "Entrer" && lettreAct === 5){
        checkGuess()
    }
}

function insertLettre(key){
    if (lettreAct < 5 && rangAct < 5 ){
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