#include "Chapter10_exercise4.h"

int main()
{
    using namespace SALES;
    double vals[3] = {2000, 3000, 5000};
    Sales salesNonInter = Sales(vals, 3);
    salesNonInter.showSales();

    Sales salesInter;
    salesInter.setSales();
    salesInter.showSales();

    return 0;
}