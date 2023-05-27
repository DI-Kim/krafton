#include <stdio.h>

int main() {
    int x = 1;
    printf("%lu\n", sizeof(x));
    printf("%lu\n", sizeof((char *)x));
    printf("%lu\n", sizeof((int *)x));
    printf("%i\n", x);
    printf("%d\n", *(char *)x);
    printf("%d\n", *(int *)x);
    // print("%c", *x);
}