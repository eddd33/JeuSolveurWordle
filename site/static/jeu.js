
// récuperer la longueur et le nb de tentative sans changer en direct
// du coup initialiser a chaque fois avec une liste des mots deja utilisés? 




let longueur = 5;
let tentatives = 6;

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

    let Sup = document.getElementById("Sup")
    Sup.addEventListener('click', () => handleClick(Sup.textContent))

    let a = document.getElementById("A")
    a.addEventListener('click', () => handleClick(a.textContent))

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

    else if (key === "A" && lettreAct < longueur){
        insertLettre(key)
    }
}


function insertLettre(key){
    if (lettreAct < longueur && rangAct < tentatives ){
        const boite = document.getElementById('ligne-' + rangAct + '-key-' + lettreAct)
        boite.textContent = key

        boite.setAttribute('data', key)
        pythonajout(rangAct,lettreAct)
        lettreAct++
        

    }

}

function supprLettre(){
    if (lettreAct > 0) {
        lettreAct--
        pythonsuppr()
        const boite = document.getElementById('ligne-' + rangAct + '-key-' + lettreAct)
        boite.textContent = '.'
        
        boite.setAttribute('data', '')
    }

}

function checkGuess(){
    pythonvalide()
    rangAct++
    lettreAct = 0
    recupinfo()
}

// dans la fonction suivante premiere est la lettre que l'on vient de rentrer
function pythonajout(ligne,lettre){
    let premiere = document.getElementById("ligne-"+ligne+"-key-"+lettre).innerHTML;
    console.log(premiere);
    fetch("http://127.0.0.1:5000/recuplettre", 
    {
    method: 'POST',
    headers: {
    'Content-type': 'application/json',
    'Accept': 'application/json'
    },


    body:JSON.stringify(premiere)})
}
function pythonsuppr(){
    fetch("http://127.0.0.1:5000/recuplettre", 
    {
    method: 'POST',
    headers: {
    'Content-type': 'application/json',
    'Accept': 'application/json'
    },


    body:JSON.stringify("suppr")})
}
function pythonvalide(){
    fetch("http://127.0.0.1:5000/recuplettre", 
    {
    method: 'POST',
    headers: {
    'Content-type': 'application/json',
    'Accept': 'application/json'
    },


    body:JSON.stringify("valide")})
}


function recupinfo(){
    let infocouleur = document.getElementById("infos").innerHTML;
    console.log(infocouleur);
}
//let bouton = document.getElementById("bouton")
//bouton.addEventListener('click', event => handleClick("Entrer") && python())