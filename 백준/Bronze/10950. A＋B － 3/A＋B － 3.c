#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main (void)
{
    int length;
    scanf("%d",&length);
    int A[length],B[length];
    for(int i = 0; i < length; i++)
    {
        scanf("%d %d",&A[i],&B[i]);
    }
    for(int i = 0; i < length; i++)
    {
        printf("%d\n",A[i]+B[i]);
    }
}