#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *visited_nodes[1024];  /* Array to store pointers */
	int i;

	/* Initialize all pointers to NULL */
	for (i = 0; i < 1024; i++)
		visited_nodes[i] = NULL;

	current = list;
	i = 0;
	while (current != NULL)
	{
		/* Check if current node is already in visited_nodes */
		for (int j = 0; j < 1024; j++)
		{
			if (visited_nodes[j] == current)
				return (1);
		}
		
		/* Add current node to visited_nodes */
		visited_nodes[i % 1024] = current;
		i++;

		current = current->next;
	}

	return (0);
}

