// 11.9.5 -- rewrite Stonewt class with status member
#ifndef STONEWT1_H_
#define STONEWT1_H
#include <iostream>

class Stonewt
{
    public:
        enum Mode {Stone, IntPound, FloatPound};
    private:
        enum {Lbs_per_stn = 14}; // pounds per stone, or static const int Lbs_per_stn = 14;
        int stone;
        double pds_left;
        double pounds;
        Mode mode;
    public:
        Stonewt();
        Stonewt(double lbs);
        Stonewt(int stn, double lbs);
        ~Stonewt()
        {

        }
        void set_stone()
        {
            mode = Stone;
        }
        void set_int()
        {
            mode = IntPound;
        }
        void set_float()
        {
            mode = FloatPound;
        }
        Stonewt operator+(Stonewt& swt) const;
        Stonewt operator-(Stonewt& swt) const;
        Stonewt operator*(double n) const;
        friend Stonewt operator*(double n, Stonewt& swt)
        {
            return swt * n;
        }
        friend std::ostream& operator<<(std::ostream& os, const Stonewt& swt);
};

#endif