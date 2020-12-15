#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - prints some simple info about a Python lists
 * @list: pointer to a Pyhton object
 */
void print_python_list_info(PyObject *list)
{
	int size;
	int i;
	PyObject *list2;

	size = PyList_Size(list);
	printf("[*] Size of the Python List = %d\n", sizeobj);
	printf("[*] Allocated = %ld\n", ((PyListObject *)list)->allocated);

	for (i = 0; i < size; i++)
	{
		list2 = PyList_GetItem(list, i);
		printf("Element %d: %s\n", i, Py_TYPE(list2)->tp_name);
	}
}
