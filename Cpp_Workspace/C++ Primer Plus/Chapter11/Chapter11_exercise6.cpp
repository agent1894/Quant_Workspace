#include <iostream>
#include "Chapter11_exercise6.h"

Stonewt::Stonewt(double lbs)
{
    pounds = lbs;
    stone = lbs / Lbs_per_stn;
    pds_left = pounds - stone * Lbs_per_stn;
}

Stonewt::Stonewt(int stn, double lbs)
{
    stone = stn;
    pds_left = lbs;
    pounds = stn * Lbs_per_stn + lbs;
}

bool Stonewt::operator<(const Stonewt& swt) const
{
    return pounds < swt.pounds;
}

bool Stonewt::operator<=(const Stonewt& swt) const
{
    return pounds <= swt.pounds;
}
bool Stonewt::operator>(const Stonewt& swt) const
{
    return pounds > swt.pounds;
}
bool Stonewt::operator>=(const Stonewt& swt) const
{
    return pounds >= swt.pounds;
}
bool Stonewt::operator==(const Stonewt& swt) const
{
    return pounds == swt.pounds;
}
bool Stonewt::operator!=(const Stonewt& swt) const
{
    return pounds != swt.pounds;
}

std::ostream& operator<<(std::ostream& os, const Stonewt& swt)
{
    os << swt.pounds << " pounds, or " << swt.stone << " stone, " << swt.pds_left << " pounds";
    return os;
}