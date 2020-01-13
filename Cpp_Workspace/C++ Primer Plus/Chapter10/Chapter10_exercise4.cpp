// 10.10.4 -- function prototypes
#include <iostream>
#include "Chapter10_exercise4.h"

namespace SALES
{
    SALES::Sales::Sales(const double ar[], int n)
    {
        for (int i = 0; i < ((n < QUARTERS) ? n : QUARTERS); i++)
        {
            sales[i] = ar[i];
        }
        if (n < QUARTERS)
        {
            for (int i = 0; i < (QUARTERS - n); i++)
            {
                sales[i + n] = 0.0;
            }
        }
        calculate();
    }

    void SALES::Sales::setSales()
    {
        for (int i = 0; i < QUARTERS; i++)
        {
            std::cout << "Please enter the " << i + 1 << " quarter sales: ";
            std::cin >> sales[i];
        }
        calculate();
    }

    void SALES::Sales::showSales() const
    {
        std::cout << "The sales of four quarters are: " << std::endl;
        for (int i = 0; i < QUARTERS; i++)
        {
            std::cout << "Quarter " << i + 1 << ": " << sales[i] << std::endl;
        }
        std::cout << "The average sales is: " << average << std::endl;
        std::cout << "The min sales is: " << min << std::endl;
        std::cout << "The max sales is: " << max << std::endl;
    }
}