#include "lists.h"
#define IS_PALINDROME 1
#define NOT_PALINDROME 0

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: adress of the pointer to the head of the list
 *
 * Return: 1 if a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{

	if (!head)
		return (NOT_PALINDROME);
	if (!*head)
		return (IS_PALINDROME);

	return (is_palindrome_helper(*head, *head, (*head)->next));
}


int is_palindrome_helper(listint_t *h, listint_t *p_last, listint_t *forward)
{
	int result;

	if (!h)
		return (IS_PALINDROME);

	if (!forward)
		return (h->n == p_last->n);


	result = (is_palindrome_helper(h, forward, forward->next));
	


	return (is_palindrome_helper(h->next, p_last, forward) && result);
}

