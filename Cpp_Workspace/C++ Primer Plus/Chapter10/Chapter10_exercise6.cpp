#include <iostream>
#include "Chapter10_exercise6.h"

Move::Move(double a, double b)
{
    x = a;
    y = b;
}

void Move::showmove() const
{
    using namespace std;
    cout << "Current x is " << x << ", ";
    cout << "Current y is " << y << endl;
}

Move Move::add(const Move& m) const
{
    double tempx = 0.0;
    double tempy = 0.0;
    tempx = x + m.x;
    tempy = y + m.y;
    return Move(tempx, tempy);
}

void Move::reset(double a, double b)
{
    x = a;
    y = b;
}