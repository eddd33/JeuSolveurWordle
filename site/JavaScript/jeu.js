//let longueur = document.getElementById(long).value;

//let tentatives = document.getElementById(tryNB).value;


function initJeu() {
    let tableau = document.getElementById("wordle");

    for (let i = 0; i < 5; i++) {
        let rang = document.createElement("div")
        rang.className = "rang"
        
        for (let j = 0; j < 5; j++) {
            let box = document.createElement("span")
            box.className = "case"
            box.id = "key"
            rang.appendChild(box)
            box.textContent = '.';
        }

        tableau.appendChild(rang)
    }
}

initJeu()


//let lettreSuiv = 0;

document.addEventListener("keyup",(e) => {


    let key = document.getElementById("key");
    key.textContent = e.key;
    console.log(e.key);

    if (tryNB === 0){
        return
    }
    

    if (key === "Backspace" && lettreSuiv !== 0){
        supprLettre()
        return
    }

    //let guess = key.match(/[A-Z]/)
    //if (!guess){
      //  return
    //} else{
      //  insertLettre(key)
    //}

})

function insertLettre(key){
    if (lettreSuiv == longueur){
        return
    }

    let rang = document.getElementsByClassName("rang")[6 - tryNB];
    let box = rang.children[lettreSuiv - 1];
    box.textContent = key
    box.classList.add("box-pleine")
    lettreSuiv = lettreSuiv +1
}

function supprLettre(){
    let rang = document.getElementsByClassName("rang")[6 - tryNB];
    let box = rang.children[lettreSuiv - 1];
    box.textContent = ""
    box.classList.remove("box-pleine")
    currentGuess.pop()
    lettreSuiv = lettreSuiv -1
}