#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n:that is for integers
 * @next:this points to the next node
 *
 * Description:A single linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

int is_palindrome(listint_t **head);
size_t listint_len(const listint_t *h);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index);

#endif
