#ifndef _SOLVEUR_H_
#define _SOLVEUR_H_

#include <stdlib.h>
#include <stdio.h>


typedef struct _element element;
struct _element{
    char mot[12];
    element *suivant;
};
typedef struct _liste liste;
struct _liste{
    element *head;
};

#endif