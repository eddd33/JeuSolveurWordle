#ifndef SOLVEUR_H
#define SOLVEUR_H

#include <stdlib.h>
#include <stdio.h>

typedef struct _element_t element_t;
struct _element_t
{
    char* ch1;
    char* ch2;
    element_t *next;
};

typedef struct _list_t list_t;
struct _list_t
{
    element_t *head;
};

typedef struct _dico dico;
struct _dico{
    list_t **lists;
    int size;
};

int nb_letters(char* mot);

void create_dico();
void ajout_dico(dico dico,char* mot,int longueur);

char* solveur();   // ou fonction avec un while et fonction annexe qui fait le boulot





#endif