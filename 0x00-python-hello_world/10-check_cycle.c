#include "lists.h"
/**
 * check_cycle - checks if a linkint_t list has a loop
 * @list: head of the list of the node from which to start
 *
 * Return: 0 if there is no loop, 1 otherwise
 */
int check_cycle(listint_t *list)
{
	size_t i = 0, size = 0;
	unsigned int adrs_size = 100, m_size = sizeof(void *) * adrs_size;
	listint_t **adrs = malloc(m_size);

	if (list == NULL || adrs == NULL)
		exit(98);

	while (list)
	{
		for (i = 0; i < size; i++)
			if (adrs[i] == list)
			{
				free(adrs);
				return (1);
			}
		if (size == adrs_size)
		{
			adrs = _realloc(adrs, m_size, m_size * 2);
			if (!adrs)
				exit(98);
			adrs_size *= 2, m_size *= 2;
		}
		adrs[size] = list;
		size++;
		list = list->next;
	}

	free(adrs);
	return (0);
}

/**
 * _realloc - reallocates a memory block using malloc and free
 * @ptr: memory block to reallocate
 * @old_size: size in bytes of current memory block
 * @new_size: size in bytes of new memory block
 *
 * Return: pointer to new memory block, NULL if it fails
 */
void *_realloc(void *ptr, unsigned int old_size, unsigned int new_size)
{
	char *m, *c_ptr;
	unsigned int limit;

	if (ptr == NULL)
		return (malloc(new_size));

	if (new_size == 0)
	{
		if (ptr != NULL)
			free(ptr);
		return (NULL);
	}
	if (new_size == old_size)
		return (ptr);

	m = malloc(new_size);
	if (m == NULL)
		return (NULL);
	limit = old_size;
	if (new_size < old_size)
		limit = new_size;

	c_ptr = ptr;
	while (limit--)
		m[limit] = c_ptr[limit];

	free(ptr);
	return (m);
}

