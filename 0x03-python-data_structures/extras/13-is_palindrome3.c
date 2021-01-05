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
	listint_t *trv, *rev = NULL;

	if (!head)
		return (NOT_PALINDROME);
	if (!*head)
		return (IS_PALINDROME);

	trv = *head;
	while (trv)
	{
		add_node(&rev, trv->n);
		trv = trv->next;
	}

	trv = *head;
	while (trv)
	{
		if (trv->n != rev->n)
		{
			free_listint(rev);
			return (NOT_PALINDROME);
		}
		trv = trv->next;
		rev = rev->next;
	}

	free_listint(rev);
	return (IS_PALINDROME);
}


/**
 * add_node - adds a new node at the beggining of a list_t list
 * @head: adress current head of the list, will be updated if new node
 * is succesfully added at the beginning of a list
 * @n: value for the new node
 */
void add_node(listint_t **head, int n)
{
	listint_t *new = malloc(sizeof(listint_t));

	new->n = n;
	new->next = *head;
	*head = new;
}
