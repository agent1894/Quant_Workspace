// 9.6.4 -- contains functions called by main()
#include <iostream>
#include "Chapter9_exercise4.h"

namespace SALES
{
    void setSales(SALES::Sales& s, const double ar[], int n)
    {
        double sum = 0.0;
        double min = ar[0];
        double max = ar[0];
        for (int i = 0; i < ((n < 4) ? n : 4); i++)
        {
            s.sales[i] = ar[i];
            sum += ar[i];
            min = (min < ar[i]) ? min : ar[i];
            max = (max > ar[i]) ? max : ar[i];
        }
        if (n < 4)
        {
            for (int i = 0; i < (4 - n); i++)
            {
                s.sales[i + n] = 0.0;
            }
        }
        s.min = min;
        s.max = max;
        if (n != 0)
            s.average = sum / n;
        else
            s.average = 0.0;
    }

    void setSales(SALES::Sales& s)
    {
        double sum = 0.0;
        for (int i = 0; i < 4; i++)
        {
            std::cout << "Please enter the " << i + 1 << " quarter sales: ";
            std::cin >> s.sales[i];
            sum += s.sales[i];
        }
        double min = s.sales[0];
        double max = s.sales[0];
        for (int i = 0; i < 4; i++)
        {
            min = (min < s.sales[i]) ? min : s.sales[i];
            max = (max > s.sales[i]) ? max : s.sales[i];
        }
        s.min = min;
        s.max = max;
        s.average = sum / 4.0;
    }

    void showSales(const SALES::Sales& s)
    {
        std::cout << "The sales of four quarters are: " << std::endl;
        for (int i = 0; i < 4; i++)
        {
            std::cout << "Quarter " << i + 1 << ": " << s.sales[i] << std::endl;
        }
        std::cout << "The average sales is: " << s.average << std::endl;
        std::cout << "The min sales is: " << s.min << std::endl;
        std::cout << "The max sales is: " << s.max << std::endl;
    }
}