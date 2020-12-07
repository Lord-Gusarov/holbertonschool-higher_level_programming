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

	while(liebre && liebre->next)
	{
		if (tortuga == liebre)
			return (1);
		tortuga = tortuga->next;
		liebre = (liebre->next)->next;
	}
		return (0);
}
