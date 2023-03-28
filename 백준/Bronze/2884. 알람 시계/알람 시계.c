#include <stdio.h>

int main (void)
{
    int H,M,sum;
    scanf("%d %d",&H, &M);
    if (H * 60 + M < 45)
    {
    	M = 60 - (45 - M);
		H = 23;
	}
	else
	{
		sum = H*60+M-45;
		H = sum / 60;
		M = sum - H * 60;
	}
	printf("%d %d",H,M);
    return 0;
}