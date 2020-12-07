#include "lists.h"
/**
 * check_cycle - checks if a linkint_t list has a loop
 * @list: head of the list of the node from which to start
 *
 * Return: 0 if there is no loop, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *tortuga = list, *liebre = list;

	if (!list)
		return (0);

	while (liebre && liebre->next)
	{
		tortuga = tortuga->next;
		liebre = (liebre->next)->next;
		if (tortuga == liebre)
			return (1);
	}
	return (0);
}
