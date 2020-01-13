// stacker.cpp -- testing the Stack class
#include <iostream>
#include <cctype>
#include "Chapter10_exercise5.h"

int main()
{
    Stack st; // create an empty stack
    char ch;
    double sumPayment = 0.0;
    Customer po;
    std::cout << "Please enter A to add a purchase order,\n" << "P to process a PO, or Q to quit.\n";
    while (std::cin >> ch && toupper(ch) != 'Q')
    {
        while (std::cin.get() != '\n')
        {
            continue;
        }
        if (!isalpha(ch))
        {
            std::cout << '\a';
            continue;
        }
        switch (ch)
        {
            case 'A':
            case 'a':
                std::cout << "Enter a PO name to add: ";
                std::cin.getline(po.fullname, 35);
                std::cout << "Enter a PO payment to add: ";
                std::cin >> po.payment;
                if (st.isfull())
                {
                    std::cout << "stack already full\n";
                }
                else
                {
                    st.push(po);
                }
                break;
            case 'P':
            case 'p':
                if (st.isempty())
                {
                    std::cout << "stack already empty\n";
                }
                else
                {
                    st.pop(po);
                    std::cout << "PO " << po.fullname << " popped\n";
                    sumPayment += po.payment;
                    std::cout << "Sum of payments: $" << sumPayment << std::endl;
                }
                break;
        }
        std::cout << "Please enter A to add a purchase order,\n" << "P to process a PO, or Q to quit.\n";
    }
    std::cout << "Bye\n";
    return 0;
}