#include <stdio.h>
#include <string.h>

int main(void) {
  int N, M, begin, mid, end, save, cmp1, cmp2;

  scanf("%d %d", &N, &M);
  int basketNum[101];

  for (int i = 0; i < N; i++)
    basketNum[i] = i + 1;

  for (int i = 0; i < M; i++) {
    scanf("%d %d %d", &begin, &end, &mid);
    cmp1 = basketNum[mid - 1];
    for (int j; basketNum[begin - 1] != cmp1; j++) {
      cmp2 = basketNum[end - 1];
      for (int k = begin; basketNum[begin - 1] != cmp2; k++) {
        save = basketNum[begin - 1];
        basketNum[begin - 1] = basketNum[k];
        basketNum[k] = save;
      }
    }
  }

  for (int i = 0; i < N; i++)
    printf("%d ", basketNum[i]);
}