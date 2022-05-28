#include "solveur.h"

int main(){
    int nb_essais=0;
    int longueur = recupnb();
    list_t *dico = create_dico();
    

    //printf("longueur en dur de 10010 %i\n",nb_letters("10010"));




    char* mot = wordfinder(dico,nb_essais);
    
    printf("Is this your word ? : %s\n", mot);

    
    char* pattern;
    scanf("%s",&pattern);
    
    
    //dico_print(dico);
    //printf("Pattern donné en string: %s\n",&pattern);
    //printf("longueur de pattern %i\n",nb_letters(&pattern));
    

    nb_essais++;
    
    if (strcmp(&pattern,"-1")==0){
        printf("I won !\nThe word was %s\n1 try !\n",mot);
    }
    
    else {
        printf("Ca passe\n");
        while (strcmp(&pattern,"-1")!=0){
            
            dico=reduction_dico(mot,&pattern,dico);

            mot = wordfinder(dico,nb_essais);
            printf("Is this your word ? : %s\n", mot);

            
            
            scanf("%s",&pattern);
            nb_essais++;
        }
        printf("I won !\nThe word was %s\n%i tries\n",mot,nb_essais);
    }
    dico_destroy(dico);
}
