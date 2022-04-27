
// récuperer la longueur et le nb de tentative sans changer en direct
// du coup initialiser a chaque fois avec une liste des mots deja utilisés? 




let longueur = Number(recuplongueur());
let tentatives = Number(recuptentatives());
console.log("longueur",longueur);
console.log("tentatives",tentatives);
let infos = recupinfo();
console.log(infos);
let avancee = recupavancee();
let couleur = recupcouleurs();
let fini = recupfini();



function initJeu(longueur,tentatives,infos,avancee,couleur) {
    if (avancee != 0){
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
                if (i>=avancee){
                    box.textContent = ".";
                }
                else{
                    box.textContent = infos[i*longueur+j] ;
                    //let touche = document.getElementById(box.textContent)
                    //console.log(touche)
                    if (couleur[i*longueur+j] === "v"){
                        box.style.background = 'green'
                        touche.style.background = 'green'
                    }
                    else if (couleur[i*longueur+j] === "o"){
                        box.style.background = 'orange'
                        touche.style.background = 'orange'
                    }
                    else if (couleur[i*longueur+j] === "g"){
                        box.style.background = 'grey'
                        touche.style.background = 'grey'
                    }
                }
                
            }

            tableau.appendChild(rang)
        }   
    }
    else{
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
    
}

initJeu(longueur,tentatives,infos,avancee,couleur)

let elt1 = document.getElementById('long');
elt1.addEventListener('change', function () {
    longueur = Number(this.value);

    // let tableau = document.getElementById("wordle");
    // let i=0;
    // while (tableau.firstChild) {
    //     id = "ligne-" + i
    //     let rang = document.getElementById(id)
    //     while (rang.firstChild) {
    //         rang.removeChild(rang.firstChild);
    //     }
    //     i++;
    //     tableau.removeChild(tableau.firstChild);
    // }
    // lettreAct = 0
    // rangAct = 0
    console.log("ca passe?")
    pythonchange(longueur,tentatives)
    
})

let elt2 = document.getElementById('tryNB');
elt2.addEventListener('change', function () {
    tentatives = Number(this.value);

    // let tableau = document.getElementById("wordle");
    // let i=0;
    // while (tableau.firstChild) {
    //     id = "ligne-" + i
    //     let rang = document.getElementById(id)
    //     while (rang.firstChild) {
    //         rang.removeChild(rang.firstChild);
    //     }
    //     i++;
    //     tableau.removeChild(tableau.firstChild);
    // }
    // lettreAct = 0
    // rangAct = 0
    pythonchange(longueur,tentatives)
    
})

let lettreAct = 0;

let rangAct = Number(avancee);
console.log(avancee)

if (Number(fini)===1){
    rangAct=tentatives;
}


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
    location.reload()
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
    location.reload()
}
function pythonchange(longueur,tentatives){
    fetch("http://127.0.0.1:5000/recuplettre", 
    {
    method: 'POST',
    headers: {
    'Content-type': 'application/json',
    'Accept': 'application/json'
    },


    body:JSON.stringify("!"+longueur+"!"+tentatives)})
    //location.reload()
}

function recupinfo(){
    let infocouleur = document.getElementById("infos").innerHTML;
    console.log(infocouleur);
    return infocouleur
}
function recupcouleurs(){
    let infocouleurs = document.getElementById("couleurs").innerHTML;
    console.log(infocouleurs);
    return infocouleurs
}
function recupavancee(){
    let infoavance = document.getElementById("avancee").innerHTML;
    console.log(infoavance);
    return infoavance
}
function recupfini(){
    let infofini = document.getElementById("fini").innerHTML;
    console.log(infofini);
    return infofini
}
function recuplongueur(){
    let infolongueur = document.getElementById("longueur").innerHTML;
    console.log(infolongueur);
    return infolongueur
}
function recuptentatives(){
    let infotentatives = document.getElementById("tentatives").innerHTML;
    console.log(infotentatives);
    return infotentatives
}
//let bouton = document.getElementById("bouton")
//bouton.addEventListener('click', event => handleClick("Entrer") && python())