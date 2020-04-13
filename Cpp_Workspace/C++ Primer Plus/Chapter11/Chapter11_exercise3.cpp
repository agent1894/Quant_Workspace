// 11.9.3 -- rewrite 11.15 to report man, min , average in N times
#include <iostream>
#include <cstdlib> // rand(), srand() prototypes
#include <ctime> // time() prototype
// #include <algorithm> // for min, max, mean
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
    std::cout << "Enter target distance (q to quit): ";
    if (!(std::cin >> target))
    {
        std::cout << "Bye!" << std::endl;
        return 0;
    }
    double dstep;
    std::cout << "Enter step length: ";
    if (!(std::cin >> dstep))
    {
        std::cout << "Invalid step length, program terminated." << std::endl;
        return 0;
    }
    unsigned long ntimes;
    std::cout << "Enter the test times: ";
    if ((std::cin >> ntimes) && (ntimes >= 1))
    {
        unsigned long stepsArr[ntimes];
        for (int i = 0; i < ntimes; i++)
        {
            while (result.magval() < target)
            {
                direction = rand() % 360;
                step.reset(dstep, direction, Vector::POL);
                result = result + step;
                steps++;
            }
            stepsArr[i] = steps;
            steps = 0;
            result.reset(0.0, 0.0);
        }
        unsigned long min = stepsArr[0];
        unsigned long max = stepsArr[0];
        double tot = 0.0;
        for (int i = 0; i < ntimes; i++)
        {
            if (stepsArr[i] < min)
            {
                min = stepsArr[i];
            }
            if (stepsArr[i] > max)
            {
                max = stepsArr[i];
            }
            tot += stepsArr[i];
        }
        std::cout << "After " << ntimes << " times tests, " << std::endl;
        std::cout << "Maximum steps: " << max << std::endl;
        std::cout << "Minimum steps: " << min << std::endl;
        std::cout << "Average steps: " << tot / ntimes << std::endl;
    }
    else
    {
        std::cout << "Invalid test times, program terminated." << std::endl;
    }
    std::cout << "Bye!" << std::endl;

    return 0;
}