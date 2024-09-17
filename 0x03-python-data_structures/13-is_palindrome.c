#include "lists.h"
#include <stddef.h>
#include <stdio.h>

/**
 * reverse_listint - reverses a singly linked list
 * @head: double pointer to the head of the list
 * Return: pointer to the first node of the reversed list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *prev = NULL, *next = NULL, *current = *head;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	*head = prev;
	return (*head);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the list
 * Return: 1 if it is a palindrome, 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *second_half, *prev_slow = *head;
	listint_t *midnode = NULL;  /* To handle odd size case */
	int result = 1;

	if (*head == NULL || (*head)->next == NULL)
		return (1);  /* Empty list or single node list is a palindrome */

	/* Use fast and slow pointers to find the middle */
	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;
		prev_slow = slow;
		slow = slow->next;
	}

	/* Handle odd-sized lists */
	if (fast != NULL)
	{
		midnode = slow;
		slow = slow->next;
	}

	second_half = slow;
	prev_slow->next = NULL;  /* Terminate first half */
	reverse_listint(&second_half);  /* Reverse second half */
	
	/* Compare first half with reversed second half */
	result = compare_lists(*head, second_half);

	/* Restore the list */
	reverse_listint(&second_half);  /* Reverse again to restore */
	if (midnode != NULL)  /* If there was a mid node */
	{
		prev_slow->next = midnode;
		midnode->next = second_half;
	}
	else
	{
		prev_slow->next = second_half;
	}

	return (result);
}

/**
 * compare_lists - compares two linked lists
 * @head1: pointer to the head of the first list
 * @head2: pointer to the head of the second list
 * Return: 1 if the lists are identical, 0 otherwise
 */
int compare_lists(listint_t *head1, listint_t *head2)
{
	while (head1 && head2)
	{
		if (head1->n != head2->n)
			return (0);
		head1 = head1->next;
		head2 = head2->next;
	}

	return (head1 == NULL && head2 == NULL);
}
