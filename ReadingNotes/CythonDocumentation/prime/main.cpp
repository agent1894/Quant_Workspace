// 
// @Filename     :prime.cpp
// @Author       :Arthur Zhan
// @Init Time    :2020/06/16
// 


#include <iostream>
#include <chrono>
#include "prime.h"
int main()
{
    std::cout << "Enter the numbers of primes: ";
    unsigned int num;
    std::cin >> num; 
    auto start = std::chrono::system_clock::now();
    PRIME data = PRIME(num);
    data.calculate();
    data.show();
    auto end = std::chrono::system_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::microseconds>(end - start);
    std::cout << "Time costs: " << duration.count()  << " us" << std::endl;
}