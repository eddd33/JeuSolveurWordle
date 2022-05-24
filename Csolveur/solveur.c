#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "solveur.h"

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

list_t* create_dico(){   //dico est le nom de la liste contenant tous les mots d'une certaine longueur.
    int longueur=recupnb();
    list_t *dico=calloc(1,sizeof(list_t));
    
    FILE* fichier=fopen("motst.txt","r");
    int l=30;
    char ligne[l];
    //printf("bite %s\n",fgets(ligne,30,fichier));
    while (fgets(ligne,l,fichier) !=NULL){
        
        if (nb_letters(ligne)==longueur+1){
            //printf("%s",ligne);
            ajout_dico(strdup(ligne),dico);

        } 
        
        l++;
    }
    
    return dico;
}
// char* removen(char* mot[])
// {
//     char *adr_retour_ligne;
//     /* Recherche de l'adresse d'un \r ou d'un \n dans la variable mot */
//     adr_retour_ligne = strpbrk(mot, "\r\n");
//     /* Adresse trouvée ? */
//     if(adr_retour_ligne != NULL)
//     {
//         /* Remplacement du caractère par un octet nul (fin de chaîne en C) */
//         *adr_retour_ligne = 0;
//     }
//     //printf("'%s'", mot); /* 'Salut !' */
//     return mot;
// }
void ajout_dico(char* mot, list_t *dico){
    
    element_t *new_element = calloc(1,sizeof(element_t));
    
    new_element->ch1=mot;
    //printf("%s",new_element->ch1);
    new_element->next = NULL;
    element_t *current = dico->head;

    if (current == NULL)
    {
        dico->head = new_element;
        return;
    }
    while (current->next != NULL)
    {
        current = current->next;
    }
    current->next = new_element;
    //printf("%s",current->next->ch1);

}

void dico_destroy(list_t *dico)
{
    element_t *current = dico->head;
    element_t *tmp;
    while (current!= NULL)
    {
        tmp=current;
        
        current = current->next;
        free(tmp->ch1);
        free(tmp);
    };
    free(dico);
}

void element_print(element_t* mot){
    printf("%s ",mot->ch1);

}

void dico_print(list_t* dico){
    if (dico == NULL){
        exit(EXIT_FAILURE);
    }
    element_t *actuel = dico->head;
    
    if (actuel==NULL){
        printf("C'est vide\n");
    }
    else{
        printf("[ ");
        while (actuel != NULL){
            element_print(actuel);
            actuel = actuel->next;
        }
        printf("]\n ");
    }   
}



bool isEmpty(list_t *liste){
    if (liste->head==NULL){
        return true;
    }
    else{
        return false;
    }
}


int length(list_t *liste){
    int compteur=0;
    element_t *actuel=liste->head;
    
    while(actuel->next!=NULL){
        actuel=actuel->next;
        compteur++;
    }
    return compteur;
}

void retire(element_t *element,list_t* dico){
    if (!isEmpty(dico)){
        element_t* current=dico->head;
        element_t* previous;

        if (current==dico->head){
            dico->head=current->next;
            free(current->ch1);
            free(current);
        }
        else{
            while(current!=element && current!=NULL){
            previous=current;
            current=current->next;
            }
            if (current!=NULL && current->next!=NULL){
                element_t* suivant=current->next;
                free(current->ch1);
                free(current);
                previous->next=suivant;
            }
            if (current!=NULL && current->next==NULL){
                free(current->ch1);
                free(current);
            }
        }
        
    }
}

char* list_get(list_t *dico, int index) {
    assert(dico != NULL);
    assert(! isEmpty(dico));

    int pos = index;
    element_t *current = dico->head;
    
    while (pos > 0 && current->next != NULL) 
    {
        pos--;
        current = current->next;
    }
    assert(pos == 0);
    return current->ch1;
}

int list_index_of(list_t *dico, char* mot) {
    assert(dico != NULL);
    assert(!isEmpty(dico));

    int pos = 0;

    element_t *current = dico->head;    
    while (current->ch1 != mot && current->next != NULL) 
    {
        //printf("oskur %s",current->ch1);
        pos++;
        current = current->next;
    }
    printf("%s,%s",current->ch1,mot);
    if (current->ch1 == mot) {
        return pos;
    } else {
        return -1;
    }
}
element_t* list_element_of(list_t *dico, char* mot) {
    assert(dico != NULL);
    assert(!isEmpty(dico));


    element_t *current = dico->head;    
    while (current->ch1 != mot && current->next != NULL) 
    {
        //printf("oskur %s",current->ch1);
        current = current->next;
    }
    printf("%s,%s",current->ch1,mot);
    if (current->ch1 == mot) {
        return current;
    } else {
        return -1; 
    }
}


