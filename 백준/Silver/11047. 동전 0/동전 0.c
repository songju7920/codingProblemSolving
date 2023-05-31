#include <stdio.h>
#include <string.h>

int main(void) {
  int k, money, coinCnt = 0, sum = 0;
  
  scanf("%d %d", &k, &money);
  int coins[k];
  
  for(int i = 0; i < k; i++)
    scanf("%d", &coins[i]);
  
  int length = sizeof(coins) / sizeof(int) - 1;
  
  for(int i = 0; sum < money; i++){
    coinCnt += money / coins[length-i];
    money -= money / coins[length-i] * coins[length-i];
    sum += money / coins[length-i] * coins[length-i];
  }
  
  printf("%d", coinCnt);
  return 0;
}