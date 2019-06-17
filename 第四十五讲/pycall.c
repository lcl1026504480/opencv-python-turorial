/*
* @Author: lenovouser
* @Date:   2019-06-14 21:25:59
* @Last Modified by:   lenovouser
* @Last Modified time: 2019-06-14 21:26:12
*/
/***gcc -o libpycall.so -shared -fPIC pycall.c*/
#include <stdio.h>
#include <stdlib.h>
int foo(int a, int b)
{
  printf("you input %d and %d\n", a, b);
  return a+b;
}