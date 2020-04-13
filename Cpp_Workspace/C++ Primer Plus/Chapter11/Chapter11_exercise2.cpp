// 11.9.2 -- rewrite cpp file for Vector 11.14
// use 11.15 to test the result which shoule be identical to the original
// compile with 11.15 randomwalk.cpp
#include <cmath>
#include <iostream>
#include "Chapter11_exercise2.h"
using std::sqrt;
using std::sin;
using std::cos;
using std::atan;
using std::atan2;
using std::cout;

namespace VECTOR
{
    // compute degrees in one radian
    const double Rad_to_deg = 45.0 / atan(1.0);
    // should be about 57.2957795130823

    Vector::Vector()
    {
        x = y = 0.0;
        mode = RECT;
    }

    Vector::Vector(double n1, double n2, Mode form)
    {
        mode = form;
        if (form == RECT)
        {
            x = n1;
            y = n2;
        }
        else if (form == POL)
        {
            x = n1 * cos(n2);
            y = n1 * sin(n2);
        }
        else
        {
            cout << "Incorrect 3rd argument to Vector() -- ";
            cout << "vector set to 0\n";
            x = y = 0.0;
            mode = RECT;
        }
    }

    double Vector::magval() const
    {
        double mag;
        mag = sqrt(x * x + y * y);
        return mag;
    }

    double Vector::angval() const
    {
        double ang;
        if (x == 0.0 && y == 0.0)
        {
            ang = 0.0;
        }
        else
        {
            ang = atan2(y, x) * Rad_to_deg;
        }
        return ang;
    }

    void Vector::reset(double n1, double n2, Mode form)
    {
        mode = form;
        if (form == RECT)
        {
            x = n1;
            y = n2;
        }
        else if (form == POL)
        {
            x = n1 * cos(n2);
            y = n1 * sin(n2);
        }
        else
        {
            cout << "Incorrect 3rd argument to Vector() -- ";
            cout << "vector set to 0\n";
            x = y = 0.0;
            mode = RECT;
        }
    }

    Vector::~Vector() // destructor
    {

    }

    void Vector::polar_mode() // set to polar mode
    {
        mode = POL;
    }
    
    void Vector::rect_mode() // set to rectangle mode
    {
        mode = RECT;
    }

    // operator overloading
    // add tow Vectors
    Vector Vector::operator+(const Vector& b) const
    {
        return Vector(x + b.x, y + b.y);
    }

    // substract Vector b from a
    Vector Vector::operator-(const Vector& b) const
    {
        return Vector(x - b.x, y - b.y);
    }

    // reverse sign of Vector
    Vector Vector::operator-() const
    {
        return Vector(-x, -y);
    }

    // multiply vector by n
    Vector Vector::operator*(double n) const
    {
        return Vector(n * x, n * y);
    }

    // friend methods
    // multiply n by Vector a
    Vector operator*(double n, const Vector& a)
    {
        return a * n;
    }

    // display rectangular coordinates if mode is RECT,
    // else display polar coordinates if mode is POL
    std::ostream& operator<<(std::ostream& os, const Vector& v)
    {
        if (v.mode == Vector::RECT)
        {
            os << "(x, y) = (" << v.x << ", " << v.y << ")";
        }
        else if (v.mode == Vector::POL)
        {
            os << "(m, a) = (" << v.magval() << ", ";
            os << v.angval() << ")";
        }
        else
        {
            os << "Vector object mode is invalid";
        }
        return os;
    }
} // end namespace VECTOR