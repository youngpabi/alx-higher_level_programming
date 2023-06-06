#include "lists.h"

/**
 * check_cycle -This checks if a singly linked list has a cycle in it.
 * @list:this pointer to the list
 * Return: 0 if is no loop and 1 thenthere is one.
 */
int check_cycle(listint_t *list)
{
	listint_t *head;
	listint_t *tmp;

	head = list;
	tmp = list;

	while(tmp != NULL && head->next != NULL && head->next->next != NULL)
	{
		head = head->next->next;
		tmp = tmp->next;

		if (head == tmp)
			return (1);
	}
	return (0);
}
