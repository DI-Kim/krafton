#include <stdio.h>

int main() {
    char x = '1';
    printf("%lu\n", sizeof(x));
    printf("%lu\n", sizeof((char *)x));
    printf("%lu\n", sizeof((int *)x));
    printf("%c\n", x);
    printf("%d\n", (char *)x);  // 처음 실행시 segmentation fault occurred
    printf("%d\n", (int *)x);
    // print("%c", *x);
}