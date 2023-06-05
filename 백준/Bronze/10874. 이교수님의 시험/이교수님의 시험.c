#include <stdio.h>

int main() {
  int n, answer, idx = 0;
  scanf("%d", &n);
  int reTest[100] = {0};

  for (int i = 0; i < n; i++) {
    int Cnt = 0;
    for (int j = 1; j <= 10; j++) {
      scanf(" %d", &answer);
      if ((j - 1) % 5 + 1 != answer)
        Cnt++;
    }
    
    if (Cnt == 0) {
      reTest[idx] = i + 1;
      idx++;
    }
  }

  for(int i = 0; reTest[i] != 0; i++) 
    printf("%d\n", reTest[i]);
}