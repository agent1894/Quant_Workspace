// 10.10.8 -- class definition for the simpleList ADT
#ifndef SIMPLELIST_H_
#define SIMPLELIST_H_
#include <iostream>

typedef double Item;

class SimpleList
{
    private:
        int maxLength;
        int length;
        Item* data;

    public:
        SimpleList()
        {
            maxLength = 0;
            length = 0;
            data = new Item[0];
        }
        SimpleList(int l)
        {
            maxLength = l;
            data = new Item[l];
            length = 0;
        }
        ~SimpleList()
        {
            delete [] data;
        }
        bool isEmpty() const;
        bool isFull() const;
        void append(Item item);
        void manipulator(Item item);
        void visit(void (*pf) (Item item, int n));
};

void print(Item item, int n);

#endif