#include <math.h>
#include <stdio.h>

int main() {
  int x, y, w, h;
  scanf("%d %d %d %d", &x, &y, &w, &h);
  int cmp1 = w - x < h - y ? w - x : h - y;
  int cmp2 = x < y ? x : y;
  printf("%d", cmp1 < cmp2 ? cmp1 : cmp2);
}