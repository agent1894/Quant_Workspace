// 11.9.1 -- rewrite 11.15 randomwalk
#include <iostream>
#include <fstream>
#include <cstdlib> // rand(), srand() prototypes
#include <ctime> // time() prototype
#include "Chapter11_13.vector.h"

int main()
{
    using VECTOR::Vector;
    srand(time(0)); // seed random-number generator
    double direction;
    Vector step;
    Vector result(0.0, 0.0);
    unsigned long steps = 0;
    double target;
    double dstep;
    std::ofstream outFile; // create object ofr output
    outFile.open("randomwalk.txt"); // associate with a file
    if (!outFile.is_open())
    {
        std::cerr << "Can't open output file. Bye!" << std::endl;
        exit(EXIT_FAILURE);
    }
    std::cout << "Enter target distance (q to quit): ";
    while (std::cin >> target)
    {
        outFile << "Target Distance: " << target << ", ";
        std::cout << "Enter step length: ";
        if (!(std::cin >> dstep))
        {
            break;
        }
        else
        {
            outFile << "Step Size: " << dstep << std::endl;
        }
        while (result.magval() < target)
        {
            outFile << steps << ": ";
            outFile << result << std::endl;
            direction = rand() % 360;
            step.reset(dstep, direction, Vector::POL);
            result = result + step;
            steps++;
        }
        outFile << "After " << steps << " steps, the subject has the following location:\n";
        outFile << result << std::endl;
        result.polar_mode();
        outFile << " or\n" << result << std::endl;
        outFile << "Average outward distance per step = ";
        outFile << result.magval() / steps << std::endl;
        steps = 0;
        result.reset(0.0, 0.0);
        std::cout << "Enter target distance (q to quit): ";
    }
    outFile.close();
    std::cout << "Bye!\n";
    std::cin.clear();
    while (std::cin.get() != '\n')
    {
        continue;
    }

    return 0;
}
