#include "lists.h"
#define IS_PALINDROME 1
#define NOT_PALINDROME -1
#define ARR_SIZE 10000

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: adress of the pointer to the head of the list
 *
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int cnt = 0, i;
	listint_t *trv;
	int rev[ARR_SIZE];

	if (!head)
		return (NOT_PALINDROME);
	if (!*head)
		return (IS_PALINDROME);
	while (trv)
	{
		rev[cnt++] = trv->n;
		trv = trv->next;
	}

	for (i = cnt - 1, trv = *head; i >= 0; i--, trv = trv->next)
	{
		if (trv->n != rev[i])
		{
			return (NOT_PALINDROME);
		}
	}

	return (IS_PALINDROME);
}

