#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int totalByte;
    scanf("%d", &totalByte);
    for (int i = 0; i < totalByte/4; i++)
    {
        printf("long ");
    }
	printf("int");
}