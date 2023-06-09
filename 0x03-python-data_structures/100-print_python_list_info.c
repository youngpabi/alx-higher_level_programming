#include "/usr/include/python3.4/Python.h"
#include "/usr/include/python3.4/listobject.h"
#include "/usr/include/python3.4/object.h"
#include <stdio.h>

void print_python_list_info(PyObject *p)
{
    int n = 0, list_len  = 0;
    PyObject *item;
    PyListObject *clone = (PyListObject *) p;

    list_len = Py_SIZE(p);
    printf("[*] Size of the Python List = %d\n", list_len);
    printf("[*] Allocated = %d\n", (int) clone->allocated);

    for (; n < list_len; ++n)
    {
        item = PyList_GET_ITEM(p, n);
        printf("Element %d: %s\n", n, item->ob_type->tp_name);
    }

    return;
}
