#include <assert.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include "solveur.h"

int recupnb(){
    FILE* fichier=fopen("wsolf.txt","r");
    int longueur;

    fscanf(fichier,"%i",&longueur);
    fclose(fichier);
    return longueur;
}

int nb_letters(char* mot){
    return strlen(mot);
}


list_t* create_dico(){   //dico est le nom de la liste contenant tous les mots d'une certaine longueur.
    int longueur=recupnb();                 //on recupere la longueur des mots a traiter
    list_t *dico=calloc(1,sizeof(list_t)); // on alloue de la mémoire au dico
    dico->head=NULL;
    FILE* fichier=fopen("motst.txt","r");  // on ouvre le txt des mots du dictionnaire
    int l=30;                               // longueur max des mots 
    char *ligne[l];                         //initialisation de la variable ligne qui va accueillir chaque mot 
    while (fgets(ligne,l,fichier) !=NULL){  //ligne accueille le mot de la ligne
        
        if (nb_letters(ligne)==longueur+1){
            char* dup=strdup(ligne);        // on le duplique pour pouvoir l'ajouter dans le dico sans probleme de pointeur
            ajout_dico(hereorbefore(dup,longueur),dico); // on ajoute le mot sans le dernier caractere qui est le \n
            free(dup);                              // on libere la memoire
        } 
        

    }
    fclose(fichier);
    return dico;
}

void ajout_dico(char* mot, list_t *dico){
    
    element_t *new_element = calloc(1,sizeof(element_t));
    
    new_element->ch1=mot;
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
    }
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
    
    while(actuel!=NULL){
        actuel=actuel->next;
        compteur++;
    }
    return compteur;
}

