#include <stdio.h>

int main() 
{
	int count, smallest =  2147483647, largest = -2147483648;
	scanf("%d", &count);
	int Num[count];
	for (int i = 0; i < count; i++)
    {
	    scanf("%d", &Num[i]);
    }
	for (int i = 0; i < count; i++)
    {
    	if(Num[i] < smallest)
    	smallest = Num[i];
    }
	for (int i = 0; i < count; i++)
    {
    	if(Num[i] > largest)
    	largest = Num[i];
    }
    printf("%d %d",smallest ,largest);
	return 0;
}