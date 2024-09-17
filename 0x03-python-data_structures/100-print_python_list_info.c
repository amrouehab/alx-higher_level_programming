#include <Python.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PyObject list.
 *
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, allocated, i;
	PyObject *item;

	size = PyList_Size(p); /* Get the size of the list */
	allocated = ((PyListObject *)p)->allocated; /* Get the allocated space */

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
