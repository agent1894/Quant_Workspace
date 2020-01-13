// 10.10.5 -- customer structure with Stack class
// using Stack class in 10.10 stack.h
#ifndef STACK_H_
#define STACK_H_

struct Customer
{
    char fullname[35];
    double payment;
};

typedef Customer Item;

class Stack
{
    private:
        enum {MAX = 10}; // constant specific to class
        Item items[MAX]; // holds stack items
        int top; // index for top stack item
    public:
        Stack();
        bool isempty() const;
        bool isfull() const;
        // push() returns false if stack already is full, true otherwise
        bool push(const Item& item); // add item to stack
        // pop() returns false if stack already is empty, true otherwise
        bool pop(Item& item); // pop top into item
};

#endif
