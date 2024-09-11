#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Double pointer to the head of the list
 * @number: Number to insert in the list
 *
 * Return: Address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *current, *previous;

	new_node = malloc(sizeof(listint_t));
	if (!new_node)
		return (NULL);

	new_node->n = number;
	previous = NULL;
	current = *head;

	/* Handle the case when the list is empty or insert at head */
	if (!current || current->n >= number)
	{
		new_node->next = current;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list to find the correct insertion point */
	while (current && current->n < number)
	{
		previous = current;
		current = current->next;
	}

	previous->next = new_node;
	new_node->next = current;

	return (new_node);
}
