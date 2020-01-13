#include <iostream>
#include "Chapter10_exercise7.h"

Plorg::Plorg(const char ar[], int ci)
{
    std::strcpy(name, ar);
    CI = ci;
}

void Plorg::changeCI(int ci)
{
    CI = ci;
}

void Plorg::showData() const
{
    std::cout << "The name of Plorg is: " << name << ", ";
    std::cout << "The CI of Plorg is: " << CI << std::endl;
}