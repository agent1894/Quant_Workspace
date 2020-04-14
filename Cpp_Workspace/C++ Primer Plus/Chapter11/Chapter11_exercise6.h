// 11.9.6 -- rewrite Stonewt class to overload relation operators
#ifndef STONEWT2_H_
#define STONEWT2_H_
#include <iostream>

class Stonewt
{
    private:
        enum {Lbs_per_stn = 14}; // pounds per stone, or static const int Lbs_per_stn = 14;
        int stone;
        double pds_left;
        double pounds;
    public:
        Stonewt()
        {
            stone = pounds = pds_left = 0;
        }
        Stonewt(double lbs);
        Stonewt(int stn, double lbs);
        ~Stonewt()
        {

        }
        bool operator<(const Stonewt& swt) const;
        bool operator<=(const Stonewt& swt) const;
        bool operator>(const Stonewt& swt) const;
        bool operator>=(const Stonewt& swt) const;
        bool operator==(const Stonewt& swt) const;
        bool operator!=(const Stonewt& swt) const;
        friend std::ostream& operator<<(std::ostream& os, const Stonewt& swt);
};

#endif