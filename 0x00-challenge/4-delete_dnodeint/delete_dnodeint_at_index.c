#include "lists.h"
#include <stdlib.h>

/**
 * delete_dnodeint_at_index - Delete a node at a specific index from a list
 * @head: A pointer to the first element of a list
 * @index: The index of the node to delete
 *
 * Return: 1 on success, -1 on failure
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index)
{
        dlistint_t *current;
        unsigned int i;

        if (*head == NULL)
                return (-1); /* Check if the list is empty */

        current = *head;

        /* Traverse the list to find the node at the specified index */
        for (i = 0; i < index && current != NULL; i++)
                current = current->next;

        if (current == NULL)
                return (-1); /* Index out of bounds */

        /* If the node to delete is the first node */
        if (index == 0)
        {
                *head = current->next;
                free(current);
                return (1);
        }

        current->prev->next = current->next;
        if (current->next != NULL)
                current->next->prev = current->prev;

        free(current);
        
        return (1);
}
