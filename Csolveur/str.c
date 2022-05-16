#include <string.h>
#include <stdio.h>

int main(void) {
    char tab[5] = "tutu";

    char *p = strdup(tab);

    printf("%s\n", p);
}