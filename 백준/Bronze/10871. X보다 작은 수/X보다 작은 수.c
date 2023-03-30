#include <stdio.h>

int main() 
{
	int count, find;
	scanf("%d %d", &count, &find);
	int Num[count];
	for (int i = 0; i < count; i++)
    {
	    scanf("%d", &Num[i]);
    }
	for (int i = 0; i < count; i++)
    {
    	if(Num[i] < find)
            printf("%d ",Num[i]);
    }
	return 0;
}