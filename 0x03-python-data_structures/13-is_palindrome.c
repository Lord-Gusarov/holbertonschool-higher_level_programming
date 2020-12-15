#include "lists.h"
#define IS_PALINDROME 1
#define NOT_PALINDROME -1

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: adress of the pointer to the head of the list
 *
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int cnt = 0, r_limit = 150, i;
	listint_t *trv;
	int *rev;

	if (!head)
		return (NOT_PALINDROME);
	if (!*head)
		return (IS_PALINDROME);
	rev = dynamic_int_arr(NULL, 0, r_limit);
	trv = *head;
	while (trv)
	{
		rev[cnt++] = trv->n;
		trv = trv->next;
		if (cnt == r_limit)
		{
			rev = dynamic_int_arr(rev, r_limit, r_limit * 2);
			r_limit *= 2;
		}
	}

	for (i = cnt - 1, trv = *head; i >= 0; i--, trv = trv->next)
	{
		if (trv->n != rev[i])
		{
			free(rev);
			return (NOT_PALINDROME);
		}
	}

	free(rev);
	return (IS_PALINDROME);
}


/**
 * dynamic_int_arr - creates or expands a dynamic int array
 * @arr: set to NULL for fully newly array, otherwise these values are copied
 * into the new one dynamic array
 * @c_size: size of the current array
 * @n_size: how many elements the new array should be able to hold
 * Return: dynamic array of @n_size
 */

int *dynamic_int_arr(int *arr, int c_size, int n_size)
{
	int *new = malloc(sizeof(int) * n_size), i;

	if (arr == NULL)
		return (new);
	for (i = 0; i < c_size; i++)
		new[i] = arr[i];

	free(arr);
	return (new);
}
