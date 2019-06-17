/*
* @Author: lcl1026504480
* @Date:   2019-06-16 21:28:39
* @Last Modified by:   lcl1026504480
* @Last Modified time: 2019-06-16 21:33:07
*/
#include "Python.h"
PyObject*  op_minus(PyObject *self, PyObject *args)
{
int a,b;
if(!PyArg_ParseTuple(args, "ii",&a,&b))  return NULL;
    return PyLong_FromLong(a-b);
//如果是正常下返回void, 使用下面代码（注：C函数应“拥有”对象的引用，然后传递给python调用者）
//Py_INCREF(Py_None);
//return Py_None;
}
PyMethodDef cmethods[] =
{
    {"minus", op_minus, METH_VARARGS, "Return the difference of the integers."},
    {NULL, NULL, 0, NULL}   // Sentinel
};

 PyModuleDef cmodule=
 {
PyModuleDef_HEAD_INIT,
" cmodule ",    // name of module

NULL,  // module documentation, may be NULL
-1, // size of per-interpreter state of the module, or -1 if the module keeps state in global variables.
 cmethods,
  };
#ifdef __cplusplus
extern "C"
#endif
PyObject* PyInit_cmodule(void)
{
    return PyModule_Create(&cmodule);
}