int occurences(char* mot,char lettre){
    int compteur=0;
    for (int i=0;i<nb_letters(mot);i++){
        if (mot[i]==lettre){
            compteur++;
        }
    }
    return compteur;
}

list_t* reduction_dico(char* mot,char* pattern, list_t* dico){
    int nb=nb_letters(mot);
    list_t* mots_possibles=dico;  //on créé un dico que l'on peut modifier sans conséquence pour cette fonction
    //dico_print(mots_possibles);
    char* présents;
    présents[nb]="\0";
    printf("pattern %s\n",pattern);
    for (int i=0;i<nb;i++){
        printf ("%c\n",pattern[i]);
        if (pattern[i]=='2'){
            présents[i]=mot[i];
            printf("presents %c\n",présents[i]);
            element_t* current=mots_possibles->head;
            while(current!=NULL){
                //printf("lettre %s",current->ch1[i]);
                element_t *suivant=current->next;
                if (current->ch1[i]!=mot[i]){
                    retire(current,mots_possibles);
                }
                current=suivant;
            }
        }
    }   
    for (int i=0;i<nb;i++){
        if (pattern[i]=='1'){
            présents[i]=mot[i];
        }
    }
    for (int i=0;i<nb;i++){
         if (pattern[i]=='0'){
            element_t* current=mots_possibles->head;
            while(current!=NULL){
                if (occurences(current->ch1,mot[i])>=occurences(présents,mot[i])){
                    retire(current,mots_possibles);
                    current=current->next;
                }
            } 
        }
    }

    return mots_possibles;
}


char* wordfinder(list_t dico){
    return "Pasfini";
}

int occurence(char* mot, char lettre){  //compte le nombre d'occurences d'une lettre dans un mot
    int compteur=0;
    for (int i=0;i<nb_letters(mot);i++){
        if(mot[i]==lettre){
            compteur++;
        }
    }
    return compteur;
}

// char* singularite(char* mot){
//     compteur=0;
//     for (int i=0;i<nb_letters(mot);i++){
//         if (in(mot[i],mot))
//     }
// }

bool in(char lettre,char* mot){
    for (int i=0;i<nb_letters(mot);i++){
        if (mot[i]==lettre){
            return true;
        }
    }
    return false;
}

char* hereofafter(char* mot,int index){
    printf("%s\n",mot+index);
    return mot + index;
}























// float nb_mots_possibles(char* mot,int pattern[nb_letters(mot)], list_t* dico){
//     int nb=nb_letters(mot);
//     list_t* motpossibles=create_dico();  //on créé un dico que l'on peut modifier sans conséquence pour cette fonction
//     int tot=length(motpossibles);
//     char* présents[nb];
//     for (int i=0;i<nb;i++){
//         if (pattern[i]==0){}
//             int occurence=occurences(mot,mot[i]);
//             retire(list_elementof(mots_possibles,mot))

//             //retirer de motpos tout les mots qui contiennent la lettre, necessite de verifier qu'on a pas déjà eu la lettre bonne une fois avant 
//         }
//         if (pattern[i]==1){
//             présents[i]=mot[i];
//             element_t* current=motpossibles->head;
//             while(current!=NULL){
//                 if (occurences(current->ch1,mot[i])==){
//                     retire(current);
//                     current=current->next;
//                 }
//             }
//         }
//         if (pattern[i]==2){
//             présents[i]=mot[i];
//             element_t* current=motpossibles->head;
//             while(current!=NULL){
//                 if (current->ch1[i]!=mot[i]){
//                     retire(current,motpossibles);
//                     current=current->next;
//                 }
//             }
//         }

//     }
//     int posssibilités=length(motpossibles);
//     dico_destroy(motpossibles);
//     return possibilités/tot;
// }

//float probabilite(char combinaison[??])

//float entropie_initiale(char* mot){
//    int longueur=nb_letters(mot);
//    return  entropie;
//}

