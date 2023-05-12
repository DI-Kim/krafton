#include <stdio.h>
// 이해하기
int main() {
    void** ptr = 30; // 예시로 든 값 입니다.
    char* name = (char*) *ptr;
    printf("%s", name);
    void** ptr2 = 40; // 마찬가지
    int64_t* number = (int64_t*) *ptr2;
    printf("%llx", *number);
}
