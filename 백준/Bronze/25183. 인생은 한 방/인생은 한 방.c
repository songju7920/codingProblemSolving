#include <stdio.h>
#include <string.h>

int main() {
  int n;
  int cnt = 1;
  scanf("%d", &n);
  
  char lottory[n + 1];
  scanf("%s", lottory);

  for (int i = 0; i < n - 1; i++) {
    if (lottory[i] + 1 == lottory[i+1]) {
      cnt++;
    } else if (lottory[i] - 1 == lottory[i+1]) {
      cnt++;
    } else {
      cnt = 1;
    }

    //5개 연속시 종료
    if (cnt == 5) {
      break;
    }
  }

  if (cnt >= 5) {
    printf("YES");
  } else {
    printf("NO");
  }
}