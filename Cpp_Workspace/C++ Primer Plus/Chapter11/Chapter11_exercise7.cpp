#include <iostream>
#include "Chapter11_exercise7.h"

complex::complex(double r, double i)
{
    real = r;
    imaginary = i;
}


complex complex::operator+(const complex& cpx) const
{
    complex temp(real + cpx.real, imaginary + cpx.imaginary);
    return temp;
}

complex complex::operator-(const complex& cpx) const
{
    complex temp(real - cpx.real, imaginary - cpx.imaginary);
    return temp;
}

complex complex::operator*(const complex& cpx) const
{
    double r = real * cpx.real - imaginary * cpx.imaginary;
    double i = real * cpx.imaginary + imaginary * cpx.real;
    complex temp(r, i);
    return temp;
}

complex complex::operator*(const double n) const
{
    complex temp(n * real, n * imaginary);
    return temp;
}

complex operator*(const double n, const complex& cpx)
{
    return cpx * n;
}

complex complex::operator~() const
{
    complex temp(real, -imaginary);
    return temp;
}

std::ostream& operator<<(std::ostream& os, const complex& cpx)
{
    os << "(" << cpx.real << ", " << cpx.imaginary << "i)";
    return os;
}

std::istream& operator>>(std::istream& is, complex& cpx)
{
    double r;
    double i;
    std::cout << "real: ";
    if (is >> r)
    {
        cpx.real = r;
        if (is >> i)
        {
            std::cout << "imaginary: ";
            cpx.imaginary = i;
        }
    }
    return is;
}