#include "solveur.h"

int recupnb(){
    FILE* fichier=fopen("wsolf.txt","r");
    int longueur;

    fscanf(fichier,"%i",&longueur);
    printf("%i\n",longueur);
    fclose(fichier);
    return longueur;
}