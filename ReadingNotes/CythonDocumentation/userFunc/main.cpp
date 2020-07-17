#include "userFunc.h"
#include <iostream>

int main()
{
    sayHello();
    double x, y;
    std::cout << "Enter x: ";
    std::cin >> x;
    std::cout << "Enter y: ";
    std::cin >> y;
    double result = addSquare(x, y);
    std::cout << "The sum of x^2 and y^2 is: " << result << std::endl;
    sayBye();

    return 0;
}