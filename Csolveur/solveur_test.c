#include "solveur.h"

int main(){
    assert(nb_letters("plage")== 5);
    assert(nb_letters("")==0);

    assert(occurrences("plage",'o')==0);
    assert(occurrences("monter",'o')==1);
    assert(occurrences("fauteuil",'u')==2);

    assert(in('a',"plage"));
    assert(!in('o',"canape"));

    assert(strcmp(hereorafter("abcdefghijklmnopqrstuvwxyz",5),"fghijklmnopqrstuvwxyz")==0);
    assert(strcmp(hereorafter("bonjour",0),"bonjour")==0);
    assert(strcmp(hereorafter("plus",4),"")==0);

    char* test1=hereorbefore("abcdefghijklmnopqrstuvwxyz",5);
    assert(strcmp(test1,"abcde")==0);
    free(test1);
    char* test2=hereorbefore("bonjour",7);
    assert(strcmp(test2,"bonjour")==0);
    free(test2);
    char* test3=hereorbefore("bonjour",0);
    assert(strcmp(test3,"")==0);
    free(test3);

    assert(indexletter("abcdefghijklmnopqrstuvwxyz",'e') == 4);

    char* test4=removeletterinalphabet("abcdefghijklmnopqrstuvwxyz",5);
    printf("%s\n",test4);
    assert(strcmp(test4,"abcdeghijklmnopqrstuvwxyz")==0);
    free(test4);

    // pour la suite recupnb() = 5

    list_t* dico = create_dico();
    assert(!isEmpty(dico));
    printf("length : %i\n",length(dico)); // on a length : 7087

    assert(length(dico)==7087);

    //char* mot = "test";
    //ajout_dico(mot,dico);
    //printf("length : %i\n",length(dico)); // on a bien length : 7088

    printf("4ème élement : %s\n",list_get(dico,3));
    assert(strcmp(dico->head->next->ch1,"abats")==0);
    printf("Indice du mot abces : %i\n",list_index_of(dico,"abces"));

    printf("Tête de dico avant suppression : %s\n",dico->head->ch1);
    retire(dico->head,dico);
    printf("Tête de dico après suppression : %s\n",dico->head->ch1);

    printf("3ème élement du dico avant suppression : %s\n",dico->head->next->next->ch1);
    retire(dico->head->next->next,dico);
    printf("3ème élement du dico après suppression : %s\n",dico->head->next->next->ch1); 


    


    dico_destroy(dico);
}
