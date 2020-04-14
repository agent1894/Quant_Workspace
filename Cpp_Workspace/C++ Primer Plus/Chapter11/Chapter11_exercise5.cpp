#include <iostream>
#include "Chapter11_exercise5.h"

Stonewt::Stonewt()
{
    stone = pounds = pds_left = 0;
    mode = FloatPound;
}

Stonewt::Stonewt(double lbs)
{
    mode = FloatPound;
    pounds = lbs;
    stone = int(pounds) / Lbs_per_stn;
    pds_left = lbs - stone * Lbs_per_stn;
}

Stonewt::Stonewt(int stn, double lbs)
{
    mode = Stone;
    stone = stn;
    pds_left = lbs;
    pounds = stn * Lbs_per_stn + lbs;
}

Stonewt Stonewt::operator+(Stonewt& swt) const
{
    double sumpounds = pounds + swt.pounds;
    Stonewt sum(sumpounds);
    return sum;
}

Stonewt Stonewt::operator-(Stonewt& swt) const
{
    double diffpounds = pounds - swt.pounds;
    Stonewt diff(diffpounds);
    return diff;
}

Stonewt Stonewt::operator*(double n) const
{
    double timepounds = pounds * n;
    Stonewt times(timepounds);
    return times;
}

std::ostream& operator<<(std::ostream& os, const Stonewt& swt)
{
    if (swt.mode == Stonewt::FloatPound)
    {
        os << "The display mode is float, weighted: ";
        os << swt.pounds << " pounds";
    }
    else if (swt.mode == Stonewt::Stone)
    {
        os << "The display mode is stone, weighted: ";
        os << swt.stone << " stone, " << swt.pds_left << " pounds";
    }
    else
    {
        os << "The display mode is int, weighted: ";
        os << int(swt.stone) << " pounds";
    }
    return os;
}