#include <stdio.h>

int main (void)
{
    int a,b,c,money;
    scanf("%d %d %d",&a, &b, &c);
    if(a==b && b==c)
        money = 10000+a*1000;
    else if(a == b || a == c || c == b)
        money = a==b? 1000+a*100 : a==c? 1000+a*100 : 1000+b*100;
    else
        money = a>b? a>c? a*100 : c*100 : b>c? b*100 : c*100;
	printf("%d",money);
    return 0;
}