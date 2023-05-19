#include <stdio.h>
// 이해하기
int main() {
    // void** ptr = 30; // 예시로 든 값 입니다.
    // char* name = (char*) *ptr;
    // printf("%s", name);
    // void** ptr2 = 40; // 마찬가지
    // int64_t* number = (int64_t*) *ptr2;
    // printf("%llx", *number);
	int num = 10;
	int *ptr;
	int **pptr;

	ptr = &num;
	pptr = &ptr;

	printf("num : %d, *ptr : %d, **ptr : %d\n", num, *ptr, **pptr);
	printf("num 주소 : %d, ptr 값 : %d, **ptr 값 : %d\n", &num, ptr, *pptr);
	printf("ptr 주소 : %d, pptr 값 : %d", &ptr, pptr);

	return 0;
}
