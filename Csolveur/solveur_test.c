#include "solveur.h"

int main(){
    //assert(recupnb()==5);
    assert(nb_letters("plage")== 5);
    assert(occurrences("plage",'o')==0);
    assert(occurrences("fauteuil",'u')==2);
    assert(in('a',"plage"));
    assert(!in('o',"canape"));
    assert(strcmp(hereorafter("abcdefghijklmnopqrstuvwxyz",5),"fghijklmnopqrstuvwxyz")==0);

    char* test1=hereorbefore("abcdefghijklmnopqrstuvwxyz",5);
    assert(strcmp(test1,"abcde")==0);
    free(test1);

    assert(indexletter("abcdefghijklmnopqrstuvwxyz",'e') == 4);


    char* test2=removeletterinalphabet("abcdefghijklmnopqrstuvwxyz",5);
    printf("%s\n",test2);
    assert(strcmp(test2,"abcdeghijklmnopqrstuvwxyz")==0);
    free(test2);

    list_t* dico = create_dico();
    assert(!isEmpty(dico));
    printf("length : %i\n",length(dico));
    
    /* printf("4ème élement : %s\n",list_get(dico,3));
    assert(strcmp(dico->head->next->ch1,"abats")==0);
    printf("Indice du mot abces : %i\n",list_index_of(dico,"abces")),

    printf("Tête de dico avant suppression : %s\n",dico->head->ch1);
    retire(dico->head,dico);
    printf("Tête de dico après suppression : %s\n",dico->head->ch1);

    printf("3ème élement du dico avant suppression : %s\n",dico->head->next->next->ch1);
    retire(dico->head->next->next,dico);
    printf("3ème élement du dico après suppression : %s\n",dico->head->next->next->ch1); */


    


    //fonctionne seulement avec 5 lettres là

    char* wordtogive=wordfinder(dico,0);    //aires

    printf("début test réduction du dico\n");
    //dico_print(dico);
    dico=reduction_dico(wordtogive,"10010",dico);
    //dico_print(dico_reduit);
    printf("dicoreduit ^^\n");
    printf("--------------------------------------\n");
    wordtogive=wordfinder(dico,1);  //calte
    dico=reduction_dico(wordtogive,"01102",dico);
    printf("--------------------------------------\n");
    wordtogive=wordfinder(dico,2);  //egale
    dico=reduction_dico(wordtogive,"01212",dico);
    printf("--------------------------------------\n");
    wordtogive=wordfinder(dico,3);  //glane
    dico=reduction_dico(wordtogive,"12202",dico);
    printf("--------------------------------------\n");
    


    dico_destroy(dico);
}
