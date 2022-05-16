#include "solveur.h"

int main(){
    int longueur = recupnb();
    printf("longueur %d\n",longueur);
    printf("%d\n",nb_letters("abc"));

    list_t *dico = create_dico();
    dico_print(dico);
    printf("testage %s\n",dico->head->next->ch1);
    dico_destroy(dico);


}
