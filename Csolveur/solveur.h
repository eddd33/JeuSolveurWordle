#ifndef SOLVEUR_H
#define SOLVEUR_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct _element_t element_t;
struct _element_t
{
    char* ch1;
    element_t *next;
};

typedef struct _list_t list_t;
struct _list_t
{
    element_t *head;
};


int nb_letters(char* mot);

list_t* create_dico();
void ajout_dico(char* mot, list_t *dico);
void dico_destroy(list_t *dico);
void dico_print(list_t* dico);
void element_print(element_t* mot);
//float nb_mots_possibles(char* mot,char pattern[nb_letters(mot)]);
//float entropie_initiale(char* mot);  nécessite une fonction qui calcule la la probabilité d'obtenir une combinaison à partir de l'ensemble des mots possibles après cette combinaison

char* solveur();   // ou fonction avec un while et fonction annexe qui fait le boulot





#endif