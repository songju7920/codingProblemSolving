#include <stdio.h>

int main() {
  int n;
  scanf("%d", &n);
  int arr[n];

  for (int i = 0; i < n; i++)
    scanf("%d", &arr[i]);

  for (int i = 0; i < n-1; i++)
    for (int j = 0; j < n-1; j++) {
      if (arr[j] > arr[j+1]) {
        int save = arr[j+1];
        arr[j+1] = arr[j];
        arr[j] = save;
      }
    }

  for (int i = 0; i < n; i++)
    printf("%d\n", arr[i]);
}