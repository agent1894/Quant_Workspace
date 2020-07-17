// 
// @Filename     :prime.cpp
// @Author       :Arthur Zhan
// @Init Time    :2020/06/16
// 


#include <iostream>
#include <vector>
#include <chrono>
#include "prime.h"

PRIME::PRIME(unsigned int n)
{
    num = n;
}

void PRIME::calculate()
{
    unsigned int i = 2;
    unsigned int limit;
    bool test = true;
    while (list.size() < num)
    {
        if (2 > i / 2 + 1)
        {
            limit = i;
        }
        else
        {
            limit = i / 2 + 1;
        }
        for (unsigned int d = 2; d < limit; ++d)
        {
            if (i % d == 0)
            {
                test = false;
                break;
            }
            else
            {
                test = true;
            }
        }
        if (test)
        {
            list.push_back(i);
        }
        i++;
    }
}

void PRIME::show()
{
    for (long unsigned int i = 0; i < list.size(); ++i)
    {
        std::cout << list[i] << " ";
    }
    std::cout << std::endl;
}
