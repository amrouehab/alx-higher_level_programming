#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *hash_table[1024];
	size_t i;

	if (list == NULL)
		return (0);

	/* Initialize the hash table */
	for (i = 0; i < 1024; i++)
		hash_table[i] = NULL;

	/* Traverse the list */
	while (list != NULL)
	{
		/* Compute the hash index */
		i = ((size_t)list) % 1024;

		/* Check if the current node is already in the hash table */
		if (hash_table[i] == list)
			return (1); /* Cycle detected */

		/* Store the current node in the hash table */
		hash_table[i] = list;

		/* Move to the next node */
		list = list->next;
	}

	return (0); /* No cycle detected */
}

