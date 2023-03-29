#include <stdio.h>

int main (void)
{
    int H,M,addingM,sum;
    scanf("%d %d",&H, &M);
    scanf("%d",&addingM);
    H += (M + addingM) / 60;
    M = addingM + M >= 60 ? (addingM + M) % 60 : addingM + M;
    H = H >= 24 ? H - 24 : H;
	printf("%d %d",H,M);
    return 0;
}