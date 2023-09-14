#include <stdio.h>
#include <string.h>
int arr[1000];

void sort(int *arr, int N) {
  for (int i = 0; i < N - 1; i++) {
    int min = i;
    for (int j = i + 1; j < N; j++) {
      if (arr[min] > arr[j])
        min = j;
    }
    int temp = arr[min];
    arr[min] = arr[i];
    arr[i] = temp;
  }
}

int main(void) {
  int N, L;
  int answer = 0;
  scanf("%d %d", &N, &L);
  for (int i = 0; i < N; i++) {
    scanf(" %d", &arr[i]);
  }

  sort(arr, N);

  for (int i = 0; i < N; i++) {
    int cnt = 0;

    for (int j = i + 1; j < N; j++) {
      if (arr[j] - arr[i] + 1 <= L) {
        cnt++;
        continue;
      } else {
        break;
      }
    }

    answer++;
    i += cnt;
  }

  printf("%d", answer);
}