#ifndef __MODULE_B_H //很明显这一部分也是为了防止重复引用

#define __MODULE_B_H

#ifdef __cplusplus //而这一部分就是告诉编译器，如果定义了__cplusplus(即如果是cpp文件，
extern "C"{ //因为cpp文件默认定义了该宏),则采用C语言方式进行编译

#include"moduleA.h"

#endif

 //其他代码

#ifdef __cplusplus

}

#endif

#endif