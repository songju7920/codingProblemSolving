#include <stdio.h>

int main() 
{
	int Num[9], location, largest = -2147483648;
	for (int i = 0; i < 9; i++)
    {
	    scanf("%d", &Num[i]);
    }
	for (int i = 0; i < 9; i++)
    {
    	if(Num[i] > largest)
    	{
    	    largest = Num[i];
    	    location = i + 1;	
		}
    }
    printf("%d\n%d",largest ,location);
	return 0;
}