#include <stdio.h>

int main() 
{
	int count, sum, find;
	scanf("%d", &count);
	int length[count];
	for (int i = 0; i < count; i++)
    {
	    scanf("%d", &length[i]);
    }
    scanf("%d", &find);
	for (int i = 0; i < count; i++)
    {
    	if(length[i] == find)
    	    sum++;
    }
    printf("%d",sum);
	return 0;
}