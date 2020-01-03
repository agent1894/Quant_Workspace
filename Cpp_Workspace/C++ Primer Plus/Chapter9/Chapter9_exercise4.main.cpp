// 9.6.4 -- exercise under namespace
#include <iostream>
#include "Chapter9_exercise4.h"

int main()
{
    SALES::Sales salesNonInter;
    double vals[3] = {2000, 3000, 5000};
    SALES::setSales(salesNonInter, vals, 3);
    SALES::showSales(salesNonInter);

    SALES::Sales salesInter;
    SALES::setSales(salesInter);
    SALES::showSales(salesInter);

    return 0;
}