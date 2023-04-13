#include <stdio.h>

int main(void) {
  int C, N;
  scanf("%d", &C);

  for (int i = 0; i < C; i++) {
    scanf("%d", &N);
    int score[1000], cnt = 0, sum = 0;
    double avg = 0.00;
    for (int j = 0; j < N; j++) {
      scanf("%d", &score[j]);
      sum += score[j];
    }
    avg = (double)sum / N;
    for (int j = 0; j < N; j++)
      if (avg < score[j])
        cnt++; 
    printf("%.3lf%%\n", (double)cnt * 100 / N);
  }
}