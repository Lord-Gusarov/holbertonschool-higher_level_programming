#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

void add_node(listint_t **head, int n);
int *dynamic_int_arr(int *arr, int c_size, int n_size);

/*tryinf recursively*/
int is_palindrome_helper(listint_t *h, listint_t *p_last, listint_t *forward);
#endif /* LISTS_H */

