#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if list is circular or not
 * @list: list to check
 * Return: 1 if it is circular or 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *head, *tail;

	if (list == NULL)
		return (0);

	head = list;
	tail = list;

	while (tail != NULL && tail->next != NULL)
	{
		head = head->next;
		tail = tail->next->next;

		if (head == tail)
			return (1);

	}
	return (0);
}
