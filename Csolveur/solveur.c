#include "solveur.h"
#include "string.h"

int recupnb(){
    FILE* fichier=fopen("wsolf.txt","r");
    int longueur;

    fscanf(fichier,"%i",&longueur);
    printf("%i\n",longueur);
    fclose(fichier);
    return longueur;
}

int nb_letters(char* mot){
    return strlen(mot);

    
}