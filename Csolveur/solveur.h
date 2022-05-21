#ifndef SOLVEUR_H
#define SOLVEUR_H

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#include <assert.h>
#include <math.h>


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
int length(list_t *liste);
bool isEmpty(list_t *liste);
void retire(element_t *element,list_t* dico);
//char* removen(char* mot[]);                         // A MODIFIER
char* list_get(list_t *dico, int index);
int list_index_of(list_t *dico, char* mot);
element_t* list_element_of(list_t *dico, char* mot);
int occurences(char* mot,char lettre);
list_t* reduction_dico(char* mot,int pattern, list_t* dico);
//float nb_mots_possibles(char* mot,int pattern[nb_letters(mot)],list_t* dico);
//float entropie_initiale(char* mot);  nécessite une fonction qui calcule la la probabilité d'obtenir une combinaison à partir de l'ensemble des mots possibles après cette combinaison

char* solveur();   // ou fonction avec un while et fonction annexe qui fait le boulot





#endif
