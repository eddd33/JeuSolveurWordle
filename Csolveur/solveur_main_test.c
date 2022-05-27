#include "solveur.h"

int main(){
    int nb_essais=0;
    int longueur = recupnb();
    list_t *dico = create_dico();
    
    char* mot = wordfinder(dico,nb_essais);
    
    printf("Is this your word ? : %s\n", mot);

    
    int patternint;
    scanf("%i",&patternint);
    char* pattern=inttochar(patternint);
    
    printf("Pattern donné en string: %s\n",pattern);

    nb_essais++;
    
    if (!(in('0',pattern) || in('1',pattern))){
        printf("I won !\nThe word was %s\n",mot);
    }
    
    else {
        printf("Ca passe\n");
        while (in('0',pattern) || in('1',pattern)){
            
            dico=reduction_dico(mot, pattern, dico);

            mot = wordfinder(dico,nb_essais);
            printf("Is this your word ? : %s\n", mot);

            char* pattern;
            int patternint;
            scanf("%d",&patternint);
            sprintf(pattern,"%d",patternint);
            nb_essais++;
        }
        printf("I won !\nThe word was %s\n",mot);
    }
    dico_destroy(dico);
}
