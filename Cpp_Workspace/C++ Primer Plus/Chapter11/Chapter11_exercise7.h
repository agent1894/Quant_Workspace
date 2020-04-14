// 11.9.7 -- complex number
#ifndef COMPLEX_H_
#define COMPLEX_H_
#include <iostream>

class complex
{
    private:
        double real;
        double imaginary;
    public:
        complex()
        {
            real = imaginary = 0.0;
        }
        complex(double r, double i);
        ~complex()
        {

        }
        complex operator+(const complex& cpx) const;
        complex operator-(const complex& cpx) const;
        complex operator*(const complex& cpx) const;
        complex operator*(const double n) const;
        friend complex operator*(const double n, const complex& cpx);
        complex operator~() const;
        friend std::ostream& operator<<(std::ostream& os, const complex& cpx);
        friend std::istream& operator>>(std::istream& is, complex& cpx);
};

#endif