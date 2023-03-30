#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int totalCnt, totalPrice, sum = 0;
    scanf("%d", &totalPrice);
    scanf("%d", &totalCnt);
    int price[totalCnt], cnt[totalCnt];
    for (int i = 0; i < totalCnt; i++)
    {
        scanf("%d %d", &price[i], &cnt[i]);
        sum += price[i] * cnt[i];
    }
    if (sum == totalPrice) printf("Yes");
    else printf("No");
}