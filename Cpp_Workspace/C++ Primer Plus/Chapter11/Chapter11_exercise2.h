// 11.9.2 -- rewrite head file for Vector 11.13
// use 11.15 (except the relying head file) to test the result which shoule be identical to the original
#ifndef MODVECTOR_H_
#define MODVECTOR_H_
#include <iostream>

namespace VECTOR
{
    class Vector
    {
        public:
            enum Mode{RECT, POL};
            // RECT for rectangular, POL for Polar modes
        private:
            double x; // horizontal value
            double y; // vertical value
            Mode mode; // RECT or POL
        public:
            Vector();
            Vector(double n1, double n2, Mode form = RECT);
            void reset(double n1, double n2, Mode form = RECT);
            ~Vector();
            double xval() const // report x value
            {
                return x;
            }
            double yval() const // report y value
            {
                return y;
            }
            double magval() const; // report magnitude
            double angval() const; // report angle
            void polar_mode(); // set mode to POL
            void rect_mode(); // set mode to RECT
            // operator overloading
            Vector operator+(const Vector& b) const;
            Vector operator-(const Vector& b) const;
            Vector operator-() const;
            Vector operator*(double d) const;
            // friends
            friend Vector operator*(double n , const Vector& a);
            friend std::ostream& operator<<(std::ostream& os, const Vector& v);
    };
} // end namespace VECTOR
#endif