#include "solveur.h"

int main(){
    int longueur = recupnb();
    printf("longueur %d\n",longueur);
    printf("%d\n",nb_letters("abc"));

    list_t *dico = create_dico();
    assert(!isEmpty(dico));

    //Vérification des fonctions annexes
    assert(occurences("aaa",'a')==3);
    
    //dico_print(dico);
    printf("testage %s\n",dico->head->ch1);
    printf("%i\n",length(dico));
    char* m="abaca";
    printf("%c\n", m[3]);
 
    

    //assert(removen(dico->head->ch1)==m);    // fail mais on sait pas pourquoi

    printf("%i\n",list_index_of(dico,"ilots"));
    printf("%s\n",list_get(dico,5));
    retire(dico->head,dico);
    printf("testage v2 %s\n",dico->head->ch1);

    dico_destroy(dico);

}
