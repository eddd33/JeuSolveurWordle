#include "solveur.h"

int main(){
    int nb_essais=0;
    int longueur = recupnb();
    printf("Creating dictionnary...  \n");
    list_t *dico = create_dico();
    printf("Dictionnary created ! \n");

    //printf("longueur en dur de 10010 %i\n",nb_letters("10010"));




    char* mot;
    printf("Start searching... \n ");
    if (longueur<=12){
        mot=savedwords(longueur);
    }
    else{
        mot = wordfinder(dico,nb_essais);
    }
    
    //mot=savedwords(longueur);
    printf("Word found !\n");
    printf("Is this your word ? : %s\n", mot);

    
    char pattern[longueur+2];
    fgets(pattern,longueur+2,stdin);
    pattern[strlen(pattern)-1]=0;
    
    //dico_print(dico);
    //printf("Pattern donné en string: %s\n",&pattern);
    //printf("longueur de pattern %i\n",nb_letters(&pattern));
    

    nb_essais++;
    
    if (strcmp(pattern,"-1")==0){
        printf("I won !\nThe word was %s\n1 try !\n",mot);
    }
    
    else {

        while (strcmp(pattern,"-1")!=0){
            printf("Reducing dictionnary...\n  ");
            dico=reduction_dico(mot,pattern,dico);
            printf("Dictionnary reduced !\n");
            printf("Start searching...\n  ");
            mot = wordfinder(dico,nb_essais);
            printf("Word found !\n");
            printf("Is this your word ? : %s\n", mot);

            
            
            fgets(pattern,longueur+2,stdin);
            pattern[strlen(pattern)-1]=0;
            nb_essais++;
        }
        printf("I won !\nThe word was %s\n%i tries\n",mot,nb_essais);
    }
    dico_destroy(dico);
}
