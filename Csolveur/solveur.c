#include <assert.h>
#include <string.h>
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

void ajout_dico(char* mot, list_t *dico){
    
    element_t *new_element = malloc(sizeof(element_t));
    
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
    printf("%s",current->next->ch1);

}

void dico_destroy(list_t *dico)
{
    element_t *current = dico->head;
    element_t *tmp;
    while (current!= NULL)
    {
        tmp=current;
        current = current->next;
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
        printf("]\n");
    }
    
     
}

//float nb_mots_possibles(char* mot,int pattern[nb_letters(mot)]){
    //int nb=nb_letters(mot);
    //char motsatest[]=dico[nb];  Il faudrait pouvoir accéder au dico pour parcourir les mots, mais comme on créé le dico dans le main a priori, je vois pas trop
    //char motpos[];   //Il faudrait initialiser cette liste comme une copie de motsatest mais on ne peut pas juste mettre un égal sinon on modifiera les données en mémoire 
    //int tot=size(motsatest);
    //for (int i=0;i<nb;i++){
        //if (pattern[i]==0){
            //retirer de motpos tout les mots qui contiennent la lettre, necessite de verifier qu'on a pas déjà eu la lettre bonne une fois avant 
        //}
        //if (pattern[i]==1){
            //retirer de motpos tout les mots qui ne contiennent pas la lettre
        //}
        //if (pattern[i]==2){
            //retirer de motpos tout les mots qui ne contiennent pas la lettre en position i
        //}

    //}
    //return size(motpos)/tot;
//}

//float probabilite(char combinaison[??])

//float entropie_initiale(char* mot){
//    int longueur=nb_letters(mot);
//    return  entropie;
//}

