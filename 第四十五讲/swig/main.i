%module main
%inline %{
#include "main.h"
%}
int compute(int a,int b);