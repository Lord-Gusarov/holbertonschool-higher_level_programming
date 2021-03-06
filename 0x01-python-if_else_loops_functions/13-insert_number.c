#include "lists.h"

/**
 * insert_node - Inserts a new node in a sorted listint_t list
 * @head: pointer to pointer of current head of the list
 * @number: value for the new node
 *
 * Return: pointer to new node or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *node = NULL;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	if (*head == NULL || (*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	node = *head;
	while (node->next && node->next->n < number)
		node = node->next;
	new->next = node->next;
	node->next = new;

	return (new);
}
