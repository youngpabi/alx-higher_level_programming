#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
  * is_palindrome -this Checks if a singly linked list is a palindrome
  * @head: this is the head of the singly linked list
  *
  * Return: 0 if not a palindrome, 1 if it is a palindrome
  */
int is_palindrome(listint_t **head)
{
    listint_t *start = NULL, *end = NULL;
    unsigned int b = 0, lent = 0, lent_cyc = 0, lent_list = 0;

    if (head == NULL)
        return (0);

    if (*head == NULL)
        return (1);
    
    start = *head;
    lent = listint_len(start);
    lent_cyc = lent * 2;
    lent_list = lent_cyc - 2;
    end = *head;

    for (; b < lent_cyc; b = b + 2)
    {
        if (start[b].n != end[lent_list].n)
            return (0);

        lent_list = lent_list - 2;
    }

    return (1);
}

/**
  * get_nodeint_at_index - Gets a node from a linked list
  * @head: The head of the linked list
  * @index: The index to find in the linked list
  *
  * Return: The specific node of the linked list
  */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int inter_time = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (inter_time == index)
				return (current);

			current = current->next;
			++inter_time;
		}
	}

	return (NULL);
}

/**
  * slistint_len -this Counts the number of elements in a linked list
  * @h: linked list to count
  * Return: Numb of elements off the linked list
  */
size_t listint_len(const listint_t *h)
{
	int lenght = 0;

	while (h != NULL)
	{
		++lenght;
		h = h->next;
	}

	return (lenght);
}
