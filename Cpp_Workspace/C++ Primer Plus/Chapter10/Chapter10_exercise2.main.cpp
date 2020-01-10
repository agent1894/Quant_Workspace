// 10.10.2 -- main function
#include <iostream>
#include "Chapter10_exercise2.h"

int main()
{
    Person one; // use default constructor
    Person two("Smythecraft"); // use #2 with one default argument
    Person three("Dimwiddy", "Sam"); // use #2, no defaults
    one.Show();
    std::cout << std::endl;
    one.FormalShow();
    std::cout << std::endl;
    two.Show();
    std::cout << std::endl;
    two.FormalShow();
    std::cout << std::endl;
    three.Show();
    std::cout << std::endl;
    three.FormalShow();
    std::cout << std::endl;
    return 0;
}