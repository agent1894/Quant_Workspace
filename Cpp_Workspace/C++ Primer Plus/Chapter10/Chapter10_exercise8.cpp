#include <iostream>
#include "Chapter10_exercise8.h"

bool SimpleList::isEmpty() const
{
    return length == 0;
}

bool SimpleList::isFull() const
{
    return length == maxLength;
}

void SimpleList::append(Item item)
{
    if (length < maxLength)
    {
        data[length++] = item;
        std::cout << "Append finished. " << std::endl;
    }
    else
    {
        std::cout << "This SimpleList is full and can not append data anymore." << std::endl;
    }
}

void SimpleList::manipulator(Item item)
{
    int i = 0;
    int match = 0;
    while (i < length)
    {
        if (data[i] != item)
        {
            i++;
        }
        else
        {
            Item temp = data[i] * data[i];
            data[i] = temp;
            i++;
            match++;
        }
    }
    if (match == 0)
    {
        std::cout << "There are no matched item " << item << " in the SimpleList!" << std::endl;
    }
}

void SimpleList::visit(void (*pf) (Item item, int n))
{
    for (int i = 0; i < length; i++)
    {
        (*pf)(data[i], i);
    }
}

void print(Item item, int n)
{
    std::cout << "The #" << n + 1 << " item is: " << item << std::endl;
}