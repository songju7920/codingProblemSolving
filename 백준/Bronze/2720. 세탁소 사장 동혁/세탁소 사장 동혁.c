#include <stdio.h>

int main(void) {
  int repeat, money;
  scanf("%d", &repeat);
  for (int i = 0; i < repeat; i++) {
    int Quarter = 0, Dime = 0, Nickel = 0, Penny = 0;
    scanf("%d", &money);
    if (money >= 25) {
      Quarter = money / 25;
      money -= Quarter * 25;
    }
    if (money >= 10) {
      Dime = money / 10;
      money -= Dime * 10;
    }
    if (money >= 5) {
      Nickel = money / 5;
      money -= Nickel * 5;
    }
    if (money != 0)
      Penny = money;
    printf("%d %d %d %d\n", Quarter, Dime, Nickel, Penny);
  }
}