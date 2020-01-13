#include <iostream>
#include "Chapter10_exercise8.h"

int main()
{
    using namespace std;
    SimpleList list(5);
    if (list.isEmpty())
    {
        cout << "Now this list is empty." << endl;
    }
    list.append(10.0);
    list.append(20.0);
    list.append(30.0);
    list.visit(print);
    list.append(40.0);
    list.append(50.0);
    list.visit(print);
    cout << "Now we try to manipulate one item." << endl;
    list.manipulator(50.0);
    list.visit(print);
    cout << "Now we try to manipulate one item which not in SimpleList." << endl;
    list.manipulator(60.0);
    if (list.isFull())
    {
        cout << "Now this list is full." << endl;
    }
    return 0;
}