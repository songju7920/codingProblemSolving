#include <stdio.h>

int main (void)
{
  int N, M, start, end, save;
  scanf("%d %d", &N, &M);
  int BascketNum[N];
  for(int i = 0; i < N; i++)
    BascketNum[i] = i + 1;
  for(int i = 0; i < M; i++)
    {
      scanf("%d %d", &start, &end);
      for (; start < end; start++)
        {
          save = BascketNum[start - 1];
          BascketNum[start - 1] = BascketNum[end - 1];
          BascketNum[end - 1] = save;
          end--;
        }
    }
  for (int z = 0; z < N; z++)
    {
      printf("%d ",BascketNum[z]);
    }
}