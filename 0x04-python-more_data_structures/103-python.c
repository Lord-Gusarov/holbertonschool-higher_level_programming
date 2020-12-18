#include <strings.h>
#include <Python.h>
#include <stdio.h>


/**
 * print_python_list - prints some basic info about Python lists
 * @obj: Pointer to a python Object
**/
void print_python_list(PyObject *obj)
{
	int size, i;
	PyObject *obj2;

	printf("[*] Python list info\n");
	size = (((PyVarObject *)(obj))->ob_size);
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)obj)->allocated);
	for (i = 0; i < size; i++)
	{
		obj2 = (((PyListObject *)(obj))->ob_item[i]);
		printf("Element %d: %s\n", i, ((obj2)->ob_type)->tp_name);
		if (strcmp(((obj2)->ob_type)->tp_name, "bytes") == 0)
		{
			print_python_bytes(obj2);
		}
	}
}


/**
 *  print_python_bytes - prints info about Python bytes
 * @obj: pointer to a object
**/
void print_python_bytes(PyObject *obj)
{
	int size;
	int i = 0;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(obj))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size =  (int)(assert(PyBytes_Check(obj)), (((PyVarObject *)(obj))->ob_size));
	printf("  size: %d\n", size);
	str =  PyBytes_AsString(obj);
	printf("  trying string: %s\n", str);

	if (size > 9)
		size = 9;
	printf("  first %d bytes:", size + 1);

	while (i <= size)
	{
		printf(" %02x", (unsigned int) *str++ & 0xFF);
		i++;
	}
	printf("\n");
}
