// 10.10.3 -- re-write 9.6.1 golf
#ifndef GOLF_H_
#define GOLF_H_
#include <cstring>
class Golf
{
    private:
        static const int Len = 40;
        char fullName[Len];
        int handicap;
    public:
        Golf()
        {
            std::strcpy(fullName, "Null");
            handicap = 0;
        }
        Golf(const char* fn, int hc);
        Golf& setgolf(Golf& g);
        // It seems that there are some misunderstandings of the exercise requirements,
        // after check out the official solutions, here are the function prototype which
        // satisfies the exercise.
        int setgolfOfficial();
        void sethandicap(int hc);
        void showgolf() const;
};

#endif