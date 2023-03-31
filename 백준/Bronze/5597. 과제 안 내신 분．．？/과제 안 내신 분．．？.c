#include <stdio.h>

int main() 
{
    int stdNum[30], Num;
    for(int i = 0; i < 30; i++)
    	stdNum[i] = 1;
    
    for(int i = 0; i < 28; i++)
    {
    	scanf("%d", &Num);
    	stdNum[Num - 1] = 0;
	  }
    for(int i = 0; i < 30; i++)
    {
    	if(stdNum[i] == 1)
    	printf("%d\n",i + 1);
	  }
    return 0;
}