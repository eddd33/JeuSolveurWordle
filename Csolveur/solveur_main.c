#include "solveur.h"

int main(){
    list_t *dico = create_dico();

    char* mot = wordfinder(*dico);
    printf("Is this your word ? : %s", mot);

    char* pattern;
    scanf("%s",&pattern);

    int longueur = recupnb();
    
    if (!(in("0",pattern) || in("1",pattern))){
        printf("I won !\nThe word was %s",mot);
    }

    else {
        while (in("0",pattern) || in("1",pattern)){
            reduction_dico(mot, pattern, dico);

            char* mot = wordfinder(*dico);
            printf("Is this your word ? : %s", mot);

            char* pattern;
            scanf("%s",&pattern);
        }
        printf("I won !\nThe word was %s",mot);
    }
}