void retire(element_t *element,list_t* dico){

    if (!isEmpty(dico)){                    //on vérifie que le dictionnaire n'est pas vide
        element_t* current=dico->head;      //on initialise notre élément courant à la tête de la liste
        element_t* previous;                //on prévoit de garder en mémoire l'élément précédant courant

        if (current==dico->head && current==element){          //si l'élément à retirer est la tête de liste
            dico->head=current->next;                           //on donne à la liste pour nouvelle tête le suivant de la tête
            free(current->ch1);
            free(current);                                      //on free l'élément
        }

        else{
            while(current!=element && current!=NULL){           //on cherche l'élément dans la liste
                previous=current;           
                current=current->next;                          //on parcourt jusqu'à trouver l'élément
            }
            if (current!=NULL && current->next!=NULL){          //si on à trouvé l'élément (cad que current n'est pas vide) et qu'il a un suivant
                element_t* suivant=current->next;               //on enregistre sont suivant
                free(current->ch1);
                free(current);                                  //on free l'élément
                previous->next=suivant;                         //on reconnecte la liste en donnant pour suivaant au précédent de l'élément son suivant
            }
            else if (current!=NULL && current->next==NULL){     //si on à trouvé l'élément (cad que current n'est pas vide) et qu'il n'a pas de suivant
                printf("on retire le dernier %s\n",current->ch1);
                previous->next==NULL;
                free(current->ch1);
                free(current);                                  //on free l'élément
                
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
    while (strcmp(current->ch1,mot)!=0 && current->next != NULL) 
    {   
        pos++;
        current = current->next;
    }
    return pos;
    
}
element_t* list_element_of(list_t *dico, char* mot) {
    assert(dico != NULL);
    assert(!isEmpty(dico));
    element_t *current = dico->head;    
    while (current->ch1 != mot && current->next != NULL) 
    {
        current = current->next;
    }
    printf("%s,%s",current->ch1,mot);
    if (current->ch1 == mot) {
        return current;
    }
}


int occurrences(char* mot,char lettre){
    int compteur=0;
    for (int i=0;i<nb_letters(mot);i++){
        if (mot[i]==lettre){
            compteur++;
        }
    }
    return compteur;
}

list_t* reduction_dico(char* mot,char* pattern, list_t* dico){   //fonction prenant en paramètre le mot proposé par le solveur et le pattern renvoyé par l'utilisateur ainsi que le dictionnaire des mots encore possible avant cette étape
    int nb=nb_letters(mot);
    element_t* current=dico->head;
    list_t* newdico=malloc(sizeof(list_t));
    newdico->head=NULL;
    int a=0;
    int b=0;
    while (current!=NULL){  // on parcourt tout le dico
        a=0;
        b=0;
        for (int i=0;i<nb;i++){      //
            if (pattern[i]=='2'){
                if (current->ch1[i]!=mot[i]){   //si la lettre n'est pas bonne
                    a+=1;   
                }
            }
            else if (pattern[i]=='1'){
                if (current->ch1[i]==mot[i]){  // si la lettre mal placée est tjr mal placée
                    a+=1;
                }
                else if(!in(mot[i],current->ch1)){  // si la lettre mal placée n'est pas dans le mot
                    a+=1;
                }
            }
            else if (pattern[i]=='0'){
                for (int k=0;k<nb;k++){
                    if (k!=i){
                        if (mot[k]==mot[i] && pattern[k]=='2'){
                            b+=1;
                        }
                        else if(mot[k]==mot[i] && pattern[k]=='1'){
                            b+=1;
                        }
                    }
                }
                if (occurrences(current->ch1,mot[i])>b){
                        a+=1;
                    }
            }
            
            
        }
        if (a==0){
            ajout_dico(strdup(current->ch1),newdico);
        }
        current=current->next;
        
    }
    dico_destroy(dico);
    return newdico;
    
}

char* inttochar(int patternint){
    char res[recupnb()+1];
    sprintf(res,"%i",patternint);
    printf("%s\n",res);
    char* final;
    for (int i=0;i<nb_letters(res);i++){
        final[i]=res[i];
        
    }
    printf("%s\n",final);
    return final;
}

char* wordfinder(list_t *dico,int trynumber){
    listchar_t *ranking=best_letters(dico);
    listint_t *wordscores=create_listint();
    wordscores->head=NULL;
    element_t *current=dico->head;
    
    while (current!=NULL){
        int s=0;
        for (int l=0;l<nb_letters(dico->head->ch1);l++){
            s+=indexlistchar(ranking,current->ch1[l]);

            if (trynumber<2){
                if (occurrences(current->ch1,current->ch1[l])>1){
                    s+=100;
                }
            }
            
        }
        listint_append(wordscores,s);
        
        current=current->next;
    }
    

    int indexofwordtogive=indexofmin(wordscores);
    char* wordtogive=list_get(dico,indexofwordtogive);
    printf("MOT A DONNER %s\n",wordtogive);
    
    listint_destroy(wordscores);
    listchar_destroy(ranking);
    
    return wordtogive;
}



bool in(char lettre,char* mot){
    for (int i=0;i<nb_letters(mot);i++){
        if (mot[i]==lettre){
            return true;
        }
    }
    return false;
}

char* hereorafter(char* mot,int index){
    return mot + index;
}
char* hereorbefore(char* mot,int index){
    char* copy=strdup(mot);
    copy[index]='\0';
    return copy;

}
int indexletter(char* alphabet,char letter){
    for (int i=0;i<26;i++){
        if (alphabet[i]==letter){
            return i;
        }
    }
    return -1;
}
int indexlistint(listint_t *countlist,int val){
    elementint_t *current=countlist->head;
    int i=0;
    while(current!=NULL){
        if (current->value==val){
            return i;
        }
        i++;
        current=current->next;
    }
    return -1;
}
int indexlistchar(listchar_t *charlist,char lettre){
    elementchar_t *current=charlist->head;
    int i=0;
    while(current!=NULL){
        if (current->letter==lettre){
            return i;
        }
        i++;
        current=current->next;
    }
    return -1;
}
elementint_t* findelementint(listint_t *countlist,int index){
    elementint_t *current=countlist->head;
    int i=0;
    while (i!=index){
        current=current->next;
        i++;
    }
    return current;
}
element_t* findelement(list_t *dico,int index){
    element_t *current=dico->head;
    int i=0;
    while (i!=index){
        current=current->next;
        i++;
    }
    return current;
}
void elementint_print(elementint_t* nbr){
    printf("%i ",nbr->value);

}
void printcountlist(listint_t *countlist){
    if (countlist == NULL){
        exit(EXIT_FAILURE);
    }
    elementint_t *actuel = countlist->head;
    
    if (actuel==NULL){
        printf("C'est vide\n");
    }
    else{
        printf("[ ");
        while (actuel != NULL){
            elementint_print(actuel);
            actuel = actuel->next;
        }
        printf("]\n ");
    }
}

void elementchar_print(elementchar_t* lettre){
    printf("%c ",lettre->letter);

}
void printlistchar(listchar_t *listchar){
    if (listchar == NULL){
        exit(EXIT_FAILURE);
    }
    elementchar_t *actuel = listchar->head;
    
    if (actuel==NULL){
        printf("C'est vide\n");
    }
    else{
        printf("[ ");
        while (actuel != NULL){
            elementchar_print(actuel);
            actuel = actuel->next;
        }
        printf("]\n ");
    }
}

void addone(listint_t *countlist,int index){
        elementint_t *toadd=findelementint(countlist,index);
        toadd->value++;
}
int indexofmin(listint_t *wordscores){
    elementint_t *current=wordscores->head;
    int m = current->value;
    int i=0;
    int ind=0;
    while (current->next!=NULL){
        if (current->next->value < m){
            m=current->next->value;
            ind=i+1;
        }
        i++;
        current=current->next;
    }
    return ind;
}
int max(listint_t *countlist){
    elementint_t *current=countlist->head;
    int m = current->value;
    while (current->next!=NULL){
        if (current->next->value > m){
            m=current->next->value;
          
            
        }
        current=current->next;
       

    }
    return m;
}
void removeelementint(listint_t *countlist,int index){
    elementint_t *current=countlist->head;
    elementint_t *prec=current;
    int i=0;
    if (index==0){
        countlist->head=current->next;

        free(current);
    }
    else{
        while (i!=index && current!=NULL){
        prec=current;
        current=current->next;
        
        i++;
        }
        if (i==index){
            if (current->next==NULL){
                prec->next=NULL;
            }
            else{
                prec->next=current->next;
            }
            free(current);
        }
    }
    
}

char* removeletterinalphabet(char* alphabet,int index){
    char* firstpart=hereorbefore(alphabet,index);
    strcat(firstpart,hereorafter(alphabet,index+1));
    return firstpart;
}

listchar_t* best_letters(list_t *dico){
    char* alphabet="abcdefghijklmnopqrstuvwxyz";
    listint_t *alphacount=create_listint();
    elementint_t *first=malloc(sizeof(elementint_t));
    first->value=0;
    alphacount->head=first;
    first->next=NULL;
    int i=1;                                                // (1)
    
    while (i!=26){
        elementint_t *nouveau=malloc(sizeof(elementint_t));
        nouveau->value=0;
        nouveau->next=alphacount->head;
        alphacount->head=nouveau;
        i++;
    }

    //int compteur=0; // (2)
    int ind;
    for (int l=0;l<length(dico);l++){ 
        for (int j=0;j<nb_letters(dico->head->ch1);j++){
            element_t *mot=findelement(dico,l); 
            ind=indexletter(alphabet,(mot->ch1)[j]);
            addone(alphacount,ind);
        }
    }

    listchar_t *bestletters=malloc(sizeof(listchar_t));
    bestletters->head=NULL;
    int m;
    int indletter;
    listchar_t *alphabetlist=create_alphalist();

    for (int k=0;k<26;k++){

        m=max(alphacount);

        indletter=indexlistint(alphacount,m);

        listchar_append(bestletters,listchar_get(alphabetlist,indletter));

        retirechar(indletter,alphabetlist);
        
        removeelementint(alphacount,indletter);
        
    }
    
    listint_destroy(alphacount);
    free(alphabetlist);
    return bestletters;
}

listchar_t* create_alphalist(){
    listchar_t *alphabet=malloc(sizeof(listchar_t));
    char* alpha="abcdefghijklmnopqrstuvwxyz";
    elementchar_t *tete=malloc(sizeof(elementchar_t));
    tete->letter='a';
    alphabet->head=tete;
    elementchar_t *current=alphabet->head;
    for (int i=1;i<nb_letters(alpha);i++){
        elementchar_t *new=malloc(sizeof(elementchar_t));
        new->letter=alpha[i];
        current->next=new;
        current=current->next;
    }
    current->next=NULL;
    return alphabet;


}

char* listchar_get(listchar_t *listchar, int index) {
    int pos = index;
    elementchar_t *current = listchar->head;
    
    while (pos > 0 && current->next != NULL) 
    {
        //printf("%i\n",pos);
        pos--;
        current = current->next;
    }
    return current->letter;
}
void retirechar(int index,listchar_t* listchar){
    if (!isEmpty(listchar)){                    //on vérifie que le dictionnaire n'est pas vide
        elementchar_t* current=listchar->head;      //on initialise notre élément courant à la tête de la liste
        elementchar_t* previous;                //on prévoit de garder en mémoire l'élément précédant courant
        int i=0;
        if (index==0){          //si l'élément à retirer est la tête de liste
            listchar->head=current->next;                           //on donne à la liste pour nouvelle tête le suivant de la tête
             // LAISSE MOI CES LIGNES
            free(current);                                      //on free l'élément
        }

        else{
            while(i!=index && current!=NULL){           //on cherche l'élément dans la liste
                previous=current;           
                current=current->next;                          //on parcourt jusqu'à trouver l'élément
                i++;
            }
            if (current!=NULL && current->next!=NULL){          //si on à trouvé l'élément (cad que current n'est pas vide) et qu'il a un suivant
                elementchar_t* suivant=current->next;               //on enregistre sont suivant
                
                free(current);                                  //on free l'élément
                previous->next=suivant;                         //on reconnecte la liste en donnant pour suivaant au précédent de l'élément son suivant
            }
            else if (current!=NULL && current->next==NULL){     //si on à trouvé l'élément (cad que current n'est pas vide) et qu'il n'a pas de suivant
                previous->next==NULL;
                
                free(current);                                  //on free l'élément
            }
        }    
    }
}



void listchar_append(listchar_t* listchar, char letter){
    elementchar_t *nouveau = malloc(sizeof(*nouveau));
    if (listchar == NULL || nouveau == NULL){
        exit(EXIT_FAILURE);
    }
    nouveau->letter=letter;
    nouveau->next=NULL;

    elementchar_t *current=listchar->head;

    if (current==NULL){
        printf("Ca rentre\n");
        listchar->head=nouveau;
        return;
    }

    while (current->next != NULL){
        current=current->next;
    }
    current->next = nouveau;
}

void listint_append(listint_t* wordscores,int score){
    elementint_t *new=malloc(sizeof(elementint_t));
    new->value=score;
    new->next=NULL;

    elementint_t *current=wordscores->head;
    if (current==NULL){
        wordscores->head=new;
        return;
    }
    while (current->next!=NULL){
        current=current->next;
    }
    current->next=new;
}

void listint_destroy(listint_t *listint)
{
    while (listint->head != NULL)
    {
        elementint_t *aSupprimer = listint->head;
        listint->head = listint->head->next;
        free(aSupprimer);
    }
    free(listint);
}

void listchar_destroy(listchar_t *listchar)
{
    while (listchar->head != NULL)
    {
        elementchar_t *aSupprimer = listchar->head;
        listchar->head = listchar->head->next;
        
        free(aSupprimer);
    }
    free(listchar);
}

char* savedwords(int longueur){
    char* mot;
    if (longueur==4){
        mot="aies";
    }
    else if (longueur==5){
        mot="aires";
    }
    else if (longueur==6){
        mot="aitres";
    }
    else if (longueur==7){
        mot="arisent";
    }
    else if (longueur==8){
        mot="aterions";
    }
    else if (longueur==9){
        mot="alertions";
    }
    else if (longueur==10){
        mot="calorisent";
    }
    else if (longueur==11){
        mot="consulterai";
    }
    else if (longueur==12){
        mot="capitulerons";
    }
    return mot;
}



listint_t* create_listint(){
    listint_t* countlist=malloc(sizeof(listint_t));
    
    return countlist;
}















