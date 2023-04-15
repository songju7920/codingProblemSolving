#include <stdio.h>

int main(void) {
  int N, M;
  scanf("%d %d",&N ,&M);
  int Num1[N][M], Num2[N][M];
  
  for(int i = 0; i < N; i++)
    for(int j = 0; j < M; j++)
      scanf("%d",&Num1[i][j]);
  
  for(int i = 0; i < N; i++)
    for(int j = 0; j < M; j++)
      scanf("%d",&Num2[i][j]);
  
  for(int i = 0; i < N; i++) {
      for(int j = 0; j < M; j++)
        printf("%d ",Num1[i][j] + Num2[i][j]);
      printf("\n");
    }
}