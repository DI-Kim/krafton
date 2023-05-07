#include <stdio.h>

struct student {
    char name[15];
    int student_id;
    int age;
    char phone_number[14];
};

int main() {
    // struct student jungle;
    // initailize
    struct student jungle = {.age = 33, .name = "bigPerson"};

    scanf("%s", jungle.name);
    scanf("%d", &jungle.student_id);
    scanf("%d", &jungle.age);
    scanf("%s", jungle.phone_number);

    printf("name: %s, ID: %d, age: %d, phone number: %s", jungle.name, jungle.student_id, jungle.age, jungle.phone_number);
    return 0;
}