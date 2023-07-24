#include <stdio.h>

int main() {
  int a, b, sum, difference;

  printf("请输入两个整数：");
  scanf("%d %d", &a, &b);

  sum = a + b;
  difference = a - b;

  printf("a + b = %d\n", sum);
  printf("a - b = %d\n", difference);

  return 0;
}
