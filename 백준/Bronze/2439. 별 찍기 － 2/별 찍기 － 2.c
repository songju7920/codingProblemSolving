#include <stdio.h>

int main() 
{
	int count;
	scanf("%d", &count);
	for (int i = 1; i <= count; i++)
    {
    	for(int j = count; j > i; j--)
        {
            printf(" ");
        }
        for(int j = 0; j < i; j++)
        {
            printf("*");
        }
        printf("\n");
    }
	return 0;
}